from concurrent.futures import ThreadPoolExecutor
from unittest.mock import MagicMock, patch

import grpc
import pytest
import vega_sim.proto.data_node.api.v1 as data_node_protos
import vega_sim.proto.data_node.api.v2 as data_node_protos_v2
import vega_sim.proto.vega as vega_protos
import vega_sim.proto.vega.events.v1.events_pb2 as events_protos
from tests.vega_sim.api.test_data_raw import (
    core_servicer_and_port,
    trading_data_servicer_and_port,
    trading_data_v2_servicer_and_port,
)
from vega_sim.api.data import (
    AccountData,
    Fee,
    MarginLevels,
    MissingAssetError,
    Order,
    OrdersBySide,
    Trade,
    asset_decimals,
    best_prices,
    find_asset_id,
    get_trades,
    margin_levels,
    market_position_decimals,
    market_price_decimals,
    open_orders_by_market,
    order_subscription,
    party_account,
)
from vega_sim.grpc.client import (
    VegaCoreClient,
    VegaTradingDataClient,
    VegaTradingDataClientV2,
)
from vega_sim.proto.data_node.api.v1.trading_data_pb2_grpc import (
    add_TradingDataServiceServicer_to_server,
)
from vega_sim.proto.data_node.api.v2.trading_data_pb2_grpc import (
    add_TradingDataServiceServicer_to_server as add_TradingDataServiceServicer_v2_to_server,
)
from vega_sim.proto.vega.api.v1.core_pb2_grpc import add_CoreServiceServicer_to_server


def test_party_account(trading_data_servicer_and_port):
    def PartyAccounts(self, request, context):
        return data_node_protos.trading_data.PartyAccountsResponse(
            accounts=[
                vega_protos.vega.Account(
                    market_id=request.market_id,
                    balance="1051",
                    type=vega_protos.vega.ACCOUNT_TYPE_BOND,
                ),
                vega_protos.vega.Account(
                    market_id=request.market_id,
                    balance="2041",
                    type=vega_protos.vega.ACCOUNT_TYPE_FEES_INFRASTRUCTURE,
                ),
                vega_protos.vega.Account(
                    market_id=request.market_id,
                    balance="5235",
                    type=vega_protos.vega.ACCOUNT_TYPE_GENERAL,
                ),
                vega_protos.vega.Account(
                    market_id=request.market_id,
                    balance="6423",
                    type=vega_protos.vega.ACCOUNT_TYPE_MARGIN,
                ),
            ]
        )

    server, port, mock_servicer = trading_data_servicer_and_port
    mock_servicer.PartyAccounts = PartyAccounts

    add_TradingDataServiceServicer_to_server(mock_servicer(), server)

    data_client = VegaTradingDataClient(f"localhost:{port}")
    res = party_account(
        "PUB_KEY",
        asset_id="a1",
        market_id="MARK_ID",
        data_client=data_client,
        asset_dp=2,
    )

    assert res == AccountData(52.35, 64.23, 10.51)

    with patch("vega_sim.api.data.asset_decimals", lambda asset_id, data_client: 2):
        res2 = party_account(
            "PUB_KEY",
            asset_id="a1",
            market_id="MARK_ID",
            data_client=data_client,
        )
        assert res2 == res


def test_find_asset_id(trading_data_servicer_and_port):
    def Assets(self, request, context):
        return data_node_protos.trading_data.AssetsResponse(
            assets=[
                vega_protos.assets.Asset(
                    id="asset1_id",
                    details=vega_protos.assets.AssetDetails(
                        name="asset1", symbol="A1", decimals=5
                    ),
                ),
                vega_protos.assets.Asset(
                    id="asset2_id",
                    details=vega_protos.assets.AssetDetails(
                        name="asset2", symbol="A2", decimals=5
                    ),
                ),
                vega_protos.assets.Asset(
                    id="asset3_id",
                    details=vega_protos.assets.AssetDetails(
                        name="asset3", symbol="A3", decimals=5
                    ),
                ),
            ]
        )

    server, port, mock_servicer = trading_data_servicer_and_port
    mock_servicer.Assets = Assets

    add_TradingDataServiceServicer_to_server(mock_servicer(), server)

    data_client = VegaTradingDataClient(f"localhost:{port}")
    res = find_asset_id(symbol="A2", data_client=data_client)
    assert res == "asset2_id"

    with pytest.raises(MissingAssetError):
        find_asset_id(symbol="A4", data_client=data_client, raise_on_missing=True)

    empty_res = find_asset_id(
        symbol="A4", data_client=data_client, raise_on_missing=False
    )
    assert empty_res is None


@patch("vega_sim.api.data_raw.market_info")
def test_market_price_decimals(mkt_info_mock):
    asset_mock = MagicMock()
    asset_mock.decimal_places = 2
    mkt_info_mock.return_value = asset_mock

    assert market_price_decimals("MKT", None) == 2


@patch("vega_sim.api.data_raw.market_info")
def test_market_position_decimals(mkt_info_mock):
    asset_mock = MagicMock()
    asset_mock.position_decimal_places = 2
    mkt_info_mock.return_value = asset_mock

    assert market_position_decimals("MKT", None) == 2


@patch("vega_sim.api.data_raw.asset_info")
def test_asset_decimals(mkt_info_mock):
    asset_mock = MagicMock()
    asset_mock.details.decimals = 3
    mkt_info_mock.return_value = asset_mock

    assert asset_decimals("ASSET", None) == 3


@patch("vega_sim.api.data_raw.market_data")
def test_best_prices(mkt_data_mock):
    mkt_data = MagicMock()
    mkt_data_mock.return_value = mkt_data

    mkt_data.best_static_bid_price = "202"
    mkt_data.best_static_offer_price = "212"

    bid_res, ask_res = best_prices("mkt", None, 2)
    assert bid_res == pytest.approx(2.02)
    assert ask_res == pytest.approx(2.12)


def test_open_orders_by_market(trading_data_servicer_and_port):
    def OrdersByMarket(self, request, context):
        return data_node_protos.trading_data.OrdersByMarketResponse(
            orders=[
                vega_protos.vega.Order(
                    id="id1",
                    market_id="market",
                    status=vega_protos.vega.Order.Status.STATUS_ACTIVE,
                    reference="ref1",
                    side=vega_protos.vega.SIDE_BUY,
                    price="10100",
                    size=101,
                    remaining=101,
                    time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
                    type=vega_protos.vega.Order.Type.TYPE_LIMIT,
                    created_at=1653266950,
                    expires_at=1653276950,
                    party_id="party1",
                    updated_at=1653266950,
                    version=1,
                ),
                vega_protos.vega.Order(
                    id="id2",
                    market_id="market",
                    status=vega_protos.vega.Order.Status.STATUS_CANCELLED,
                    reference="ref1",
                    side=vega_protos.vega.SIDE_BUY,
                    price="10100",
                    size=101,
                    remaining=101,
                    time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
                    type=vega_protos.vega.Order.Type.TYPE_LIMIT,
                    created_at=1653266950,
                    expires_at=1653276950,
                    party_id="party1",
                    updated_at=1653266950,
                    version=1,
                ),
                vega_protos.vega.Order(
                    id="id3",
                    market_id="market",
                    status=vega_protos.vega.Order.Status.STATUS_FILLED,
                    reference="ref1",
                    side=vega_protos.vega.SIDE_BUY,
                    price="10100",
                    size=101,
                    remaining=0,
                    time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
                    type=vega_protos.vega.Order.Type.TYPE_LIMIT,
                    created_at=1653266950,
                    expires_at=1653276950,
                    party_id="party1",
                    updated_at=1653266950,
                    version=1,
                ),
                vega_protos.vega.Order(
                    id="id4",
                    market_id="market",
                    status=vega_protos.vega.Order.Status.STATUS_ACTIVE,
                    reference="ref1",
                    side=vega_protos.vega.SIDE_BUY,
                    price="10110",
                    size=101,
                    remaining=101,
                    time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
                    type=vega_protos.vega.Order.Type.TYPE_LIMIT,
                    created_at=1653266950,
                    expires_at=1653276950,
                    party_id="party1",
                    updated_at=1653266950,
                    version=1,
                ),
                vega_protos.vega.Order(
                    id="id5",
                    market_id="market",
                    status=vega_protos.vega.Order.Status.STATUS_ACTIVE,
                    reference="ref1",
                    side=vega_protos.vega.SIDE_BUY,
                    price="10100",
                    size=101,
                    remaining=101,
                    time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
                    type=vega_protos.vega.Order.Type.TYPE_LIMIT,
                    created_at=1653266950,
                    expires_at=1653276950,
                    party_id="party2",
                    updated_at=1653266950,
                    version=1,
                ),
                vega_protos.vega.Order(
                    id="id6",
                    market_id="market",
                    status=vega_protos.vega.Order.Status.STATUS_ACTIVE,
                    reference="ref1",
                    side=vega_protos.vega.SIDE_SELL,
                    price="10400",
                    size=111,
                    remaining=121,
                    time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
                    type=vega_protos.vega.Order.Type.TYPE_LIMIT,
                    created_at=1653266950,
                    expires_at=1653276950,
                    party_id="party1",
                    updated_at=1653266950,
                    version=1,
                ),
                vega_protos.vega.Order(
                    id="id7",
                    market_id="market",
                    status=vega_protos.vega.Order.Status.STATUS_ACTIVE,
                    reference="ref1",
                    side=vega_protos.vega.SIDE_SELL,
                    price="10100",
                    size=101,
                    remaining=101,
                    time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
                    type=vega_protos.vega.Order.Type.TYPE_LIMIT,
                    created_at=1653266950,
                    expires_at=1653276950,
                    party_id="party1",
                    updated_at=1653266950,
                    version=1,
                ),
            ]
        )

    server, port, mock_servicer = trading_data_servicer_and_port
    mock_servicer.OrdersByMarket = OrdersByMarket

    add_TradingDataServiceServicer_to_server(mock_servicer(), server)

    data_client = VegaTradingDataClient(f"localhost:{port}")

    res = open_orders_by_market(
        market_id="MARK1",
        data_client=data_client,
        price_decimals=2,
        position_decimals=1,
    )

    assert res == OrdersBySide(
        bids=[
            Order(
                id="id1",
                market_id="market",
                status=vega_protos.vega.Order.Status.STATUS_ACTIVE,
                reference="ref1",
                side=vega_protos.vega.SIDE_BUY,
                price=101,
                size=10.1,
                remaining=10.1,
                time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
                order_type=vega_protos.vega.Order.Type.TYPE_LIMIT,
                created_at=1653266950,
                expires_at=1653276950,
                party_id="party1",
                updated_at=1653266950,
                version=1,
            ),
            Order(
                id="id4",
                market_id="market",
                status=vega_protos.vega.Order.Status.STATUS_ACTIVE,
                reference="ref1",
                side=vega_protos.vega.SIDE_BUY,
                price=101.10,
                size=10.1,
                remaining=10.1,
                time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
                order_type=vega_protos.vega.Order.Type.TYPE_LIMIT,
                created_at=1653266950,
                expires_at=1653276950,
                party_id="party1",
                updated_at=1653266950,
                version=1,
            ),
            Order(
                id="id5",
                market_id="market",
                status=vega_protos.vega.Order.Status.STATUS_ACTIVE,
                reference="ref1",
                side=vega_protos.vega.SIDE_BUY,
                price=101.00,
                size=10.1,
                remaining=10.1,
                time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
                order_type=vega_protos.vega.Order.Type.TYPE_LIMIT,
                created_at=1653266950,
                expires_at=1653276950,
                party_id="party2",
                updated_at=1653266950,
                version=1,
            ),
        ],
        asks=[
            Order(
                id="id6",
                market_id="market",
                status=vega_protos.vega.Order.Status.STATUS_ACTIVE,
                reference="ref1",
                side=vega_protos.vega.SIDE_SELL,
                price=104.00,
                size=11.1,
                remaining=12.1,
                time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
                order_type=vega_protos.vega.Order.Type.TYPE_LIMIT,
                created_at=1653266950,
                expires_at=1653276950,
                party_id="party1",
                updated_at=1653266950,
                version=1,
            ),
            Order(
                id="id7",
                market_id="market",
                status=vega_protos.vega.Order.Status.STATUS_ACTIVE,
                reference="ref1",
                side=vega_protos.vega.SIDE_SELL,
                price=101.00,
                size=10.1,
                remaining=10.1,
                time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
                order_type=vega_protos.vega.Order.Type.TYPE_LIMIT,
                created_at=1653266950,
                expires_at=1653276950,
                party_id="party1",
                updated_at=1653266950,
                version=1,
            ),
        ],
    )


@patch("vega_sim.api.data.market_position_decimals")
@patch("vega_sim.api.data.market_price_decimals")
def test_order_subscription(mkt_price_mock, mkt_pos_mock, core_servicer_and_port):
    mkt_pos_mock.return_value = 2
    mkt_price_mock.return_value = 2
    orders = [
        vega_protos.vega.Order(
            id="id1",
            market_id="market",
            status=vega_protos.vega.Order.Status.STATUS_ACTIVE,
            reference="ref1",
            side=vega_protos.vega.SIDE_BUY,
            price="10100",
            size=101,
            remaining=101,
            time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
            type=vega_protos.vega.Order.Type.TYPE_LIMIT,
            created_at=1653266950,
            expires_at=1653276950,
            party_id="party1",
            updated_at=1653266950,
            version=1,
        ),
        vega_protos.vega.Order(
            id="id2",
            market_id="market",
            status=vega_protos.vega.Order.Status.STATUS_CANCELLED,
            reference="ref1",
            side=vega_protos.vega.SIDE_BUY,
            price="10100",
            size=101,
            remaining=101,
            time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
            type=vega_protos.vega.Order.Type.TYPE_LIMIT,
            created_at=1653266950,
            expires_at=1653276950,
            party_id="party1",
            updated_at=1653266950,
            version=1,
        ),
        vega_protos.vega.Order(
            id="id3",
            market_id="market",
            status=vega_protos.vega.Order.Status.STATUS_FILLED,
            reference="ref1",
            side=vega_protos.vega.SIDE_BUY,
            price="10100",
            size=101,
            remaining=0,
            time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
            type=vega_protos.vega.Order.Type.TYPE_LIMIT,
            created_at=1653266950,
            expires_at=1653276950,
            party_id="party1",
            updated_at=1653266950,
            version=1,
        ),
        vega_protos.vega.Order(
            id="id4",
            market_id="market",
            status=vega_protos.vega.Order.Status.STATUS_ACTIVE,
            reference="ref1",
            side=vega_protos.vega.SIDE_BUY,
            price="10110",
            size=101,
            remaining=101,
            time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
            type=vega_protos.vega.Order.Type.TYPE_LIMIT,
            created_at=1653266950,
            expires_at=1653276950,
            party_id="party1",
            updated_at=1653266950,
            version=1,
        ),
        vega_protos.vega.Order(
            id="id5",
            market_id="market",
            status=vega_protos.vega.Order.Status.STATUS_ACTIVE,
            reference="ref1",
            side=vega_protos.vega.SIDE_BUY,
            price="10100",
            size=101,
            remaining=101,
            time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
            type=vega_protos.vega.Order.Type.TYPE_LIMIT,
            created_at=1653266950,
            expires_at=1653276950,
            party_id="party2",
            updated_at=1653266950,
            version=1,
        ),
        vega_protos.vega.Order(
            id="id6",
            market_id="market",
            status=vega_protos.vega.Order.Status.STATUS_ACTIVE,
            reference="ref1",
            side=vega_protos.vega.SIDE_SELL,
            price="10400",
            size=111,
            remaining=121,
            time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
            type=vega_protos.vega.Order.Type.TYPE_LIMIT,
            created_at=1653266950,
            expires_at=1653276950,
            party_id="party1",
            updated_at=1653266950,
            version=1,
        ),
        vega_protos.vega.Order(
            id="id7",
            market_id="market",
            status=vega_protos.vega.Order.Status.STATUS_ACTIVE,
            reference="ref1",
            side=vega_protos.vega.SIDE_SELL,
            price="10100",
            size=101,
            remaining=101,
            time_in_force=vega_protos.vega.Order.TimeInForce.TIME_IN_FORCE_GTC,
            type=vega_protos.vega.Order.Type.TYPE_LIMIT,
            created_at=1653266950,
            expires_at=1653276950,
            party_id="party1",
            updated_at=1653266950,
            version=1,
        ),
    ]

    def ObserveEventBus(self, request, context):
        for order_chunk in [orders[:3], orders[3:6], orders[6:]]:
            yield vega_protos.api.v1.core.ObserveEventBusResponse(
                events=[events_protos.BusEvent(order=order) for order in order_chunk]
            )

    server, port, mock_servicer = core_servicer_and_port
    mock_servicer.ObserveEventBus = ObserveEventBus

    add_CoreServiceServicer_to_server(mock_servicer(), server)

    data_client = VegaCoreClient(f"localhost:{port}")

    queue = order_subscription(data_client=data_client, trading_data_client=None)
    for order in orders:
        assert order.id == next(queue).id


@patch("vega_sim.api.data.asset_decimals")
def test_market_limits(mk_asset_decimals, trading_data_v2_servicer_and_port):
    expected = [
        MarginLevels(
            maintenance_margin=10,
            search_level=15,
            initial_margin=20,
            collateral_release_level=30,
            party_id="party",
            market_id="market",
            asset="asset",
            timestamp=1251825938592,
        )
    ]

    def ListMarginLevels(self, request, context):
        return data_node_protos_v2.trading_data.ListMarginLevelsResponse(
            margin_levels=data_node_protos_v2.trading_data.MarginConnection(
                page_info=data_node_protos_v2.trading_data.PageInfo(
                    has_next_page=False,
                    has_previous_page=False,
                    start_cursor="",
                    end_cursor="",
                ),
                edges=[
                    data_node_protos_v2.trading_data.MarginEdge(
                        cursor="cursor",
                        node=vega_protos.vega.MarginLevels(
                            maintenance_margin="100",
                            search_level="150",
                            initial_margin="200",
                            collateral_release_level="300",
                            party_id="party",
                            market_id="market",
                            asset="asset",
                            timestamp=1251825938592,
                        ),
                    )
                ],
            )
        )

    mk_asset_decimals.return_value = 1
    server, port, mock_servicer = trading_data_v2_servicer_and_port
    mock_servicer.ListMarginLevels = ListMarginLevels

    add_TradingDataServiceServicer_v2_to_server(mock_servicer(), server)

    data_client = VegaTradingDataClientV2(f"localhost:{port}")
    res = margin_levels(
        party_id="party",
        market_id="market",
        data_client=data_client,
        data_client_v1=None,
    )

    assert res == expected


@patch("vega_sim.api.data.asset_decimals")
@patch("vega_sim.api.data.market_price_decimals")
@patch("vega_sim.api.data.market_position_decimals")
@patch("vega_sim.api.data_raw.market_info")
def test_get_trades(
    mk_mkt_info,
    mk_pos_decimals,
    mk_price_decimals,
    mk_asset_decimals,
    trading_data_v2_servicer_and_port,
):
    expected = [
        Trade(
            id="t1",
            market_id="m1",
            price=10,
            size=10,
            buyer="b1",
            seller="s1",
            aggressor=vega_protos.vega.SIDE_BUY,
            buy_order="bo1",
            sell_order="so1",
            timestamp=100,
            trade_type=vega_protos.vega.Trade.TYPE_DEFAULT,
            buyer_fee=Fee(maker_fee=10, infrastructure_fee=1.2, liquidity_fee=1.4),
            seller_fee=Fee(maker_fee=20, infrastructure_fee=12.2, liquidity_fee=14.4),
            buyer_auction_batch=100,
            seller_auction_batch=96,
        )
    ]

    def ListTrades(self, request, context):
        return data_node_protos_v2.trading_data.ListTradesResponse(
            trades=data_node_protos_v2.trading_data.TradeConnection(
                page_info=data_node_protos_v2.trading_data.PageInfo(
                    has_next_page=False,
                    has_previous_page=False,
                    start_cursor="",
                    end_cursor="",
                ),
                edges=[
                    data_node_protos_v2.trading_data.TradeEdge(
                        cursor="cursor",
                        node=vega_protos.vega.Trade(
                            id="t1",
                            market_id="m1",
                            price="100",
                            size=10,
                            buyer="b1",
                            seller="s1",
                            aggressor=vega_protos.vega.SIDE_BUY,
                            buy_order="bo1",
                            sell_order="so1",
                            timestamp=100,
                            type=vega_protos.vega.Trade.TYPE_DEFAULT,
                            buyer_fee=vega_protos.vega.Fee(
                                maker_fee="100",
                                infrastructure_fee="12",
                                liquidity_fee="14",
                            ),
                            seller_fee=vega_protos.vega.Fee(
                                maker_fee="200",
                                infrastructure_fee="122",
                                liquidity_fee="144",
                            ),
                            buyer_auction_batch=100,
                            seller_auction_batch=96,
                        ),
                    )
                ],
            )
        )

    mk_asset_decimals.return_value = 1
    mk_pos_decimals.return_value = 0
    mk_price_decimals.return_value = 1

    mk_mkt = MagicMock()
    mk_mkt_info.return_value = mk_mkt
    mk_mkt.tradable_instrument.instrument.future.settlement_asset = "a1"

    server, port, mock_servicer = trading_data_v2_servicer_and_port
    mock_servicer.ListTrades = ListTrades

    add_TradingDataServiceServicer_v2_to_server(mock_servicer(), server)

    data_client = VegaTradingDataClientV2(f"localhost:{port}")
    res = get_trades(
        party_id="party",
        market_id="market",
        data_client=data_client,
        data_client_v1=None,
    )

    assert res == expected
