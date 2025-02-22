# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vega/checkpoint/v1/checkpoint.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ... import vega_pb2 as vega_dot_vega__pb2
from ... import assets_pb2 as vega_dot_assets__pb2
from ... import governance_pb2 as vega_dot_governance__pb2
from ...events.v1 import events_pb2 as vega_dot_events_dot_v1_dot_events__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n#vega/checkpoint/v1/checkpoint.proto\x12\x12vega.checkpoint.v1\x1a\x0fvega/vega.proto\x1a\x11vega/assets.proto\x1a\x15vega/governance.proto\x1a\x1bvega/events/v1/events.proto";\n\x0f\x43heckpointState\x12\x12\n\x04hash\x18\x01 \x01(\x0cR\x04hash\x12\x14\n\x05state\x18\x02 \x01(\x0cR\x05state"\x9f\x03\n\nCheckpoint\x12\x1e\n\ngovernance\x18\x01 \x01(\x0cR\ngovernance\x12\x16\n\x06\x61ssets\x18\x02 \x01(\x0cR\x06\x61ssets\x12\x1e\n\ncollateral\x18\x03 \x01(\x0cR\ncollateral\x12-\n\x12network_parameters\x18\x04 \x01(\x0cR\x11networkParameters\x12\x1e\n\ndelegation\x18\x05 \x01(\x0cR\ndelegation\x12\x14\n\x05\x65poch\x18\x06 \x01(\x0cR\x05\x65poch\x12\x14\n\x05\x62lock\x18\x07 \x01(\x0cR\x05\x62lock\x12\x18\n\x07rewards\x18\x08 \x01(\x0cR\x07rewards\x12\x18\n\x07\x62\x61nking\x18\t \x01(\x0cR\x07\x62\x61nking\x12\x1e\n\nvalidators\x18\n \x01(\x0cR\nvalidators\x12\x18\n\x07staking\x18\x0b \x01(\x0cR\x07staking\x12)\n\x10multisig_control\x18\x0c \x01(\x0cR\x0fmultisigControl\x12%\n\x0emarket_tracker\x18\r \x01(\x0cR\rmarketTracker"U\n\nAssetEntry\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x37\n\rasset_details\x18\x02 \x01(\x0b\x32\x12.vega.AssetDetailsR\x0c\x61ssetDetails"\x96\x01\n\x06\x41ssets\x12\x36\n\x06\x61ssets\x18\x01 \x03(\x0b\x32\x1e.vega.checkpoint.v1.AssetEntryR\x06\x61ssets\x12T\n\x16pending_listing_assets\x18\x02 \x03(\x0b\x32\x1e.vega.checkpoint.v1.AssetEntryR\x14pendingListingAssets"T\n\x0c\x41ssetBalance\x12\x14\n\x05party\x18\x01 \x01(\tR\x05party\x12\x14\n\x05\x61sset\x18\x02 \x01(\tR\x05\x61sset\x12\x18\n\x07\x62\x61lance\x18\x03 \x01(\tR\x07\x62\x61lance"J\n\nCollateral\x12<\n\x08\x62\x61lances\x18\x01 \x03(\x0b\x32 .vega.checkpoint.v1.AssetBalanceR\x08\x62\x61lances";\n\tNetParams\x12.\n\x06params\x18\x01 \x03(\x0b\x32\x16.vega.NetworkParameterR\x06params"9\n\tProposals\x12,\n\tproposals\x18\x01 \x03(\x0b\x32\x0e.vega.ProposalR\tproposals"\x8e\x01\n\rDelegateEntry\x12\x14\n\x05party\x18\x01 \x01(\tR\x05party\x12\x12\n\x04node\x18\x02 \x01(\tR\x04node\x12\x16\n\x06\x61mount\x18\x03 \x01(\tR\x06\x61mount\x12\x1e\n\nundelegate\x18\x04 \x01(\x08R\nundelegate\x12\x1b\n\tepoch_seq\x18\x05 \x01(\x04R\x08\x65pochSeq"\xab\x01\n\x08\x44\x65legate\x12\x39\n\x06\x61\x63tive\x18\x01 \x03(\x0b\x32!.vega.checkpoint.v1.DelegateEntryR\x06\x61\x63tive\x12;\n\x07pending\x18\x02 \x03(\x0b\x32!.vega.checkpoint.v1.DelegateEntryR\x07pending\x12\'\n\x0f\x61uto_delegation\x18\x03 \x03(\tR\x0e\x61utoDelegation"\x1f\n\x05\x42lock\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height"E\n\x07Rewards\x12:\n\x07rewards\x18\x01 \x03(\x0b\x32 .vega.checkpoint.v1.RewardPayoutR\x07rewards"\x7f\n\x0cRewardPayout\x12\x1f\n\x0bpayout_time\x18\x01 \x01(\x03R\npayoutTime\x12N\n\x0erewards_payout\x18\x02 \x03(\x0b\x32\'.vega.checkpoint.v1.PendingRewardPayoutR\rrewardsPayout"\xf0\x01\n\x13PendingRewardPayout\x12!\n\x0c\x66rom_account\x18\x01 \x01(\tR\x0b\x66romAccount\x12\x14\n\x05\x61sset\x18\x02 \x01(\tR\x05\x61sset\x12\x42\n\x0cparty_amount\x18\x03 \x03(\x0b\x32\x1f.vega.checkpoint.v1.PartyAmountR\x0bpartyAmount\x12!\n\x0ctotal_reward\x18\x04 \x01(\tR\x0btotalReward\x12\x1b\n\tepoch_seq\x18\x05 \x01(\tR\x08\x65pochSeq\x12\x1c\n\ttimestamp\x18\x06 \x01(\x03R\ttimestamp";\n\x0bPartyAmount\x12\x14\n\x05party\x18\x01 \x01(\tR\x05party\x12\x16\n\x06\x61mount\x18\x02 \x01(\tR\x06\x61mount"\xb9\x01\n\x12PendingKeyRotation\x12?\n\x1crelative_target_block_height\x18\x01 \x01(\x04R\x19relativeTargetBlockHeight\x12\x17\n\x07node_id\x18\x02 \x01(\tR\x06nodeId\x12\x1e\n\x0bnew_pub_key\x18\x03 \x01(\tR\tnewPubKey\x12)\n\x11new_pub_key_index\x18\x04 \x01(\rR\x0enewPubKeyIndex"\x97\x01\n\x1aPendingEthereumKeyRotation\x12?\n\x1crelative_target_block_height\x18\x01 \x01(\x04R\x19relativeTargetBlockHeight\x12\x17\n\x07node_id\x18\x02 \x01(\tR\x06nodeId\x12\x1f\n\x0bnew_address\x18\x03 \x01(\tR\nnewAddress"\xd6\x01\n\x11ScheduledTransfer\x12*\n\x08transfer\x18\x01 \x01(\x0b\x32\x0e.vega.TransferR\x08transfer\x12\x34\n\x0c\x61\x63\x63ount_type\x18\x02 \x01(\x0e\x32\x11.vega.AccountTypeR\x0b\x61\x63\x63ountType\x12\x1c\n\treference\x18\x03 \x01(\tR\treference\x12\x41\n\x0foneoff_transfer\x18\x04 \x01(\x0b\x32\x18.vega.events.v1.TransferR\x0eoneoffTransfer"}\n\x17ScheduledTransferAtTime\x12\x1d\n\ndeliver_on\x18\x01 \x01(\x03R\tdeliverOn\x12\x43\n\ttransfers\x18\x02 \x03(\x0b\x32%.vega.checkpoint.v1.ScheduledTransferR\ttransfers"_\n\x12RecurringTransfers\x12I\n\x13recurring_transfers\x18\x01 \x03(\x0b\x32\x18.vega.events.v1.TransferR\x12recurringTransfers"\xff\x01\n\x07\x42\x61nking\x12W\n\x11transfers_at_time\x18\x01 \x03(\x0b\x32+.vega.checkpoint.v1.ScheduledTransferAtTimeR\x0ftransfersAtTime\x12W\n\x13recurring_transfers\x18\x02 \x01(\x0b\x32&.vega.checkpoint.v1.RecurringTransfersR\x12recurringTransfers\x12\x42\n\x0c\x62ridge_state\x18\x03 \x01(\x0b\x32\x1f.vega.checkpoint.v1.BridgeStateR\x0b\x62ridgeState"e\n\x0b\x42ridgeState\x12\x16\n\x06\x61\x63tive\x18\x01 \x01(\x08R\x06\x61\x63tive\x12!\n\x0c\x62lock_height\x18\x02 \x01(\x04R\x0b\x62lockHeight\x12\x1b\n\tlog_index\x18\x03 \x01(\x04R\x08logIndex"\xaa\x02\n\nValidators\x12K\n\x0fvalidator_state\x18\x01 \x03(\x0b\x32".vega.checkpoint.v1.ValidatorStateR\x0evalidatorState\x12Z\n\x15pending_key_rotations\x18\x02 \x03(\x0b\x32&.vega.checkpoint.v1.PendingKeyRotationR\x13pendingKeyRotations\x12s\n\x1epending_ethereum_key_rotations\x18\x03 \x03(\x0b\x32..vega.checkpoint.v1.PendingEthereumKeyRotationR\x1bpendingEthereumKeyRotations"\x88\x02\n\x0eValidatorState\x12J\n\x10validator_update\x18\x01 \x01(\x0b\x32\x1f.vega.events.v1.ValidatorUpdateR\x0fvalidatorUpdate\x12\x16\n\x06status\x18\x02 \x01(\x05R\x06status\x12\x30\n\x14\x65th_events_forwarded\x18\x03 \x01(\x04R\x12\x65thEventsForwarded\x12\'\n\x0fvalidator_power\x18\x04 \x01(\x03R\x0evalidatorPower\x12\x37\n\rranking_score\x18\x05 \x01(\x0b\x32\x12.vega.RankingScoreR\x0crankingScore"k\n\x07Staking\x12\x38\n\x08\x61\x63\x63\x65pted\x18\x01 \x03(\x0b\x32\x1c.vega.events.v1.StakeLinkingR\x08\x61\x63\x63\x65pted\x12&\n\x0flast_block_seen\x18\x02 \x01(\x04R\rlastBlockSeen"\xd2\x01\n\x0fMultisigControl\x12\x42\n\x07signers\x18\x01 \x03(\x0b\x32(.vega.events.v1.ERC20MultiSigSignerEventR\x07signers\x12S\n\rthreshold_set\x18\x02 \x01(\x0b\x32..vega.events.v1.ERC20MultiSigThresholdSetEventR\x0cthresholdSet\x12&\n\x0flast_block_seen\x18\x03 \x01(\x04R\rlastBlockSeen"c\n\rMarketTracker\x12R\n\x0fmarket_activity\x18\x01 \x03(\x0b\x32).vega.checkpoint.v1.MarketActivityTrackerR\x0emarketActivity"\x99\x03\n\x15MarketActivityTracker\x12\x16\n\x06market\x18\x01 \x01(\tR\x06market\x12\x14\n\x05\x61sset\x18\x02 \x01(\tR\x05\x61sset\x12M\n\x13maker_fees_received\x18\x03 \x03(\x0b\x32\x1d.vega.checkpoint.v1.PartyFeesR\x11makerFeesReceived\x12\x45\n\x0fmaker_fees_paid\x18\x04 \x03(\x0b\x32\x1d.vega.checkpoint.v1.PartyFeesR\rmakerFeesPaid\x12\x36\n\x07lp_fees\x18\x05 \x03(\x0b\x32\x1d.vega.checkpoint.v1.PartyFeesR\x06lpFees\x12\x1a\n\x08proposer\x18\x06 \x01(\tR\x08proposer\x12\x1d\n\nbonus_paid\x18\x07 \x03(\tR\tbonusPaid\x12!\n\x0cvalue_traded\x18\x08 \x01(\tR\x0bvalueTraded\x12&\n\x0fready_to_delete\x18\t \x01(\x08R\rreadyToDelete"3\n\tPartyFees\x12\x14\n\x05party\x18\x01 \x01(\tR\x05party\x12\x10\n\x03\x66\x65\x65\x18\x02 \x01(\tR\x03\x66\x65\x65\x42\x35Z3code.vegaprotocol.io/vega/protos/vega/checkpoint/v1b\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "vega.checkpoint.v1.checkpoint_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"Z3code.vegaprotocol.io/vega/protos/vega/checkpoint/v1"
    )
    _CHECKPOINTSTATE._serialized_start = 147
    _CHECKPOINTSTATE._serialized_end = 206
    _CHECKPOINT._serialized_start = 209
    _CHECKPOINT._serialized_end = 624
    _ASSETENTRY._serialized_start = 626
    _ASSETENTRY._serialized_end = 711
    _ASSETS._serialized_start = 714
    _ASSETS._serialized_end = 864
    _ASSETBALANCE._serialized_start = 866
    _ASSETBALANCE._serialized_end = 950
    _COLLATERAL._serialized_start = 952
    _COLLATERAL._serialized_end = 1026
    _NETPARAMS._serialized_start = 1028
    _NETPARAMS._serialized_end = 1087
    _PROPOSALS._serialized_start = 1089
    _PROPOSALS._serialized_end = 1146
    _DELEGATEENTRY._serialized_start = 1149
    _DELEGATEENTRY._serialized_end = 1291
    _DELEGATE._serialized_start = 1294
    _DELEGATE._serialized_end = 1465
    _BLOCK._serialized_start = 1467
    _BLOCK._serialized_end = 1498
    _REWARDS._serialized_start = 1500
    _REWARDS._serialized_end = 1569
    _REWARDPAYOUT._serialized_start = 1571
    _REWARDPAYOUT._serialized_end = 1698
    _PENDINGREWARDPAYOUT._serialized_start = 1701
    _PENDINGREWARDPAYOUT._serialized_end = 1941
    _PARTYAMOUNT._serialized_start = 1943
    _PARTYAMOUNT._serialized_end = 2002
    _PENDINGKEYROTATION._serialized_start = 2005
    _PENDINGKEYROTATION._serialized_end = 2190
    _PENDINGETHEREUMKEYROTATION._serialized_start = 2193
    _PENDINGETHEREUMKEYROTATION._serialized_end = 2344
    _SCHEDULEDTRANSFER._serialized_start = 2347
    _SCHEDULEDTRANSFER._serialized_end = 2561
    _SCHEDULEDTRANSFERATTIME._serialized_start = 2563
    _SCHEDULEDTRANSFERATTIME._serialized_end = 2688
    _RECURRINGTRANSFERS._serialized_start = 2690
    _RECURRINGTRANSFERS._serialized_end = 2785
    _BANKING._serialized_start = 2788
    _BANKING._serialized_end = 3043
    _BRIDGESTATE._serialized_start = 3045
    _BRIDGESTATE._serialized_end = 3146
    _VALIDATORS._serialized_start = 3149
    _VALIDATORS._serialized_end = 3447
    _VALIDATORSTATE._serialized_start = 3450
    _VALIDATORSTATE._serialized_end = 3714
    _STAKING._serialized_start = 3716
    _STAKING._serialized_end = 3823
    _MULTISIGCONTROL._serialized_start = 3826
    _MULTISIGCONTROL._serialized_end = 4036
    _MARKETTRACKER._serialized_start = 4038
    _MARKETTRACKER._serialized_end = 4137
    _MARKETACTIVITYTRACKER._serialized_start = 4140
    _MARKETACTIVITYTRACKER._serialized_end = 4549
    _PARTYFEES._serialized_start = 4551
    _PARTYFEES._serialized_end = 4602
# @@protoc_insertion_point(module_scope)
