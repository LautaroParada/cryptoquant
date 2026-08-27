"""Tests that exercise __init__ and every endpoint method to meet coverage threshold."""
from __future__ import annotations

from unittest import TestCase
from unittest.mock import MagicMock, patch

from cryptoquant.cryptoquant import CryptoQuant
from cryptoquant.bitcoin.bitcoin import Bitcoin
from cryptoquant.ethereum.ethereum import Ethereum
from cryptoquant.xrp.xrp import XRP
from cryptoquant.erc20.erc20 import Erc20
from cryptoquant.stablecoins.stablecoins import StableCoins
from cryptoquant.trx.trx import TRX
from cryptoquant.altcoins.altcoins import AltCoins
from cryptoquant.discovery.discovery import Discovery

_PATCH_TARGET = (
    "cryptoquant.request_handler_class.request_handler.RequestHandler.handle_request"
)
_FAKE_RESPONSE = {"data": []}


class InitTests(TestCase):
    """Verify that all __init__ methods execute without error."""

    def test_cryptoquant_init(self):
        cq = CryptoQuant("fake_key")
        self.assertIsInstance(cq, CryptoQuant)

    def test_bitcoin_init(self):
        self.assertIsInstance(Bitcoin("fake_key"), Bitcoin)

    def test_ethereum_init(self):
        self.assertIsInstance(Ethereum("fake_key"), Ethereum)

    def test_xrp_init(self):
        self.assertIsInstance(XRP("fake_key"), XRP)

    def test_erc20_init(self):
        self.assertIsInstance(Erc20("fake_key"), Erc20)

    def test_stablecoins_init(self):
        self.assertIsInstance(StableCoins("fake_key"), StableCoins)

    def test_trx_init(self):
        self.assertIsInstance(TRX("fake_key"), TRX)

    def test_altcoins_init(self):
        self.assertIsInstance(AltCoins("fake_key"), AltCoins)

    def test_discovery_init(self):
        self.assertIsInstance(Discovery("fake_key"), Discovery)


class BitcoinEndpointTests(TestCase):
    def setUp(self):
        patcher = patch(_PATCH_TARGET, return_value=_FAKE_RESPONSE)
        self.mock_hr = patcher.start()
        self.addCleanup(patcher.stop)
        self.btc = Bitcoin("fake_key")

    def test_get_btc_exch_entity(self):
        self.btc.get_btc_exch_entity()
        self.mock_hr.assert_called()

    def test_get_btc_exch_reserve(self):
        self.btc.get_btc_exch_reserve()

    def test_get_btc_exch_netflow(self):
        self.btc.get_btc_exch_netflow()

    def test_get_btc_exch_inflow(self):
        self.btc.get_btc_exch_inflow()

    def test_get_btc_exch_outflow(self):
        self.btc.get_btc_exch_outflow()

    def test_get_btc_exch_txn(self):
        self.btc.get_btc_exch_txn()

    def test_get_btc_exch_addrs(self):
        self.btc.get_btc_exch_addrs()

    def test_get_btc_exch_inhouseflow(self):
        self.btc.get_btc_exch_inhouseflow()

    def test_get_btc_idx_mpi(self):
        self.btc.get_btc_idx_mpi()

    def test_get_btc_idx_exchshutdown(self):
        self.btc.get_btc_idx_exchshutdown()

    def test_get_btc_idx_whale(self):
        self.btc.get_btc_idx_whale()

    def test_get_btc_idx_fundflow(self):
        self.btc.get_btc_idx_fundflow()

    def test_get_btc_idx_stableratio(self):
        self.btc.get_btc_idx_stableratio()

    def test_get_btc_idx_agedistr(self):
        self.btc.get_btc_idx_agedistr()

    def test_get_btc_idx_supplydstr(self):
        self.btc.get_btc_idx_supplydstr()

    def test_get_btc_idx_cdd(self):
        self.btc.get_btc_idx_cdd()

    def test_get_btc_idx_exchsupplyratio(self):
        self.btc.get_btc_idx_exchsupplyratio()

    def test_get_btc_idx_minersupplyratio(self):
        self.btc.get_btc_idx_minersupplyratio()

    def test_get_btc_mkt_leverage(self):
        self.btc.get_btc_mkt_leverage()

    def test_get_btc_mkt_ssr(self):
        self.btc.get_btc_mkt_ssr()

    def test_get_btc_mkt_mvrv(self):
        self.btc.get_btc_mkt_mvrv()

    def test_get_btc_mkt_sopr(self):
        self.btc.get_btc_mkt_sopr()

    def test_get_btc_mkt_soprratio(self):
        self.btc.get_btc_mkt_soprratio()

    def test_get_btc_mkt_realizedprice(self):
        self.btc.get_btc_mkt_realizedprice()

    def test_get_btc_mkt_utxo(self):
        self.btc.get_btc_mkt_utxo()

    def test_get_btc_ntw_stock2flow(self):
        self.btc.get_btc_ntw_stock2flow()

    def test_get_btc_ntw_nvt(self):
        self.btc.get_btc_ntw_nvt()

    def test_get_btc_ntw_nvtgoldencross(self):
        self.btc.get_btc_ntw_nvtgoldencross()

    def test_get_btc_ntw_nvm(self):
        self.btc.get_btc_ntw_nvm()

    def test_get_btc_ntw_puell(self):
        self.btc.get_btc_ntw_puell()

    def test_get_btc_ntw_cdd(self):
        self.btc.get_btc_ntw_cdd()

    def test_get_btc_ntw_mca(self):
        self.btc.get_btc_ntw_mca()

    def test_get_btc_ntw_sca(self):
        self.btc.get_btc_ntw_sca()

    def test_get_btc_ntw_scad(self):
        self.btc.get_btc_ntw_scad()

    def test_get_btc_ntw_nupl(self):
        self.btc.get_btc_ntw_nupl()

    def test_get_btc_ntw_nrpl(self):
        self.btc.get_btc_ntw_nrpl()

    def test_get_btc_ntw_pnlutxo(self):
        self.btc.get_btc_ntw_pnlutxo()

    def test_get_btc_ntw_pnlsupply(self):
        self.btc.get_btc_ntw_pnlsupply()

    def test_get_btc_ntw_dormancy(self):
        self.btc.get_btc_ntw_dormancy()

    def test_get_btc_ntw_utxo_age_distr(self):
        self.btc.get_btc_ntw_utxo_age_distr()

    def test_get_btc_ntw_utxo_realized_age_dstr(self):
        self.btc.get_btc_ntw_utxo_realized_age_dstr()

    def test_get_btc_ntw_utxo_count_age_dstr(self):
        self.btc.get_btc_ntw_utxo_count_age_dstr()

    def test_get_btc_ntw_spent_output_age_dstr(self):
        self.btc.get_btc_ntw_spent_output_age_dstr()

    def test_get_btc_ntw_utxo_supply_dstr(self):
        self.btc.get_btc_ntw_utxo_supply_dstr()

    def test_get_btc_ntw_utxo_realized_supply_dstr(self):
        self.btc.get_btc_ntw_utxo_realized_supply_dstr()

    def test_get_btc_ntw_utxo_count_supply_dstr(self):
        self.btc.get_btc_ntw_utxo_count_supply_dstr()

    def test_get_btc_ntw_spent_output_supply_dstr(self):
        self.btc.get_btc_ntw_spent_output_supply_dstr()

    def test_get_btc_miner_reserve(self):
        self.btc.get_btc_miner_reserve()

    def test_get_btc_miner_netflow(self):
        self.btc.get_btc_miner_netflow()

    def test_get_btc_miner_inflow(self):
        self.btc.get_btc_miner_inflow()

    def test_get_btc_miner_outflow(self):
        self.btc.get_btc_miner_outflow()

    def test_get_btc_miner_txn_count(self):
        self.btc.get_btc_miner_txn_count()

    def test_get_btc_miner_addr_count(self):
        self.btc.get_btc_miner_addr_count()

    def test_get_btc_miner_inhouse_flow(self):
        self.btc.get_btc_miner_inhouse_flow()

    def test_get_btc_inter_exch_2_exch(self):
        self.btc.get_btc_inter_exch_2_exch()

    def test_get_btc_inter_miner_2_exch(self):
        self.btc.get_btc_inter_miner_2_exch()

    def test_get_btc_inter_exch_2_miner(self):
        self.btc.get_btc_inter_exch_2_miner()

    def test_get_btc_inter_miner_2_miner(self):
        self.btc.get_btc_inter_miner_2_miner()

    def test_get_btc_fund_mkt_price(self):
        self.btc.get_btc_fund_mkt_price()

    def test_get_btc_fund_mkt_volume(self):
        self.btc.get_btc_fund_mkt_volume()

    def test_get_btc_fund_mkt_premium(self):
        self.btc.get_btc_fund_mkt_premium()

    def test_get_btc_fund_digital_assets_holdings(self):
        self.btc.get_btc_fund_digital_assets_holdings()

    def test_get_btc_liq_ohlcv(self):
        self.btc.get_btc_liq_ohlcv()

    def test_get_btc_liq_open_interest(self):
        self.btc.get_btc_liq_open_interest()

    def test_get_btc_liq_funding_rates(self):
        self.btc.get_btc_liq_funding_rates()

    def test_get_btc_liq_taker_stats(self):
        self.btc.get_btc_liq_taker_stats()

    def test_get_btc_liq_liquidations(self):
        self.btc.get_btc_liq_liquidations()

    def test_get_btc_liq_capitalization(self):
        self.btc.get_btc_liq_capitalization()

    def test_get_btc_liq_coinbase_idx(self):
        self.btc.get_btc_liq_coinbase_idx()

    def test_get_btc_miner_company_data(self):
        self.btc.get_btc_miner_company_data()

    def test_get_btc_net_supply(self):
        self.btc.get_btc_net_supply()

    def test_get_btc_net_velocity(self):
        self.btc.get_btc_net_velocity()

    def test_get_btc_net_trx_count(self):
        self.btc.get_btc_net_trx_count()

    def test_get_btc_net_addr_count(self):
        self.btc.get_btc_net_addr_count()

    def test_get_btc_net_tokens_transferred(self):
        self.btc.get_btc_net_tokens_transferred()

    def test_get_btc_net_block_bytes(self):
        self.btc.get_btc_net_block_bytes()

    def test_get_btc_net_block_count(self):
        self.btc.get_btc_net_block_count()

    def test_get_btc_net_block_interval(self):
        self.btc.get_btc_net_block_interval()

    def test_get_btc_net_utxo_count(self):
        self.btc.get_btc_net_utxo_count()

    def test_get_btc_net_fees(self):
        self.btc.get_btc_net_fees()

    def test_get_btc_net_fees_trx(self):
        self.btc.get_btc_net_fees_trx()

    def test_get_btc_net_blockreward(self):
        self.btc.get_btc_net_blockreward()

    def test_get_btc_net_difficulty(self):
        self.btc.get_btc_net_difficulty()

    def test_get_btc_net_hashrate(self):
        self.btc.get_btc_net_hashrate()

    def test_get_btc_mem_stats_by_relative_fee(self):
        self.btc.get_btc_mem_stats_by_relative_fee()

    def test_get_btc_mem_stats_in_total(self):
        self.btc.get_btc_mem_stats_in_total()

    def test_get_btc_light_stats(self):
        self.btc.get_btc_light_stats()


class EthereumEndpointTests(TestCase):
    def setUp(self):
        patcher = patch(_PATCH_TARGET, return_value=_FAKE_RESPONSE)
        self.mock_hr = patcher.start()
        self.addCleanup(patcher.stop)
        self.eth = Ethereum("fake_key")

    def test_get_eth_entity_list(self):
        self.eth.get_eth_entity_list()

    def test_get_eth_exch_reserve(self):
        self.eth.get_eth_exch_reserve()

    def test_get_eth_exch_netflow(self):
        self.eth.get_eth_exch_netflow()

    def test_get_eth_exch_inflow(self):
        self.eth.get_eth_exch_inflow()

    def test_get_eth_exch_outflow(self):
        self.eth.get_eth_exch_outflow()

    def test_get_eth_exch_trx_count(self):
        self.eth.get_eth_exch_trx_count()

    def test_get_eth_exch_addrs_count(self):
        self.eth.get_eth_exch_addrs_count()

    def test_get_eth_flow_exch_supply_ratio(self):
        self.eth.get_eth_flow_exch_supply_ratio()

    def test_get_eth_mkt_estimated_leverage_ratio(self):
        self.eth.get_eth_mkt_estimated_leverage_ratio()

    def test_get_eth_20_total_value_staked(self):
        self.eth.get_eth_20_total_value_staked()

    def test_get_eth_20_total_inflow_staking(self):
        self.eth.get_eth_20_total_inflow_staking()

    def test_get_eth_20_staking_trx_count(self):
        self.eth.get_eth_20_staking_trx_count()

    def test_get_eth_20_staking_validator_total(self):
        self.eth.get_eth_20_staking_validator_total()

    def test_get_eth_20_depositor_count_total(self):
        self.eth.get_eth_20_depositor_count_total()

    def test_get_eth_20_depositor_count_new(self):
        self.eth.get_eth_20_depositor_count_new()

    def test_get_eth_20_staking_rate(self):
        self.eth.get_eth_20_staking_rate()

    def test_get_eth_20_phase_0_success_rate(self):
        self.eth.get_eth_20_phase_0_success_rate()

    def test_get_eth_fund_market_price(self):
        self.eth.get_eth_fund_market_price()

    def test_get_eth_fund_market_volumen(self):
        self.eth.get_eth_fund_market_volumen()

    def test_get_eth_fund_market_premium(self):
        self.eth.get_eth_fund_market_premium()

    def test_get_eth_fund_digital_asset_holdings(self):
        self.eth.get_eth_fund_digital_asset_holdings()

    def test_get_eth_mkt_ohlcv(self):
        self.eth.get_eth_mkt_ohlcv()

    def test_get_eth_mkt_open_interest(self):
        self.eth.get_eth_mkt_open_interest()

    def test_get_eth_mkt_funding_rates(self):
        self.eth.get_eth_mkt_funding_rates()

    def test_get_eth_mkt_taker_buy_sell_stats(self):
        self.eth.get_eth_mkt_taker_buy_sell_stats()

    def test_get_eth_mkt_liquidations(self):
        self.eth.get_eth_mkt_liquidations()

    def test_get_eth_mkt_coinbase_premium_index(self):
        self.eth.get_eth_mkt_coinbase_premium_index()

    def test_get_eth_mkt_capitalization(self):
        self.eth.get_eth_mkt_capitalization()

    def test_get_eth_ntx_supply(self):
        self.eth.get_eth_ntx_supply()

    def test_get_eth_ntx_velocity(self):
        self.eth.get_eth_ntx_velocity()

    def test_get_eth_ntx_contracts_count(self):
        self.eth.get_eth_ntx_contracts_count()

    def test_get_eth_ntx_trx_count(self):
        self.eth.get_eth_ntx_trx_count()

    def test_get_eth_ntx_trx_eoa(self):
        self.eth.get_eth_ntx_trx_eoa()

    def test_get_eth_ntx_trx_contract_calls_external(self):
        self.eth.get_eth_ntx_trx_contract_calls_external()

    def test_get_eth_ntx_trx_contract_calls_internal(self):
        self.eth.get_eth_ntx_trx_contract_calls_internal()

    def test_get_eth_ntx_trx_contract_calls_count(self):
        self.eth.get_eth_ntx_trx_contract_calls_count()

    def test_get_eth_ntx_trx_count_all(self):
        self.eth.get_eth_ntx_trx_count_all()

    def test_get_eth_ntx_addr_count(self):
        self.eth.get_eth_ntx_addr_count()

    def test_get_eth_ntx_addr_count_all(self):
        self.eth.get_eth_ntx_addr_count_all()

    def test_get_eth_ntx_tokens_transferred_count(self):
        self.eth.get_eth_ntx_tokens_transferred_count()

    def test_get_eth_ntx_tokens_transferred_count_eoa(self):
        self.eth.get_eth_ntx_tokens_transferred_count_eoa()

    def test_get_eth_ntx_tokens_transferred_count_calls_external(self):
        self.eth.get_eth_ntx_tokens_transferred_count_calls_external()

    def test_get_eth_ntx_tokens_transferred_count_calls_internal(self):
        self.eth.get_eth_ntx_tokens_transferred_count_calls_internal()

    def test_get_eth_ntx_tokens_transferred_count_calls(self):
        self.eth.get_eth_ntx_tokens_transferred_count_calls()

    def test_get_eth_ntx_tokens_transferred_count_all(self):
        self.eth.get_eth_ntx_tokens_transferred_count_all()

    def test_get_eth_ntx_tokens_transferred(self):
        self.eth.get_eth_ntx_tokens_transferred()

    def test_get_eth_ntx_tokens_transferred_eoa(self):
        self.eth.get_eth_ntx_tokens_transferred_eoa()

    def test_get_eth_ntx_tokens_transferred_calls_external(self):
        self.eth.get_eth_ntx_tokens_transferred_calls_external()

    def test_get_eth_ntx_tokens_transferred_calls_internal(self):
        self.eth.get_eth_ntx_tokens_transferred_calls_internal()

    def test_get_eth_ntx_tokens_transferred_calls(self):
        self.eth.get_eth_ntx_tokens_transferred_calls()

    def test_get_eth_ntx_tokens_transferred_all(self):
        self.eth.get_eth_ntx_tokens_transferred_all()

    def test_get_eth_ntx_failed_trx_count(self):
        self.eth.get_eth_ntx_failed_trx_count()

    def test_get_eth_ntx_failed_tokens_transferred_count(self):
        self.eth.get_eth_ntx_failed_tokens_transferred_count()

    def test_get_eth_ntx_block_bytes(self):
        self.eth.get_eth_ntx_block_bytes()

    def test_get_eth_ntx_block_count(self):
        self.eth.get_eth_ntx_block_count()

    def test_get_eth_ntx_block_interval(self):
        self.eth.get_eth_ntx_block_interval()

    def test_get_eth_ntx_fees(self):
        self.eth.get_eth_ntx_fees()

    def test_get_eth_ntx_fees_burnt(self):
        self.eth.get_eth_ntx_fees_burnt()

    def test_get_eth_ntx_fees_tips(self):
        self.eth.get_eth_ntx_fees_tips()

    def test_get_eth_ntx_fees_trx(self):
        self.eth.get_eth_ntx_fees_trx()

    def test_get_eth_ntx_fees_trx_burnt(self):
        self.eth.get_eth_ntx_fees_trx_burnt()

    def test_get_eth_ntx_fees_trx_tips(self):
        self.eth.get_eth_ntx_fees_trx_tips()

    def test_get_eth_ntx_blockreward(self):
        self.eth.get_eth_ntx_blockreward()

    def test_get_eth_ntx_blockreward_except_uncle(self):
        self.eth.get_eth_ntx_blockreward_except_uncle()

    def test_get_eth_ntx_gas(self):
        self.eth.get_eth_ntx_gas()

    def test_get_eth_ntx_base_fee(self):
        self.eth.get_eth_ntx_base_fee()

    def test_get_eth_ntx_max_fee(self):
        self.eth.get_eth_ntx_max_fee()

    def test_get_eth_ntx_max_priority_fee(self):
        self.eth.get_eth_ntx_max_priority_fee()

    def test_get_eth_ntx_difficulty(self):
        self.eth.get_eth_ntx_difficulty()

    def test_get_eth_ntx_hashrate(self):
        self.eth.get_eth_ntx_hashrate()

    def test_get_eth_ntx_uncle_block_count(self):
        self.eth.get_eth_ntx_uncle_block_count()

    def test_get_eth_ntx_uncle_blockreward(self):
        self.eth.get_eth_ntx_uncle_blockreward()


class XRPEndpointTests(TestCase):
    def setUp(self):
        patcher = patch(_PATCH_TARGET, return_value=_FAKE_RESPONSE)
        self.mock_hr = patcher.start()
        self.addCleanup(patcher.stop)
        self.xrp = XRP("fake_key")

    def test_get_xrp_entity_list(self):
        self.xrp.get_xrp_entity_list()

    def test_get_xrp_entity_reserve(self):
        self.xrp.get_xrp_entity_reserve()

    def test_get_xrp_entity_share(self):
        self.xrp.get_xrp_entity_share()

    def test_get_xrp_entity_trx_count(self):
        self.xrp.get_xrp_entity_trx_count()

    def test_get_xrp_entity_inflow(self):
        self.xrp.get_xrp_entity_inflow()

    def test_get_xrp_entity_outflow(self):
        self.xrp.get_xrp_entity_outflow()

    def test_get_xrp_entity_addrs_count(self):
        self.xrp.get_xrp_entity_addrs_count()

    def test_get_xrp_entity_whale_movements(self):
        self.xrp.get_xrp_entity_whale_movements()

    def test_get_xrp_flow_exch_inflow_value_dstr(self):
        self.xrp.get_xrp_flow_exch_inflow_value_dstr()

    def test_get_xrp_flow_exch_outflow_value_dstr(self):
        self.xrp.get_xrp_flow_exch_outflow_value_dstr()

    def test_get_xrp_flow_exch_inflow_count_value_dstr(self):
        self.xrp.get_xrp_flow_exch_inflow_count_value_dstr()

    def test_get_xrp_flow_exch_outflow_count_value_dstr(self):
        self.xrp.get_xrp_flow_exch_outflow_count_value_dstr()

    def test_get_xrp_flow_exch_supply_ratio(self):
        self.xrp.get_xrp_flow_exch_supply_ratio()

    def test_get_xrp_mkt_ohlcv(self):
        self.xrp.get_xrp_mkt_ohlcv()

    def test_get_xrp_mkt_open_interest(self):
        self.xrp.get_xrp_mkt_open_interest()

    def test_get_xrp_mkt_funding_rates(self):
        self.xrp.get_xrp_mkt_funding_rates()

    def test_get_xrp_mkt_taker_buysell_stats(self):
        self.xrp.get_xrp_mkt_taker_buysell_stats()

    def test_get_xrp_mkt_liquidations(self):
        self.xrp.get_xrp_mkt_liquidations()

    def test_get_xrp_mkt_capitalization(self):
        self.xrp.get_xrp_mkt_capitalization()

    def test_get_xrp_mkt_estimated_leverage_ratio(self):
        self.xrp.get_xrp_mkt_estimated_leverage_ratio()

    def test_get_xrp_ntx_addrs_count(self):
        self.xrp.get_xrp_ntx_addrs_count()

    def test_get_xrp_ntx_velocity(self):
        self.xrp.get_xrp_ntx_velocity()

    def test_get_xrp_ntx_block_interval(self):
        self.xrp.get_xrp_ntx_block_interval()

    def test_get_xrp_ntx_burnt(self):
        self.xrp.get_xrp_ntx_burnt()

    def test_get_xrp_ntx_ledger_count(self):
        self.xrp.get_xrp_ntx_ledger_count()

    def test_get_xrp_ntx_fees(self):
        self.xrp.get_xrp_ntx_fees()

    def test_get_xrp_ntx_trx_count(self):
        self.xrp.get_xrp_ntx_trx_count()

    def test_get_xrp_ntx_tokens_transferred(self):
        self.xrp.get_xrp_ntx_tokens_transferred()

    def test_get_xrp_ntx_supply(self):
        self.xrp.get_xrp_ntx_supply()

    def test_get_xrp_ntx_value_to_trx(self):
        self.xrp.get_xrp_ntx_value_to_trx()

    def test_get_xrp_dex_volume(self):
        self.xrp.get_xrp_dex_volume()

    def test_get_xrp_dex_trx_count(self):
        self.xrp.get_xrp_dex_trx_count()

    def test_get_xrp_dex_liquidity(self):
        self.xrp.get_xrp_dex_liquidity()

    def test_get_xrp_dex_price(self):
        self.xrp.get_xrp_dex_price()

    def test_get_xrp_amm_price(self):
        self.xrp.get_xrp_amm_price()

    def test_get_xrp_amm_liquidity(self):
        self.xrp.get_xrp_amm_liquidity()

    def test_get_xrp_amm_fee(self):
        self.xrp.get_xrp_amm_fee()

    def test_get_xrp_amm_swaps(self):
        self.xrp.get_xrp_amm_swaps()


class Erc20EndpointTests(TestCase):
    def setUp(self):
        patcher = patch(_PATCH_TARGET, return_value=_FAKE_RESPONSE)
        self.mock_hr = patcher.start()
        self.addCleanup(patcher.stop)
        self.erc20 = Erc20("fake_key")

    def test_get_erc20_entity_list(self):
        self.erc20.get_erc20_entity_list()

    def test_get_erc20_exch_reserve(self):
        self.erc20.get_erc20_exch_reserve()

    def test_get_erc20_exch_netflow(self):
        self.erc20.get_erc20_exch_netflow()

    def test_get_erc20_exch_inflow(self):
        self.erc20.get_erc20_exch_inflow()

    def test_get_erc20_exch_outflow(self):
        self.erc20.get_erc20_exch_outflow()

    def test_get_erc20_exch_trx_count(self):
        self.erc20.get_erc20_exch_trx_count()

    def test_get_erc20_exch_addrs_count(self):
        self.erc20.get_erc20_exch_addrs_count()

    def test_get_erc20_exch_supply_ratio(self):
        self.erc20.get_erc20_exch_supply_ratio()

    def test_get_erc20_mkt_ohlcv(self):
        self.erc20.get_erc20_mkt_ohlcv()

    def test_get_erc20_ntx_supply(self):
        self.erc20.get_erc20_ntx_supply()

    def test_get_erc20_ntx_velocity(self):
        self.erc20.get_erc20_ntx_velocity()

    def test_get_erc20_ntx_trx_count(self):
        self.erc20.get_erc20_ntx_trx_count()

    def test_get_erc20_ntx_tokens_transferred_count(self):
        self.erc20.get_erc20_ntx_tokens_transferred_count()

    def test_get_erc20_ntx_tokens_transferred(self):
        self.erc20.get_erc20_ntx_tokens_transferred()

    def test_get_erc20_ntx_addrs_count(self):
        self.erc20.get_erc20_ntx_addrs_count()


class StableCoinsEndpointTests(TestCase):
    def setUp(self):
        patcher = patch(_PATCH_TARGET, return_value=_FAKE_RESPONSE)
        self.mock_hr = patcher.start()
        self.addCleanup(patcher.stop)
        self.sc = StableCoins("fake_key")

    def test_get_stable_entity_list(self):
        self.sc.get_stable_entity_list()

    def test_get_stable_exch_reserve(self):
        self.sc.get_stable_exch_reserve()

    def test_get_stable_exch_netflow(self):
        self.sc.get_stable_exch_netflow()

    def test_get_stable_exch_inflow(self):
        self.sc.get_stable_exch_inflow()

    def test_get_stable_exch_outflow(self):
        self.sc.get_stable_exch_outflow()

    def test_get_stable_exch_trx_count(self):
        self.sc.get_stable_exch_trx_count()

    def test_get_stable_exch_addrs_count(self):
        self.sc.get_stable_exch_addrs_count()

    def test_get_stable_flow_exch_supply_ratio(self):
        self.sc.get_stable_flow_exch_supply_ratio()

    def test_get_stable_mkt_ohlcv(self):
        self.sc.get_stable_mkt_ohlcv()

    def test_get_stable_mkt_capitalization(self):
        self.sc.get_stable_mkt_capitalization()

    def test_get_stable_ntx_supply(self):
        self.sc.get_stable_ntx_supply()

    def test_get_stable_ntx_events_count(self):
        self.sc.get_stable_ntx_events_count()

    def test_get_stable_trx_tokens_transferred(self):
        self.sc.get_stable_trx_tokens_transferred()

    def test_get_stable_trx_addrs_count(self):
        self.sc.get_stable_trx_addrs_count()


class TRXEndpointTests(TestCase):
    def setUp(self):
        patcher = patch(_PATCH_TARGET, return_value=_FAKE_RESPONSE)
        self.mock_hr = patcher.start()
        self.addCleanup(patcher.stop)
        self.trx = TRX("fake_key")

    def test_get_trx_mkt_ohlcv(self):
        self.trx.get_trx_mkt_ohlcv()

    def test_get_trx_mkt_capitalization(self):
        self.trx.get_trx_mkt_capitalization()

    def test_get_trx_ntx_supply(self):
        self.trx.get_trx_ntx_supply()

    def test_get_trx_ntx_trx_count(self):
        self.trx.get_trx_ntx_trx_count()

    def test_get_trx_ntx_addrs_count(self):
        self.trx.get_trx_ntx_addrs_count()

    def test_get_trx_ntx_tokens_transferred(self):
        self.trx.get_trx_ntx_tokens_transferred()

    def test_get_trx_ntx_block_count(self):
        self.trx.get_trx_ntx_block_count()

    def test_get_trx_ntx_fees(self):
        self.trx.get_trx_ntx_fees()

    def test_get_trx_ntx_tps(self):
        self.trx.get_trx_ntx_tps()

    def test_get_trx_ntx_total_value_staked(self):
        self.trx.get_trx_ntx_total_value_staked()

    def test_get_trx_ntx_enery_stake(self):
        self.trx.get_trx_ntx_enery_stake()

    def test_get_trx_defi_sunpump_tokens(self):
        self.trx.get_trx_defi_sunpump_tokens()

    def test_get_trx_defi_sunswap_activity(self):
        self.trx.get_trx_defi_sunswap_activity()


class AltCoinsEndpointTests(TestCase):
    def setUp(self):
        patcher = patch(_PATCH_TARGET, return_value=_FAKE_RESPONSE)
        self.mock_hr = patcher.start()
        self.addCleanup(patcher.stop)
        self.alts = AltCoins("fake_key")

    def test_get_alts_mkt_ohlcv(self):
        self.alts.get_alts_mkt_ohlcv()
        self.mock_hr.assert_called()


class DiscoveryEndpointTests(TestCase):
    def setUp(self):
        patcher = patch(_PATCH_TARGET, return_value=_FAKE_RESPONSE)
        self.mock_hr = patcher.start()
        self.addCleanup(patcher.stop)
        self.disc = Discovery("fake_key")

    def test_get_endpoints(self):
        self.disc.get_endpoints()
        self.mock_hr.assert_called()
