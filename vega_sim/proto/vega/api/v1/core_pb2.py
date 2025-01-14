# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vega/api/v1/core.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ... import vega_pb2 as vega_dot_vega__pb2
from ...events.v1 import events_pb2 as vega_dot_events_dot_v1_dot_events__pb2
from ...commands.v1 import (
    transaction_pb2 as vega_dot_commands_dot_v1_dot_transaction__pb2,
)
from protoc_gen_openapiv2.options import (
    annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2,
)


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x16vega/api/v1/core.proto\x12\x0bvega.api.v1\x1a\x0fvega/vega.proto\x1a\x1bvega/events/v1/events.proto\x1a"vega/commands/v1/transaction.proto\x1a.protoc-gen-openapiv2/options/annotations.proto"i\n\x1aPropagateChainEventRequest\x12\x14\n\x05\x65vent\x18\x01 \x01(\x0cR\x05\x65vent\x12\x17\n\x07pub_key\x18\x02 \x01(\tR\x06pubKey\x12\x1c\n\tsignature\x18\x03 \x01(\x0cR\tsignature"7\n\x1bPropagateChainEventResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"\xd7\x01\n\x18SubmitTransactionRequest\x12-\n\x02tx\x18\x01 \x01(\x0b\x32\x1d.vega.commands.v1.TransactionR\x02tx\x12>\n\x04type\x18\x02 \x01(\x0e\x32*.vega.api.v1.SubmitTransactionRequest.TypeR\x04type"L\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nTYPE_ASYNC\x10\x01\x12\r\n\tTYPE_SYNC\x10\x02\x12\x0f\n\x0bTYPE_COMMIT\x10\x03"\xa0\x01\n\x19SubmitTransactionResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x17\n\x07tx_hash\x18\x02 \x01(\tR\x06txHash\x12\x12\n\x04\x63ode\x18\x03 \x01(\rR\x04\x63ode\x12\x12\n\x04\x64\x61ta\x18\x04 \x01(\tR\x04\x64\x61ta\x12\x10\n\x03log\x18\x05 \x01(\tR\x03log\x12\x16\n\x06height\x18\x06 \x01(\x03R\x06height"H\n\x17\x43heckTransactionRequest\x12-\n\x02tx\x18\x01 \x01(\x0b\x32\x1d.vega.commands.v1.TransactionR\x02tx"\x82\x01\n\x18\x43heckTransactionResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x12\n\x04\x63ode\x18\x02 \x01(\rR\x04\x63ode\x12\x1d\n\ngas_wanted\x18\x03 \x01(\x03R\tgasWanted\x12\x19\n\x08gas_used\x18\x04 \x01(\x03R\x07gasUsed"\xbe\x01\n\x1bSubmitRawTransactionRequest\x12\x0e\n\x02tx\x18\x01 \x01(\x0cR\x02tx\x12\x41\n\x04type\x18\x02 \x01(\x0e\x32-.vega.api.v1.SubmitRawTransactionRequest.TypeR\x04type"L\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nTYPE_ASYNC\x10\x01\x12\r\n\tTYPE_SYNC\x10\x02\x12\x0f\n\x0bTYPE_COMMIT\x10\x03"\xa3\x01\n\x1cSubmitRawTransactionResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x17\n\x07tx_hash\x18\x02 \x01(\tR\x06txHash\x12\x12\n\x04\x63ode\x18\x03 \x01(\rR\x04\x63ode\x12\x12\n\x04\x64\x61ta\x18\x04 \x01(\tR\x04\x64\x61ta\x12\x10\n\x03log\x18\x05 \x01(\tR\x03log\x12\x16\n\x06height\x18\x06 \x01(\x03R\x06height",\n\x1a\x43heckRawTransactionRequest\x12\x0e\n\x02tx\x18\x01 \x01(\x0cR\x02tx"\x85\x01\n\x1b\x43heckRawTransactionResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x12\n\x04\x63ode\x18\x02 \x01(\rR\x04\x63ode\x12\x1d\n\ngas_wanted\x18\x03 \x01(\x03R\tgasWanted\x12\x19\n\x08gas_used\x18\x04 \x01(\x03R\x07gasUsed"\x14\n\x12GetVegaTimeRequest"3\n\x13GetVegaTimeResponse\x12\x1c\n\ttimestamp\x18\x01 \x01(\x03R\ttimestamp"\xa1\x01\n\x16ObserveEventBusRequest\x12\x30\n\x04type\x18\x01 \x03(\x0e\x32\x1c.vega.events.v1.BusEventTypeR\x04type\x12\x1b\n\tmarket_id\x18\x02 \x01(\tR\x08marketId\x12\x19\n\x08party_id\x18\x03 \x01(\tR\x07partyId\x12\x1d\n\nbatch_size\x18\x04 \x01(\x03R\tbatchSize"K\n\x17ObserveEventBusResponse\x12\x30\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x18.vega.events.v1.BusEventR\x06\x65vents"\x13\n\x11StatisticsRequest"M\n\x12StatisticsResponse\x12\x37\n\nstatistics\x18\x01 \x01(\x0b\x32\x17.vega.api.v1.StatisticsR\nstatistics"\x88\x0b\n\nStatistics\x12!\n\x0c\x62lock_height\x18\x01 \x01(\x04R\x0b\x62lockHeight\x12%\n\x0e\x62\x61\x63klog_length\x18\x02 \x01(\x04R\rbacklogLength\x12\x1f\n\x0btotal_peers\x18\x03 \x01(\x04R\ntotalPeers\x12!\n\x0cgenesis_time\x18\x04 \x01(\tR\x0bgenesisTime\x12!\n\x0c\x63urrent_time\x18\x05 \x01(\tR\x0b\x63urrentTime\x12\x1b\n\tvega_time\x18\x06 \x01(\tR\x08vegaTime\x12)\n\x06status\x18\x07 \x01(\x0e\x32\x11.vega.ChainStatusR\x06status\x12 \n\x0ctx_per_block\x18\x08 \x01(\x04R\ntxPerBlock\x12(\n\x10\x61verage_tx_bytes\x18\t \x01(\x04R\x0e\x61verageTxBytes\x12\x37\n\x18\x61verage_orders_per_block\x18\n \x01(\x04R\x15\x61verageOrdersPerBlock\x12*\n\x11trades_per_second\x18\x0b \x01(\x04R\x0ftradesPerSecond\x12*\n\x11orders_per_second\x18\x0c \x01(\x04R\x0fordersPerSecond\x12#\n\rtotal_markets\x18\r \x01(\x04R\x0ctotalMarkets\x12*\n\x11total_amend_order\x18\x10 \x01(\x04R\x0ftotalAmendOrder\x12,\n\x12total_cancel_order\x18\x11 \x01(\x04R\x10totalCancelOrder\x12,\n\x12total_create_order\x18\x12 \x01(\x04R\x10totalCreateOrder\x12!\n\x0ctotal_orders\x18\x13 \x01(\x04R\x0btotalOrders\x12!\n\x0ctotal_trades\x18\x14 \x01(\x04R\x0btotalTrades\x12/\n\x13order_subscriptions\x18\x15 \x01(\rR\x12orderSubscriptions\x12/\n\x13trade_subscriptions\x18\x16 \x01(\rR\x12tradeSubscriptions\x12\x31\n\x14\x63\x61ndle_subscriptions\x18\x17 \x01(\rR\x13\x63\x61ndleSubscriptions\x12<\n\x1amarket_depth_subscriptions\x18\x18 \x01(\rR\x18marketDepthSubscriptions\x12\x37\n\x17positions_subscriptions\x18\x19 \x01(\rR\x16positionsSubscriptions\x12\x33\n\x15\x61\x63\x63ount_subscriptions\x18\x1a \x01(\rR\x14\x61\x63\x63ountSubscriptions\x12:\n\x19market_data_subscriptions\x18\x1b \x01(\rR\x17marketDataSubscriptions\x12(\n\x10\x61pp_version_hash\x18\x1c \x01(\tR\x0e\x61ppVersionHash\x12\x1f\n\x0b\x61pp_version\x18\x1d \x01(\tR\nappVersion\x12#\n\rchain_version\x18\x1e \x01(\tR\x0c\x63hainVersion\x12%\n\x0e\x62lock_duration\x18\x1f \x01(\x04R\rblockDuration\x12\x16\n\x06uptime\x18  \x01(\tR\x06uptime\x12\x19\n\x08\x63hain_id\x18! \x01(\tR\x07\x63hainId\x12K\n"market_depth_updates_subscriptions\x18" \x01(\rR\x1fmarketDepthUpdatesSubscriptions\x12\x1d\n\nblock_hash\x18# \x01(\tR\tblockHash"\x18\n\x16LastBlockHeightRequest"\x91\x03\n\x17LastBlockHeightResponse\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\x12\x12\n\x04hash\x18\x02 \x01(\tR\x04hash\x12\x33\n\x16spam_pow_hash_function\x18\x03 \x01(\tR\x13spamPowHashFunction\x12.\n\x13spam_pow_difficulty\x18\x04 \x01(\rR\x11spamPowDifficulty\x12\x41\n\x1espam_pow_number_of_past_blocks\x18\x05 \x01(\rR\x19spamPowNumberOfPastBlocks\x12\x42\n\x1fspam_pow_number_of_tx_per_block\x18\x06 \x01(\rR\x19spamPowNumberOfTxPerBlock\x12\x43\n\x1espam_pow_increasing_difficulty\x18\x07 \x01(\x08R\x1bspamPowIncreasingDifficulty\x12\x19\n\x08\x63hain_id\x18\x08 \x01(\tR\x07\x63hainId2\xf4\x06\n\x0b\x43oreService\x12\x62\n\x11SubmitTransaction\x12%.vega.api.v1.SubmitTransactionRequest\x1a&.vega.api.v1.SubmitTransactionResponse\x12h\n\x13PropagateChainEvent\x12\'.vega.api.v1.PropagateChainEventRequest\x1a(.vega.api.v1.PropagateChainEventResponse\x12M\n\nStatistics\x12\x1e.vega.api.v1.StatisticsRequest\x1a\x1f.vega.api.v1.StatisticsResponse\x12\\\n\x0fLastBlockHeight\x12#.vega.api.v1.LastBlockHeightRequest\x1a$.vega.api.v1.LastBlockHeightResponse\x12P\n\x0bGetVegaTime\x12\x1f.vega.api.v1.GetVegaTimeRequest\x1a .vega.api.v1.GetVegaTimeResponse\x12`\n\x0fObserveEventBus\x12#.vega.api.v1.ObserveEventBusRequest\x1a$.vega.api.v1.ObserveEventBusResponse(\x01\x30\x01\x12k\n\x14SubmitRawTransaction\x12(.vega.api.v1.SubmitRawTransactionRequest\x1a).vega.api.v1.SubmitRawTransactionResponse\x12_\n\x10\x43heckTransaction\x12$.vega.api.v1.CheckTransactionRequest\x1a%.vega.api.v1.CheckTransactionResponse\x12h\n\x13\x43heckRawTransaction\x12\'.vega.api.v1.CheckRawTransactionRequest\x1a(.vega.api.v1.CheckRawTransactionResponseBdZ,code.vegaprotocol.io/vega/protos/vega/api/v1\x92\x41\x33\x12\x18\n\x0eVega core APIs2\x06\x30.57.0\x1a\x13lb.testnet.vega.xyz*\x02\x01\x02\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "vega.api.v1.core_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z,code.vegaprotocol.io/vega/protos/vega/api/v1\222A3\022\030\n\016Vega core APIs2\0060.57.0\032\023lb.testnet.vega.xyz*\002\001\002"
    _PROPAGATECHAINEVENTREQUEST._serialized_start = 169
    _PROPAGATECHAINEVENTREQUEST._serialized_end = 274
    _PROPAGATECHAINEVENTRESPONSE._serialized_start = 276
    _PROPAGATECHAINEVENTRESPONSE._serialized_end = 331
    _SUBMITTRANSACTIONREQUEST._serialized_start = 334
    _SUBMITTRANSACTIONREQUEST._serialized_end = 549
    _SUBMITTRANSACTIONREQUEST_TYPE._serialized_start = 473
    _SUBMITTRANSACTIONREQUEST_TYPE._serialized_end = 549
    _SUBMITTRANSACTIONRESPONSE._serialized_start = 552
    _SUBMITTRANSACTIONRESPONSE._serialized_end = 712
    _CHECKTRANSACTIONREQUEST._serialized_start = 714
    _CHECKTRANSACTIONREQUEST._serialized_end = 786
    _CHECKTRANSACTIONRESPONSE._serialized_start = 789
    _CHECKTRANSACTIONRESPONSE._serialized_end = 919
    _SUBMITRAWTRANSACTIONREQUEST._serialized_start = 922
    _SUBMITRAWTRANSACTIONREQUEST._serialized_end = 1112
    _SUBMITRAWTRANSACTIONREQUEST_TYPE._serialized_start = 473
    _SUBMITRAWTRANSACTIONREQUEST_TYPE._serialized_end = 549
    _SUBMITRAWTRANSACTIONRESPONSE._serialized_start = 1115
    _SUBMITRAWTRANSACTIONRESPONSE._serialized_end = 1278
    _CHECKRAWTRANSACTIONREQUEST._serialized_start = 1280
    _CHECKRAWTRANSACTIONREQUEST._serialized_end = 1324
    _CHECKRAWTRANSACTIONRESPONSE._serialized_start = 1327
    _CHECKRAWTRANSACTIONRESPONSE._serialized_end = 1460
    _GETVEGATIMEREQUEST._serialized_start = 1462
    _GETVEGATIMEREQUEST._serialized_end = 1482
    _GETVEGATIMERESPONSE._serialized_start = 1484
    _GETVEGATIMERESPONSE._serialized_end = 1535
    _OBSERVEEVENTBUSREQUEST._serialized_start = 1538
    _OBSERVEEVENTBUSREQUEST._serialized_end = 1699
    _OBSERVEEVENTBUSRESPONSE._serialized_start = 1701
    _OBSERVEEVENTBUSRESPONSE._serialized_end = 1776
    _STATISTICSREQUEST._serialized_start = 1778
    _STATISTICSREQUEST._serialized_end = 1797
    _STATISTICSRESPONSE._serialized_start = 1799
    _STATISTICSRESPONSE._serialized_end = 1876
    _STATISTICS._serialized_start = 1879
    _STATISTICS._serialized_end = 3295
    _LASTBLOCKHEIGHTREQUEST._serialized_start = 3297
    _LASTBLOCKHEIGHTREQUEST._serialized_end = 3321
    _LASTBLOCKHEIGHTRESPONSE._serialized_start = 3324
    _LASTBLOCKHEIGHTRESPONSE._serialized_end = 3725
    _CORESERVICE._serialized_start = 3728
    _CORESERVICE._serialized_end = 4612
# @@protoc_insertion_point(module_scope)
