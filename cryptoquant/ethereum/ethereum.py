# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 10:30:02 2025

@author: lauta
"""

from cryptoquant.request_handler_class import RequestHandler

class Ethereum(RequestHandler):
    def __init__(self, api_key: str):
        
        #Entity List
        self.ENTITY_STATUS = "eth/status/entity-list"
        # ETH Exchange Flows
        self.EXCH_FLOWS_RESERVE = "eth/exchange-flows/reserve"
        self.EXCH_FLOWS_NETFLOW = "eth/exchange-flows/netflow"
        self.EXCH_FLOWS_INFLOW = "eth/exchange-flows/inflow"
        self.EXCH_FLOWS_OUTFLOW = "eth/exchange-flows/outflow"
        self.EXCH_FLOWS_TRANSACTIONS_COUNT = "eth/exchange-flows/transactions-count"
        self.EXCH_FLOWS_ADDRESES_COUNT = "eth/exchange-flows/addresses-count"
        # Exchange Supply Ratio
        self.FLOW_IDX_EXCHNAGE_SUPPLY_RATIO = "eth/flow-indicator/exchange-supply-ratio"
        # ETH Market Indicator
        self.MARKET_IDX_ESTIMATED_LEVERAGE_RATIO = "eth/market-indicator/estimated-leverage-ratio"
        # ETH 2.0
        self.ETH_2_TOTAL_VALUE_STAKED = "eth/eth2/total-value-staked"
        self.ETH_2_STAKING_INFLOW_TOTAL = "eth/eth2/staking-inflow-total"
        self.ETH_2_STAKING_TRX_COUNT = "eth/eth2/staking-transaction-count"
        self.ETH_2_STAKING_VALIDATOR_TOTAL = "eth/eth2/staking-validator-total"
        self.ETH_2_DEPOSITOR_COUNT_TOTAL = "eth/eth2/depositor-count-total"
        self.ETH_2_DEPOSITOR_COUNT_NEW = "eth/eth2/depositor-count-new"
        self.ETH_2_STAKING_RATE = "eth/eth2/staking-rate"
        self.ETH_2_PHASE_0_SUCCESS_RATE = "eth/eth2/phase0-success-rate"
        # ETH Fund Data
        self.FUND_MARKET_PRICE = "eth/fund-data/market-price-usd"
        self.FUND_MARKET_VOLUME = "eth/fund-data/market-volume"
        self.FUND_MARKET_PREMIUM = "eth/fund-data/market-premium"
        self.FUND_MARKET_DIGITAL_HOLDINGS = "eth/fund-data/digital-asset-holdings"
        # Market Data
        self.MARKET_PRICE_OHLCV = "eth/market-data/price-ohlcv"
        self.MARKET_OPEN_INTEREST = "eth/market-data/open-interest"
        self.MARKET_FUNDING_RATES = "eth/market-data/funding-rates"
        self.MARKET_TAKER_BUY_SELL_STATS = "eth/market-data/taker-buy-sell-stats"
        self.MARKET_LIQUIDATIONS = "eth/market-data/liquidations"
        self.MARKET_COINBASE_PREMIUM_INDEX = "eth/market-data/coinbase-premium-index"
        self.MARKET_CAPITALIZATION = "eth/market-data/capitalization"
        # ETH Network Data
        self.NETWORK_SUPPLY = "eth/network-data/supply"
        self.NETWORK_VELOCITY = "eth/network-data/velocity"
        self.NETWORK_CONTRACTS_COUNT = "eth/network-data/contracts-count"
        
        super().__init__(api_key)
        
    # -------------------------------
    # Entity list
    # -------------------------------
    
    def get_eth_entity_list(self, **query_params):
        """
        This endpoint returns entity list to serve data. The meaning of the 
        market_type value of the exchange object is as follows. For exchange 
        objects, the market_type field tells whether the exchange is a spot 
        exchange or a derivative exchange. Entities without a market type, 
        such as miners or banks, will return 0 for market_type.

        Exchange Market Type	Description
                            0	Undefined
                            1	Spot Exchange
                            2	Derivative Exchange

        Parameters
        ----------
        **query_params :
            type_ (str, required): A type from the entity in exchange.
            format_ (str:optional): A format type about return message type. 
                            Supported formats are json, csv. Default is json

        Returns
        -------
        dict
            Entity list on a given type.

        """
        return super().handle_request(self.ENTITY_STATUS, query_params)
    
    # -------------------------------
    # ETH Exchange Flows
    # -------------------------------
    
    def get_eth_exch_reserve(self, **query_params):
        """
        Returns the full historical on-chain balance of Ethereum exchanges.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            The amount of eth on a given exchange on this window.

        """
        return super().handle_request(self.EXCH_FLOWS_RESERVE, query_params)
    
    def get_eth_exch_netflow(self, **query_params):
        """
        The difference between coins flowing into exchanges and flowing out of
        exchanges. Netflow usually helps us to figure out an increase of idle
        coins waiting to be traded in a certain time frame.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            total netflow.

        """
        return super().handle_request(self.EXCH_FLOWS_NETFLOW, query_params)
    
    def get_eth_exch_inflow(self, **query_params):
        """
        This endpoint returns the inflow of ETH into exchange wallets for as 
        far back as CQ track. The average inflow is the average transaction 
        value for transactions flowing into exchange wallets on a given day.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            inflow statistics.

        """
        return super().handle_request(self.EXCH_FLOWS_INFLOW, query_params)
    
    def get_eth_exch_outflow(self, **query_params):
        """
        This endpoint returns the outflow of ETH into exchange wallets for as
        far back as CQ track. The average outflow is the average transaction 
        value for transactions flowing into exchange wallets on a given day.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            Outflow statistics.

        """
        return super().handle_request(self.EXCH_FLOWS_OUTFLOW, query_params)
    
    def get_eth_exch_trx_count(self, **query_params):
        """
        This endpoint returns the number of transactions flowing in/out of 
        Ethereum exchanges.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            Transactions count of inflows and outflows of ethereum exchnages.

        """
        return super().handle_request(self.EXCH_FLOWS_TRANSACTIONS_COUNT, query_params)
    
    def get_eth_exch_addrs_count(self, **query_params):
        """
        This endpoint returns the number of addresses involved in 
        inflow/outflow transactions.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            The number of addresses evoking inflow/outflow transactions to 
            exchange wallets.

        """
        return super().handle_request(self.EXCH_FLOWS_ADDRESES_COUNT, query_params)
    
    # -------------------------------
    # Exchange Supply Ratio
    # -------------------------------
    
    def get_eth_flow_exch_supply_ratio(self, **query_params):
        """
        Exchange Supply Ratio is calculated as exchange reserve divided by 
        total supply. The metric measures how much tokens are reserved in the 
        exchange relative to total supply of the token.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            Ratio of reserved token in the exchange relative to total supply.

        """
        return super().handle_request(self.FLOW_IDX_EXCHNAGE_SUPPLY_RATIO, query_params)
    
    # -------------------------------
    # ETH Market Indicator
    # -------------------------------
    
    def get_eth_mkt_estimated_leverage_ratio(self, **query_params):
        """
        By dividing the open interest of an exchange by their ETH reserve, you 
        can estimate a relative average user leverage. Whenever the leverage 
        value reaches a high, there is rapid volatility. Similar to Open 
        Interest, but more accurate because it reflects the growth of the 
        exchange itself. This is experimental indicator but it seems this 
        reflects market sentiment. You can see how aggressive people are and
        how conservative they are in terms of investment. For 'In Progress'
        exchanges, estimated leverage ratio is not supported yet even though 
        they provide open interest.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            The amount of open interest of exchnge divided by their 
            ETH reserve.

        """
        return super().handle_request(self.MARKET_IDX_ESTIMATED_LEVERAGE_RATIO, query_params)
    
    # -------------------------------
    # ETH 2.0
    # -------------------------------
    
    def get_eth_20_total_value_staked(self, **query_params):
        """
        This endpoint returns the valid ETH balance of the deposit contract.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            The valid amount of ETH in the deposit contract on this window.

        """
        return super().handle_request(self.ETH_2_TOTAL_VALUE_STAKED, query_params)
    
    def get_eth_20_total_inflow_staking(self, **query_params):
        """
        This endpoint returns the valid ETH inflow into the deposit contract.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            The valid amount of ETH in the deposit contract on this window.

        """
        return super().handle_request(self.ETH_2_STAKING_INFLOW_TOTAL, query_params)
    
    def get_eth_20_staking_trx_count(self, **query_params):
        """
        This endpoint returns the number of valid transactions to the deposit
        contract.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            The valid amount of ETH in the deposit contract on this window.

        """
        return super().handle_request(self.ETH_2_STAKING_TRX_COUNT, query_params)
    
    def get_eth_20_staking_validator_total(self, **query_params):
        """
        This endpoint returns the number of total validators.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            The number of the number of total validators on this window.

        """
        return super().handle_request(self.ETH_2_STAKING_VALIDATOR_TOTAL, query_params)
    
    def get_eth_20_depositor_count_total(self, **query_params):
        """
        This endpoint returns the number of unique accounts who deposited over 
        32 ETH to the deposit contract.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            The number of unique accounts who deposited iver 32 ETH on this 
            window.

        """
        return super().handle_request(self.ETH_2_DEPOSITOR_COUNT_TOTAL, query_params)
    
    def get_eth_20_depositor_count_new(self, **query_params):
        """
        This endpoint returns the number of new unique accounts who deposited 
        over 32 ETH to the deposit contract.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv


        Returns
        -------
        dict
            This endpoint returns the number of new unique accounts who
            deposited over 32 ETH to the deposit contract.

        """
        return super().handle_request(self.ETH_2_DEPOSITOR_COUNT_NEW, query_params)
    
    def get_eth_20_staking_rate(self, **query_params):
        """
        This endpoint returns the percentage of the balance of the ETH 2.0 
        deposit contract to the total supply.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            The percentage of valid balance of the deposit contract to the
            total supply on this window.

        """
        return super().handle_request(self.ETH_2_STAKING_RATE, query_params)
    
    def get_eth_20_phase_0_success_rate(self, **query_params):
        """
        This endpoint returns the percentage of the valid ETH balance of the
        deposit contract to 524,288 ETH.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            The percentage of valid balance of the deposit contract to
            524,288 ETH on thi window.

        """
        return super().handle_request(self.ETH_2_PHASE_0_SUCCESS_RATE, query_params)
    
    # -------------------------------
    # ETH Fund Data
    # -------------------------------
    
    def get_eth_fund_market_price(self, **query_params):
        """
        The price of certain symbol (e.g. ethe) managed by each fund (e.g. 
        Grayscale) reflects sentiment of investors in regulated markets. In
        this specific case, having single share of ETHE means having 
        approximately 0.01 ETH invested to Grayscale. This endpoint returns
        metrics related to the US Dollar(USD) price of fund related stocks 
        (e.g. ethe). CQ provide five metrics, price_usd_open, USD opening price
        at the beginning of the window, price_usd_close, USD closing price at 
        the end of the window, price_usd_high, the highest USD price in a given
        window, price_usd_low, the lowest USD price in a given window, and 
        price_usd_adj_close, USD adjusted closing price at the end of the
        window. All Symbol is not supported.
        
        full symbol list: https://cryptoquant.com/docs#tag/ETH-Fund-Data

        Parameters
        ----------
        **query_params : TYPE
            symbol (str, required): A stock symbol (ticker) from the table that
                                    CQ support
            window (str, optional): day.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            Market price OHLC and adjusted C data in USD.

        """
        return super().handle_request(self.FUND_MARKET_PRICE, query_params)
    
    def get_eth_fund_market_volumen(self, **query_params):
        """
        The volume of certain symbol (e.g. ethe) managed by each fund
        (e.g. Grayscale) reflects sentiment of investors in regulated markets. 
        This endpoint returns traded volume of fund related stocks (e.g. ethe).
        At this endpoint, metrics are calculated by Day. CQ provide one metric,
        volume, traded volume of the window.

        full symbol list: https://cryptoquant.com/docs#tag/ETH-Fund-Data

        Parameters
        ----------
        **query_params : TYPE
            symbol (str, required): A stock symbol (ticker) from the table that
                                    CQ support
            window (str, optional): day.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            Market volume data.

        """
        return super().handle_request(self.FUND_MARKET_VOLUME, query_params)
    
    def get_eth_fund_market_premium(self, **query_params):
        """
        The premium of certain symbol (e.g. ethe) is defined as (market price 
        of the symbol - NAV) divided by NAV where NAV (Native Asset Value) is 
        the current value of holdings (e.g. ETH price multiplied by ETH per 
        Share). Higher the premium indicates market bullish, which also
        indicates downside risk. On the other hand, lower the premium indicates 
        market bearish, which also indicates upside risk. All Symbol market 
        premium is calculated by taking VWAP (Volume Weighted Average Ratio) of
        each fund data volume (usd).

        full symbol list: https://cryptoquant.com/docs#tag/ETH-Fund-Data

        Parameters
        ----------
        **query_params : TYPE
            symbol (str, required): A stock symbol (ticker) from the table that
                                    CQ support
            window (str, optional): day.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        dict
            Market premium data.

        """
        return super().handle_request(self.FUND_MARKET_PREMIUM, query_params)
    
    def get_eth_fund_digital_asset_holdings(self, **query_params):
        """
        This endpoint returns digital asset holdings status of each fund. For 
        example, Grayscale ETH Holdings along with ETHE represents how much ETH
        Grayscale is holding for its investment. This metric indicates stock 
        market's sentiment where higher the value means bullish sentiment of 
        investors in stock market.

        full symbol list: https://cryptoquant.com/docs#tag/ETH-Fund-Data

        Parameters
        ----------
        **query_params : TYPE
            symbol (str, required): A stock symbol (ticker) from the table that
                                    CQ support
            window (str, optional): day.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv
        Returns
        -------
        dict
            Digital asset holdings data.

        """
        return super().handle_request(self.FUND_MARKET_DIGITAL_HOLDINGS, query_params)
    
    # -------------------------------
    # ETH Market Data
    # -------------------------------
    
    def get_eth_mkt_ohlcv(self, **query_params):
        """
        This endpoint returns metrics related to ETH price. We provide two 
        types of price, CryptoQuant's ETH Index Price and USD or USDT price of 
        ETH of global exchanges. Price OHLCV data consists of five metrics.  
        open, the opening price at the beginning of the window, close, USD 
        closing price at the end of the window,  high, the highest USD price in
        a given window, low, the lowest USD price in a given window, and volume,
        the total volume traded in a given window.
        
        At this endpoint, metrics are calculated by Minute, Hour and Day. ETH 
        Index Price is calculated by taking VWAP(Volume Weighted Average Price)
        of ETH price data aggregated from all exchanges CQ provide.
        
        full documentation: https://cryptoquant.com/docs#tag/ETH-Market-Data/operation/getETHPriceOHLCV

        Parameters
        ----------
        **query_params : TYPE
            market (str, optinal): A market type from the table CQ support
            exchange (str, optional): A exchnage from the table CQ support
            symbol (str, required): A stock symbol (ticker) from the table that
                                    CQ support
            window (str, optional): day, hour and minute.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            Price OHLCV data.

        """
        return super().handle_request(self.MARKET_PRICE_OHLCV, query_params)
    
    def get_eth_mkt_open_interest(self, **query_params):
        """
        This endpoint returns ETH Perpetual Open Interest from derivative
        exchanges. Supported exchanges for Open Interest are below. Note CQ
        unify the unit of return value to USD for each exchange where its
        contract specification may vary.
        
        full documentation: https://cryptoquant.com/docs#tag/ETH-Market-Data/operation/ETHgetOpenInterest

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, optional): A exchnage from the table CQ support
            symbol (str, required): A stock symbol (ticker) from the table that
                                    CQ support
            window (str, optional): day, hour and minute.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            Open interest in USD.

        """
        return super().handle_request(self.MARKET_OPEN_INTEREST, query_params)
    
    def get_eth_mkt_fundind_rates(self, **query_params):
        """
        Funding rates represents traders' sentiments of which position they bet
        on in perpetual swaps market. Positive funding rates implies that many
        traders are bullish and long traders pay funding to short traders. 
        Negative funding rates implies many traders are bearish and short 
        traders pay funding to long traders.
        
        full documentation: https://cryptoquant.com/docs#tag/ETH-Market-Data/operation/ETHgetFundingRates

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, optional): A exchnage from the table CQ support
            symbol (str, required): A stock symbol (ticker) from the table that
                                    CQ support
            window (str, optional): day, hour and minute.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            funding rates in percentage.

        """
        return super().handle_request(self.MARKET_FUNDING_RATES, query_params)
    
    def get_eth_mkt_taker_buy_sell_stats(self, **query_params):
        """
        Taker Buy/Sell Stats represent takers' sentiment of which position they
        are taking in the market. This metric is calculated with perpetual swap
        trades in each exchange. taker_buy_volume is volume that takers buy. 
        taker_sell_volume is volume that takers sell. taker_total_volume is the
        sum of taker_buy_volume and taker_sell_volume. taker_buy_ratio is the 
        ratio of taker_buy_volume divided by taker_total_volume. 
        taker_sell_ratio is the ratio of taker_sell_volume divided by 
        taker_total_volume. taker_buy_sell_ratio is the ratio of 
        taker_buy_volume divided by taker_sell_volume. Note CQ unify the unit 
        of return value to USD for each exchange where its contract 
        specification may vary.
        
        full documentation: https://cryptoquant.com/docs#tag/ETH-Market-Data/operation/ETHgetTakerBuySellStats

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, optional): A exchnage from the table CQ support
            symbol (str, required): A stock symbol (ticker) from the table that
                                    CQ support
            window (str, optional): day, hour and minute.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            Taker buy, sell volume and ratio.

        """
        return super().handle_request(self.MARKET_TAKER_BUY_SELL_STATS, query_params)
    
    def get_eth_mkt_liquidations(self, **query_params):
        """
        Liquidations are sum of forced market orders to exit leveraged 
        positions caused by price volatility. Liquidations indicate current 
        price volatility and traders' sentiment which side they had been 
        betting. Note that Binance's liquidation data collection policy has 
        changed since 2021-04-27, which makes the distribution of the data has 
        changed after that.
        
        full documentatio: https://cryptoquant.com/docs#tag/ETH-Market-Data/operation/ETHgetLiquidations

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, optional): A exchnage from the table CQ support
            symbol (str, required): A stock symbol (ticker) from the table that
                                    CQ support
            window (str, optional): day, hour and minute.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            Amount of long/short liquidations orders.

        """
        return super().handle_request(self.MARKET_LIQUIDATIONS, query_params)
    
    def get_eth_mkt_coinbase_premium_index(self, **query_params):
        """
        Coinbase Premium Index is calculated as percent difference from Binance
        price(ETHUSDT) to Coinbase price(ETHUSD). Coinbase Premium Gap is 
        calculated as gap between Coinbase price(ETHUSD) and Binance 
        price(ETHUSDT). The higher the premium, the stronger the spot buying 
        pressure from Coinbase.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day, hour and minute.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            Coinbase premium index in percentage and coinbase premium gap.

        """
        return super().handle_request(self.MARKET_COINBASE_PREMIUM_INDEX, query_params)
    
    def get_eth_mkt_capitalization(self, **query_params):
        """
        This endpoint returns metrics related to market capitalization. CQ
        provide market_cap, which is total market capitalization of ETH, 
        calculated by multiplying the circulating supply with its USD price.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day, hour and minute.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            Market capitalization of Ethereum calculated by total supply
            times price usd close.

        """
        return super().handle_request(self.MARKET_CAPITALIZATION, query_params)
    
    # -------------------------------
    # ETH Network Data
    # -------------------------------
    
    def get_eth_ntx_supply(self, **query_params):
        """
        This endpoint returns metrics related to Ethereum supply, i.e. the 
        amount of Ethereum in existence. CQ currently provide two metrics, 
        supply_total, the total amount of Ethereum in existence (sum of all 
       Ethereum issued by the block rewards), and supply_new, the amount of 
        newly issued tokens in a given window.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day, hour, 10minute, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            Total and new supply.

        """
        return super().handle_request(self.NETWORK_SUPPLY, query_params)
    
    def get_eth_ntx_velocity(self, **query_params):
        """
        This endpoint returns metrics related to the velocity of Ethereum. 
        Ethereum's velocity is calculated by dividing the trailing 1 year 
        estimated transaction volume(the cumulated sum of transferred tokens) 
        by current supply. Velocity is a metric that explains how actively is 
        money circulating in the market.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day, hour, 10minute, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            Ethereum transaction volume in the trailing 1 year divided by
            current total supply.

        """
        return super().handle_request(self.NETWORK_VELOCITY, query_params)
    
    def get_eth_ntx_contracts_count(self, **query_params):
        """
        This endpoint returns metrics related to the number of contracts. CQ
        provide contracts_created_new representing the number of contracts 
        created, contracts_destroyed_new representing the number of contracts 
        destroyed, and contracts_count_total representing the unique number of
        contracts.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day, hour, 10minute, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            new, destrpyed and total contracts on the ethereum netwok.

        """
        return super().handle_request(self.NETWORK_CONTRACTS_COUNT, query_params)