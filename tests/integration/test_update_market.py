import pytest

from tests.integration.utils.fixtures import (
    vega_service_with_market,
    vega_service,
    create_and_faucet_wallet,
    WalletConfig,
    MM_WALLET,
)
from vega_sim.null_service import VegaServiceNull
import vega_sim.proto.vega as vega_protos


LIQ = WalletConfig("liq", "liq")


@pytest.mark.integration
def test_update_market_liquidity_monitoring(vega_service_with_market: VegaServiceNull):
    vega = vega_service_with_market
    market_id = vega.all_markets()[0].id

    vega.wait_for_total_catchup()

    create_and_faucet_wallet(vega=vega, wallet=LIQ)

    pre_market = vega.market_info(market_id)

    vega.update_market(
        MM_WALLET.name,
        market_id=market_id,
        updated_liquidity_monitoring_parameters=vega_protos.markets.LiquidityMonitoringParameters(
            target_stake_parameters=vega_protos.markets.TargetStakeParameters(
                time_window=3600, scaling_factor=1
            ),
            triggering_ratio=0.6,
            auction_extension=0,
        ),
    )
    vega.wait_for_total_catchup()
    after_market = vega.market_info(market_id)

    assert pre_market.liquidity_monitoring_parameters.triggering_ratio == 0.7
    assert after_market.liquidity_monitoring_parameters.triggering_ratio == 0.6


@pytest.mark.integration
def test_update_market_price_monitoring(vega_service_with_market: VegaServiceNull):
    vega = vega_service_with_market
    market_id = vega.all_markets()[0].id

    vega.wait_for_total_catchup()

    create_and_faucet_wallet(vega=vega, wallet=LIQ)

    pre_market = vega.market_info(market_id)

    vega.update_market(
        MM_WALLET.name,
        market_id=market_id,
        updated_price_monitoring_parameters=vega_protos.markets.PriceMonitoringParameters(
            triggers=[
                vega_protos.markets.PriceMonitoringTrigger(
                    # in seconds, so 24h, the longer the wider bounds
                    horizon=600,
                    # number close to but below 1 leads to wide bounds
                    probability="0.8",
                    # in seconds
                    auction_extension=5,
                )
            ]
        ),
    )
    vega.wait_for_total_catchup()
    after_market = vega.market_info(market_id)

    assert pre_market.price_monitoring_settings.parameters.triggers[0].horizon == 86400
    assert after_market.price_monitoring_settings.parameters.triggers[0].horizon == 600


@pytest.mark.integration
def test_update_market_instrument(vega_service_with_market: VegaServiceNull):
    vega = vega_service_with_market
    market_id = vega.all_markets()[0].id

    vega.wait_for_total_catchup()

    create_and_faucet_wallet(vega=vega, wallet=LIQ)

    pre_market = vega.market_info(market_id)
    curr_inst = pre_market.tradable_instrument.instrument
    curr_fut = curr_inst.future
    curr_fut_prod = vega_protos.governance.UpdateFutureProduct(
        quote_name=curr_fut.quote_name,
        oracle_spec_for_settlement_data=vega_protos.oracles.v1.spec.OracleSpecConfiguration(
            pub_keys=curr_fut.oracle_spec_for_settlement_data.pub_keys,
            filters=curr_fut.oracle_spec_for_settlement_data.filters,
        ),
        oracle_spec_for_trading_termination=vega_protos.oracles.v1.spec.OracleSpecConfiguration(
            pub_keys=curr_fut.oracle_spec_for_trading_termination.pub_keys,
            filters=curr_fut.oracle_spec_for_trading_termination.filters,
        ),
        oracle_spec_binding=curr_fut.oracle_spec_binding,
        settlement_data_decimals=curr_fut.settlement_data_decimals,
    )
    updated_instrument = vega_protos.governance.UpdateInstrumentConfiguration(
        code="BTCUSD",
        future=curr_fut_prod,
    )
    vega.update_market(
        MM_WALLET.name,
        market_id=market_id,
        updated_instrument=updated_instrument,
    )
    vega.wait_for_total_catchup()
    after_market = vega.market_info(market_id)

    assert pre_market.tradable_instrument.instrument.code == "CRYPTO:BTCDAI/DEC22"
    assert after_market.tradable_instrument.instrument.code == "BTCUSD"


@pytest.mark.integration
def test_update_market_risk(vega_service_with_market: VegaServiceNull):
    vega = vega_service_with_market
    market_id = vega.all_markets()[0].id

    vega.wait_for_total_catchup()

    create_and_faucet_wallet(vega=vega, wallet=LIQ)

    pre_market = vega.market_info(market_id)

    vega.update_market(
        MM_WALLET.name,
        market_id=market_id,
        updated_log_normal_risk_model=vega_protos.markets.LogNormalRiskModel(
            risk_aversion_parameter=0.5,
            tau=1.90128526884173e-06,
            params=vega_protos.markets.LogNormalModelParams(mu=0, r=0.016, sigma=3.0),
        ),
    )
    vega.wait_for_total_catchup()
    after_market = vega.market_info(market_id)

    assert (
        pre_market.tradable_instrument.log_normal_risk_model.risk_aversion_parameter
        == 1e-06
    )
    assert (
        after_market.tradable_instrument.log_normal_risk_model.risk_aversion_parameter
        == 0.5
    )
