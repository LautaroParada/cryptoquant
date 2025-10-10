# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 14:19:40 2025

@author: lauta
"""

from cryptoquant.request_handler_class import RequestHandler

class Bitcoin(RequestHandler):
    def __init__(self, api_key: str):
        
        # URLS for exchanges
        self.EXCH_ENTITY_URL = "btc/status/entity-list"
        self.EXCH_RESERVES = "btc/exchange-flows/reserve"
        self.EXCH_NETFLOW = "btc/exchange-flows/netflow"
        self.EXCH_INFLOW = "btc/exchange-flows/inflow"
        self.EXCH_OUTFLOW = "btc/exchange-flows/outflow"
        self.EXCH_TNX_COUNT = "btc/exchange-flows/transactions-count"
        self.EXCH_ADDRESSES_COUNT = "btc/exchange-flows/addresses-count"
        self.EXCH_INHOUSE_FLOW = "btc/exchange-flows/in-house-flow"
        # Bitcoin Flow Indicators
        self.IDX_MPI = "btc/flow-indicator/mpi"
        self.IDX_EXCHANGE_SHUTDOWN = "btc/flow-indicator/exchange-shutdown-index"
        self.IDX_EXCHANGE_WHALE_RATIO = "btc/flow-indicator/exchange-whale-ratio"
        self.IDX_FUND_FLOW_RAIO = "btc/flow-indicator/fund-flow-ratio"
        self.IDX_STABLECOINS_RATIO = "btc/flow-indicator/stablecoins-ratio"
        self.IDX_EXCHANGE_INFLOW_AGE_DSTR = "btc/flow-indicator/exchange-inflow-age-distribution"
        self.IDX_EXCHANGE_INFLOW_SUPPLY_DSTR = "btc/flow-indicator/exchange-inflow-supply-distribution"
        self.IDX_EXCHANGE_INFLOW_CDD = "btc/flow-indicator/exchange-inflow-cdd"
        self.IDX_EXCHANGE_SUPPLY_RATIO = "btc/flow-indicator/exchange-supply-ratio"
        self.IDX_MINER_SUPPLY_RATIO = "btc/flow-indicator/miner-supply-ratio"
        # Bitcoin market indicators
        self.MKT_ESTIMATED_LEVERAGE_RATIO = "btc/market-indicator/estimated-leverage-ratio"
        self.MKT_STABLECOIN_SUPPLY_RATIO = "btc/market-indicator/stablecoin-supply-ratio"
        self.MKT_MVRV = "btc/market-indicator/mvrv"
        self.MKT_SOPR = "btc/market-indicator/sopr"
        self.MKT_SOPR_RATIO = "btc/market-indicator/sopr-ratio"
        self.MKT_REALIZED_PRICE = "btc/market-indicator/realized-price"
        self.MKT_UTXO_REALIZED_PRICE_AGRE_DIST = "btc/market-indicator/utxo-realized-price-age-distribution"
        # Bitcoin network indicators
        self.NTW_STOCK_TO_FLOW = "btc/network-indicator/stock-to-flow"
        self.NTW_NVT = "btc/network-indicator/nvt"
        self.NTW_NVT_GOLDEN_CROSS = "btc/network-indicator/nvt-golden-cross"
        self.NTW_NVM = "btc/network-indicator/nvm"
        self.NTW_PUELL_MULTIPLE = "btc/network-indicator/puell-multiple"
        self.NTW_COIN_DAYS_DESTROYED = "btc/network-indicator/cdd"
        self.NTW_MEAN_COIN_AGE = "btc/network-indicator/mca"
        self.NTW_SUM_COIN_AGE = "btc/network-indicator/sca"
        self.NTW_SUM_COIN_AGE_DISTRIBUTION = "btc/network-indicator/sca-distribution"
        self.NTW_NET_UNREALIZED_PNL = "btc/network-indicator/nupl"
        self.NTW_NET_REALIZED_PNL = "btc/network-indicator/nrpl"
        self.NTW_PROFIT_AND_LOSS_UTXO = "btc/network-indicator/pnl-utxo"
        self.NTW_PROFIT_AND_LOSS_SUPPLY = "btc/network-indicator/pnl-supply"
        self.NTW_DORMANCY = "btc/network-indicator/dormancy"
        self.NTW_UTXO_AGE_DISTRIBUTION = "btc/network-indicator/utxo-age-distribution"
        self.NTW_UTXO_REALIZED_AGE_DISTR = "btc/network-indicator/utxo-realized-age-distribution"
        self.NTW_UTXO_COUNT_AGE_DSTR = "btc/network-indicator/utxo-count-age-distribution"
        self.NTW_SPENT_OUTPUT_AGE_DSTR = "btc/network-indicator/spent-output-age-distribution"
        self.NTW_UTXO_SUPPLY_DSTR = "btc/network-indicator/utxo-supply-distribution"
        self.NTW_UTXO_REALIZED_SUPPLY_DSTR = "btc/network-indicator/utxo-realized-supply-distribution"
        self.NTW_UTXO_COUNT_SUPPLY_DSTR = "btc/network-indicator/utxo-count-supply-distribution"
        self.NTW_SPENT_OUTPUT_SUPPLY_DSTR = "btc/network-indicator/spent-output-supply-distribution"
        # Bitcoin Miner Flows
        self.MINER_RESERVE = "btc/miner-flows/reserve"
        self.MINER_NETFLOW = "btc/miner-flows/netflow"
        self.MINER_INFLOW = "btc/miner-flows/inflow"
        self.MINER_OUTFLOW = "btc/miner-flows/outflow"
        self.MINER_TRANSACTIONS_COUNT = "btc/miner-flows/transactions-count"
        self.MINER_ADDRESSES_COUNT = "btc/miner-flows/addresses-count"
        
        super().__init__(api_key)
    
    # -------------------------------------
    # Exchange endpoints
    # -------------------------------------
    
    def get_btc_exch_entity(self, **query_params):
        """
        This method returns entity list to serve data. The meaning of the 
        market_type value of the exchange object is as follows:
            For exchange objects, the market_type field tells whether the 
            exchange is a spot exchange or a derivative exchange. Entities 
            without a market type, such as miners, will 
            return 0 for market_type.
        
        Exchange Market Type	Description
                            0	Undefined
                            1	Spot Exchange
                            2	Derivative Exchange

        Parameters
        ----------
        **query_params :
            type_ (str, required): A type from the entity in exchange, bank, 
                                    miner.
            format_ (str:optional): A format type about return message type. 
                            Supported formats are json, csv. Default is json

        Returns
        -------
        dict
            Entity list on a given type.

        """
        return super().handle_request(self.EXCH_ENTITY_URL, query_params)
    
    def get_btc_exch_reserve(self, **query_params):
        """
        This endpoint returns the full historical on-chain balance 
        of Bitcoin exchanges.

        Parameters
        ----------
        **query_params :
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
            The amount of BTC on a given exchange on this window.

        """
        return super().handle_request(self.EXCH_RESERVES, query_params)
    
    def get_btc_exch_netflow(self, **query_params):
        """
        The difference between coins flowing into exchanges and flowing out of 
        exchanges. Netflow usually helps us to figure out an increase of idle 
        coins waiting to be traded in a certain time frame.

        Parameters
        ----------
        **query_params :
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
            total netfow.

        """
        return super().handle_request(self.EXCH_NETFLOW, query_params)
    
    def get_btc_exch_inflow(self, **query_params):
        """
        Inflow of BTC into exchange wallets for as far back as CQ track. 
        The average inflow is the average transaction value for transactions 
        flowing into exchange wallets on a given day.

        Parameters
        ----------
        **query_params :
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
            inflow total, top 10 inflow, mean inflow, and 7 day sma inflow.

        """
        return super().handle_request(self.EXCH_INFLOW, query_params)
    
    def get_btc_exch_outflow(self, **query_params):
        """
        Outflow of BTC into exchange wallets for as far back as CQ track. 
        The average outflow is the average transaction value for transactions 
        flowing into exchange wallets on a given day.

        Parameters
        ----------
        **query_params :
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
            outflow total, top 10 outflow, mean outflow, and 7 day sma outflow.

        """
        return super().handle_request(self.EXCH_OUTFLOW, query_params)
    
    def get_btc_exch_txn(self, **query_params):
        """
        This endpoint returns the number of transactions flowing in/out of 
        Bitcoin exchanges.

        Parameters
        ----------
        **query_params :
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
            Transactions count inflows and transactions count outflow

        """
        
        return super().handle_request(self.EXCH_TNX_COUNT, query_params)
    
    def get_btc_exch_addrs(self, **query_params):
        """
        Number of addresses involved in inflow/outflow transactions.

        Parameters
        ----------
        **query_params :
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
        return super().handle_request(self.EXCH_ADDRESSES_COUNT, query_params)
    
    def get_btc_exch_inhouseflow(self, **query_params):
        """
        This endpoint returns the in-house flow of BTC within wallets of the 
        same exchange for as far back as CQ track. The average in-house flow is
        the average transaction value for transactions flowing within wallets
        on a given day.

        Parameters
        ----------
        **query_params :
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
            Total flow, mean flow, count transactions flow

        """
        return super().handle_request(self.EXCH_INHOUSE_FLOW, query_params)
    
    # -------------------------------------
    # BTC Flow Indicator
    # -------------------------------------
    
    def get_btc_idx_mpi(self, **query_params):
        """
        MPI(Miners’ Position Index) is a z score of a specific period. The 
        period range must be 2 days or more and if not, it will return an error.
        mpi is an index to understand miners’ behavior by examining the total 
        outflow of miners. It highlights periods where the value of Bitcoin’s 
        outflow by miners on a daily basis has historically been extremely high 
        or low. MPI values above 2 indicate that most of the miners are selling 
        Bitcoin. MPI values under 0 indicate that there is less selling pressure 
        by miners.

        Parameters
        ----------
        **query_params :
            window (str, optional): Currently, we only support day.
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
            Miners position index

        """
        return super().handle_request(self.IDX_MPI, query_params)
    
    def get_btc_idx_exchshutdown(self, **query_params):
        """
        Stay Ahead of Exchange Hacks. See hacks as they happen by identifying 
        sudden increases and become zero in exchange outflows and hedge against
        potential risk.

        Parameters
        ----------
        **query_params :
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): Currently, we only support day.
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
            Exchange Shutdown Index

        """
        return super().handle_request(self.IDX_EXCHANGE_SHUTDOWN, query_params)
    
    def get_btc_idx_whale(self, **query_params):
        """
        Find Whale Focused Exchanges with Top 10 Inflows. Looking at the relative
        size of the top 10 inflows to total inflows, it is possible to discover
        which exchanges whales use. For example, as Gemini has mostly whales 
        users, it is possible for the price to rise or fall dramatically. This
        has potential risks, but also the possibility of arbitrage.

        Parameters
        ----------
        **query_params :
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): Currently, we only support day.
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
            The total BTC amount of top 10 inflow amount divided by the total BTC
            amount flowed into exchange.

        """
        return super().handle_request(self.IDX_EXCHANGE_WHALE_RATIO, query_params)
    
    def get_btc_idx_fundflow(self, **query_params):
        """
        Fund Flow Ratio provides the amount of bitcoins that exchanges occupy 
        among the bitcoins sent underlying the Bitcoin network. Knowing the 
        amount of fund currently involved in trading can help you understand 
        market volatility.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): Currently, we only support day.
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
            The total BTC inflow and outflow of exchange divided by the total
            BTC transferred on the Bitcoin network.

        """
        return super().handle_request(self.IDX_FUND_FLOW_RAIO, query_params)
    
    def get_btc_idx_stableratio(self, **query_params):
        """
        BTC reserve divided by all stablecoins reserve held by an exchange. 
        This usually indicates potential sell pressure. Supported exchanges are
        determined by the concurrent validity of both BTC and Stablecoins 
        (for at least 1 token).

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): Currently, we only support day.
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
            Total BTC reserve divided by all stablecoins reserve held by an
            exchange.

        """
        return super().handle_request(self.IDX_STABLECOINS_RATIO, query_params)
    
    def get_btc_idx_agedistr(self, **query_params):
        """
        Exchange Inflow Age Distribution is a set of active inflow to exchanges
        with age bands. This indicator summarizes the behaviors of long-term or 
        short-term holders flowed into the exchanges. CQ provide the distribution
        values in native and percent values.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): Currently, we only support day.
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
            Exchange inflow age distribution.

        """
        return super().handle_request(self.IDX_EXCHANGE_INFLOW_AGE_DSTR, query_params)
    
    def get_btc_idx_supplydstr(self, **query_params):
        """
        Exchange Inflow Supply Distribution is a set of active inflow to 
        exchanges with balance (supply) bands. This indicator summarizes the 
        behaviors of whales or retails flowed into the exchanges, separated by 
        amount of coins they hold along with price actions. We provide the 
        distribution values in native and percent values.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): Currently, we only support day.
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
            Exchange inflow supply distribution.

        """
        return super().handle_request(self.IDX_EXCHANGE_INFLOW_SUPPLY_DSTR, query_params)
    
    def get_btc_idx_cdd(self, **query_params):
        """
        Exchange Inflow CDD is a subset of Coin Days Destroyed (CDD) where 
        coins are destroyed by flowing into exchanges. This indicator is 
        noise-removed version of CDD with respect to exchange dumping signal.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): Currently, we only support day.
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
            Exchange inflow cdd.

        """
        return super().handle_request(self.IDX_EXCHANGE_INFLOW_CDD, query_params)
    
    def get_btc_idx_exchsupplyratio(self, **query_params):
        """
        Exchange Supply Ratio is calculated as exchange reserve divided by 
        total supply. The metric measures how much tokens are reserved in the 
        exchange relative to total supply of the token.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): Currently, we only support day.
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
        return super().handle_request(self.IDX_EXCHANGE_SUPPLY_RATIO, query_params)
    
    def get_btc_idx_minersupplyratio(self, **query_params):
        """
        Miner Supply Ratio is calculated as miner reserve divided by total 
        supply. The metric measures how much tokens are reserved in the miner 
        relative to total supply of the token.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): Currently, we only support day.
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
            Ratio of reserved token in the miner relative to total supply.

        """
        return super().handle_request(self.IDX_MINER_SUPPLY_RATIO, query_params)
    
    # -------------------------------------
    # BTC Market Indicator
    # -------------------------------------
    
    def get_btc_mkt_leverage(self, **query_params):
        """
        By dividing the open interest of an exchange by their BTC reserve, you
        can estimate a relative average user leverage. Whenever the leverage 
        value reaches a high, there is rapid volatility. Similar to Open Interest,
        but more accurate because it reflects the growth of the exchange itself.
        This is experimental indicator but it seems this reflects market sentiment.
        You can see how aggressive people are and how conservative they are in
        terms of investment. For 'In Progress' exchanges, estimated leverage 
        ratio is not supported yet even though they provide open interest.
        
        Note: This endpoint does not support Point-In-Time (PIT) accuracy due
        to periodic updates to wallet address clustering. Historical data may
        change as new exchange wallets are discovered, added, and validated.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): Currently, we only support day.
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
            The amount of open interest of exchange divided by their BTC reserve

        """
        return super().handle_request(self.MKT_ESTIMATED_LEVERAGE_RATIO, query_params)
    
    def get_btc_mkt_ssr(self, **query_params):
        """
        SSR(Stablecoin Supply Ratio) is a ratio of stablecoin supply in the 
        whole cryptocurrency market where stablecoin is used as fiat substitute
        for trading. This means that the supply of stablecoin can be used to 
        assess the potential buying pressure for bitcoin. The historical 
        starting point is 2017-11-28 00:00:00.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Stablecoin supply ratio.

        """
        return super().handle_request(self.MKT_STABLECOIN_SUPPLY_RATIO, query_params)
    
    def get_btc_mkt_mvrv(self, **query_params):
        """
        MVRV(Market-Value-to-Realized-Value) is a ratio of market_cap divided
        by realized_cap. It can be interpreted as the relationship between 
        short-term and long-term investors (i.e. speculators vs hodlers). 
        When this value is too high, BTC price may be overvalued, and if it is
        too low, there is a possibility that the price is undervalued.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Market-Value-to-Realized-Value

        """
        return super().handle_request(self.MKT_MVRV, query_params)
    
    def get_btc_mkt_sopr(self, **query_params):
        """
        sopr is abbreviation of Spent Output Profit Ratio. Spent Output Profit Ratio
        evaluates the profit ratio of the whole market participants by comparing
        the value of outputs at spent time to created time. sopr is a ratio 
        that is calculated as the USD value of spent outputs at the spent time
        divided by the USD value of spent outputs at the created time. So you 
        can see the value when UTxO destroyed. In a simple way, you can estimate
        the distribution of spent transaction output are in profit or not.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Spent Output Profit Ratio

        """
        return super().handle_request(self.MKT_SOPR, query_params)
    
    def get_btc_mkt_soprratio(self, **query_params):
        """
        SOPR Ratio is calculated as long term holders' SOPR divided by short 
        term holders' SOPR. Higher value of the ratio means higher spent 
        profit of LTH over STH, which is usually useful for spotting market tops.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Long term holders SOPR divided by short term holders SOPR

        """
        return super().handle_request(self.MKT_SOPR_RATIO, query_params)
    
    def get_btc_mkt_realizedprice(self, **query_params):
        """
        Realized Price is calculated as Realized Cap divided by the total coin 
        supply. It measures the average price weighted by the supply of what 
        the entire market participants paid for their coins. It sometimes can
        be interpreted as the on-chain support or resistance price.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Realized cap divided by total supply.

        """
        return super().handle_request(self.MKT_REALIZED_PRICE, query_params)
    
    def get_btc_mkt_utxo(self, **query_params):
        """
        UTxO Realized Price Age Distribution is a set of realized prices along 
        with age bands. The metrics help us to overview each cohort’s holding
        behavior by overlaying a set of different realized prices.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            UTxO Realized Price Age Distribution.

        """
        return super().handle_request(self.MKT_UTXO_REALIZED_PRICE_AGRE_DIST, query_params)
    
    # -------------------------------------
    # BTC Network Indicator
    # -------------------------------------
    
    def get_btc_ntw_stock2flow(self, **query_params):
        """
        Stock to Flow is a metric used to assume bitcoin price based on its 
        scarcity just like gold, silver, and other valuable objects that are 
        limited in amount and costly to earn. The same model for evaluating the
        value of those objects can be adopted to assess the value of bitcoin. 
        The scarcity is calculated by dividing currently circulating coins in 
        the blockchain network to newly supplied coins.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Stock to flow and stock to flow reversion.

        """
        return super().handle_request(self.NTW_STOCK_TO_FLOW, query_params)
    
    def get_btc_ntw_nvt(self, **query_params):
        """
        NVT(Network Value to Transaction) ratio is the network value(supply_total * price_usd)
        divided by tokens_transferred_total. nvt is a metric often used to 
        determine whether Bitcoin price is overvalued or not. The theory behind 
        this indicator is that the value of the token depends on how actively
        transactions take place on the network.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Network Value to Transaction ratio.

        """
        return super().handle_request(self.NTW_NVT, query_params)
    
    def get_btc_ntw_nvtgoldencross(self, **query_params):
        """
        NVT Golden Cross is a modified index of NVT that provides local tops 
        and bottoms. NVT Golden Cross values above 2.2 indicate that downside
        risk goes up. NVT Golden Cross values below -1.6 mean huge upside 
        potential will occur.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            NVT golden cross.

        """
        return super().handle_request(self.NTW_NVT_GOLDEN_CROSS, query_params)
    
    def get_btc_ntw_nvm(self, **query_params):
        """
        NVM(Network Value to Metcalfe Ratio) is a metric based on Metcalfe’s law;
        the value of a network is proportional to the square of its nodes or user. 
        NVM is a ratio of market cap divided by daily active address. Based on 
        Metcalfe’s law, the value of bitcoin rises if the daily active addresses
        increase. Therefore, if the NVM value is relatively small, it means that 
        the value of the network is underestimated and if the value is relatively
        high, it means that the value of the network is overestimated.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Network Value to Metcalfe Ratio.

        """
        return super().handle_request(self.NTW_NVM, query_params)
    
    def get_btc_ntw_puell(self, **query_params):
        """
        Puell Multiple is the mining revenue usd divided by MA 365 mining 
        revenue usd. puell_multiple is a metric shows the historically low and 
        high periods of the value of bitcoin issued daily, and at what point 
        investors should buy bitcoin to get high returns. This indicator was 
        created by David Puell.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Puell Multiple.

        """
        return super().handle_request(self.NTW_PUELL_MULTIPLE, query_params)
    
    def get_btc_ntw_cdd(self, **query_params):
        """
        Coin Days Destroyed reflects market participants who have been in the
        bitcoin on-chain for longer. This indicator gives more weight to 
        long-term-holder position. cdd is the sum of products of spent 
        transaction output alive days and its value. sa_cdd is abbreviation of 
        supply-adjusted cdd. Since cdd increases as the newly created block
        mined, we need an indicator which normalize cdd value. sa_cdd is
        calculated by cdd over supply_total. average_sa_cdd is the average
        value of sa_cdd since genesis block. binary_cdd is the signal whether
        current sa_cdd is larger than average_sa_cdd or not. If 
        sa_cdd > average_sa_cdd, then binary_cdd is 1. In conclusion, 
        these indicators help us to estimate how whale's moving.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            cdd.

        """
        return super().handle_request(self.NTW_COIN_DAYS_DESTROYED, query_params)
    
    def get_btc_ntw_mca(self, **query_params):
        """
        Mean Coin Age is the mean value of products of bitcoin unspent 
        transaction output alive days and its value. It is basically similar to
        cdd. But mca focuses on unspent transaction output. Mean Coin Dollar 
        Age is the sum value of products of bitcoin unspent transaction output 
        alive days, value, and price at the created time.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            mca.

        """
        return super().handle_request(self.NTW_MEAN_COIN_AGE, query_params)
    
    def get_btc_ntw_sca(self, **query_params):
        """
        Sum Coin Age is the sum value of products of bitcoin unspent
        transaction output alive days and its value. It is basically similar to 
        cdd. But sca focuses on unspent transaction output. Sum Coin Dollar Age
        is the sum value of products of bitcoin unspent transaction output 
        alive days, value, and price at the created time.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Sum Coin age.

        """
        return super().handle_request(self.NTW_SUM_COIN_AGE, query_params)
    
    def get_btc_ntw_scad(self, **query_params):
        """
        This indicator shows the distribution of long-term holder and
        short-term holder with UTxO data. It is similar to UTxO distribution,
        but weighted by alive days to highlight long-term holder's distribution
        in different ranges. Each field is calculated as the sum of the 
        products of bitcoin unspent transaction output alive days and its 
        value in a given period, divided by their sum. If long-term SCA 
        distribution ratio increases, then we can interpret this as one of 
        bullish moment.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Sum Coin Age Distribution.

        """
        return super().handle_request(self.NTW_SUM_COIN_AGE_DISTRIBUTION, query_params)
    
    def get_btc_ntw_nupl(self, **query_params):
        """
        Net Unrealized Profit and Loss shows how different between market_cap 
        and realized_cap. nupl is calculated as difference between market_cap 
        and realized_cap divided by market_cap. If market_cap > realized_cap, 
        then nupl > 0, which means bitcoin on-chain expected value is less than
        what they actually have. So this value will give selling pressure. nup 
        is net unrealized profit, which is calculated as sum of products of 
        UTxO's value and price difference between created and destroyed, 
        divided by market_cap. nup only contains UTxOs in profit. nul is net
        unrealized loss. This is opposite indicator of nup. It only contains
        UTxOs in loss.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Net unrealized profit and loss.

        """
        return super().handle_request(self.NTW_NET_UNREALIZED_PNL, query_params)
    
    def get_btc_ntw_nrpl(self, **query_params):
        """
        Net Realized Profit/Loss metric presenting the net magnitude of profit,
        or loss realized by all holders spending coins. Realized Profit/Loss is 
        assessed relative to the price when a coin last moved.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Net realized profit and loss.

        """
        return super().handle_request(self.NTW_NET_REALIZED_PNL, query_params)
    
    def get_btc_ntw_pnlutxo(self, **query_params):
        """
        Profit and Loss (UTxO) evaluates the number of UTxOs being in profit or 
        not by comparing the price between created and destroyed. When the 
        price at destroyed time is higher than created, this transaction is in
        profit.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Profit and Loss UTxO.

        """
        return super().handle_request(self.NTW_PROFIT_AND_LOSS_UTXO, query_params)
    
    def get_btc_ntw_pnlsupply(self, **query_params):
        """
        Profit and Loss (Supply) evaluates the sum of UTxOs being in profit or 
        not by comparing the price between created and destroyed. These metrics
        are similar to the ones in Profit and Loss (UTxO) but differ from 
        putting more weight on each UTxO with its value. Sometimes we want to 
        know the exact alive bitcoin transaction output value in profit. 
        pnl-supply will show it accuretely. pnl-supply is calculated as the sum
        of UTxO value.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Profit and Loss (Supply).

        """
        return super().handle_request(self.NTW_PROFIT_AND_LOSS_SUPPLY, query_params)
    
    def get_btc_ntw_dormancy(self, **query_params):
        """
        Average Dormancy (average_dormancy) is the average number of days 
        destroyed per coin transacted. Supply-Adjusted Average Dormancy 
        (sa_average_dormancy) is the average dormancy normalized by supply 
        total, where supply total increases as more blocks mined.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Te average number of days destroyed per coin transacted.

        """
        return super().handle_request(self.NTW_DORMANCY, query_params)
    
    def get_btc_ntw_utxo_age_distr(self, **query_params):
        """
        UTxO Age Distribution is a set of active supply with age bands. This 
        indicator summarizes the behaviors of long-term or short-term holders
        along with price actions. We provide the distribution values in native,
        USD, and percent values.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            UTxO Age Distribution.

        """
        return super().handle_request(self.NTW_UTXO_AGE_DISTRIBUTION, query_params)
    
    def get_btc_ntw_utxo_realized_age_dstr(self, **query_params):
        """
        UTxO Realized Age Distribution is a set of active supply with age bands
        weighted by the price at UTxO created time. Similar to Realized Cap, 
        this indicator summarizes the capitalization held by long-term or 
        short-term holders (each band). We provide the distribution values in 
        native, USD, and percent values.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            UTxO Realized Age Distribution.

        """
        return super().handle_request(self.NTW_UTXO_REALIZED_AGE_DISTR, query_params)
    
    def get_btc_ntw_utxo_count_age_dstr(self, **query_params):
        """
        UTxO Count Age Distribution is a set of active number of holders with 
        age bands. This indicator summarizes how many long-term or short-term
        holders exist by each band. We provide the distribution values in 
        native, and percent values.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            UTxO Count Age Distribution.

        """
        return super().handle_request(self.NTW_UTXO_COUNT_AGE_DSTR, query_params)
    
    def get_btc_ntw_spent_output_age_dstr(self, **query_params):
        """
        Spent Output Age Distribution is a set of active sum of spent outputs
        with age bands. This indicator summarizes how much UTxOs are destroyed
        by long-term or short-term holders (each band). We provide the 
        distribution values in native, USD, and percent values.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Spent Output Age Distribution.

        """
        return super().handle_request(self.NTW_SPENT_OUTPUT_AGE_DSTR, query_params)
    
    def get_btc_ntw_utxo_supply_dstr(self, **query_params):
        """
        UTxO Supply Distribution is a set of active supply with balance 
        (supply) bands. This indicator summarizes the behaviors of whales or
        retails separated by amount of coins they hold along with price 
        actions. We provide the distribution values in native, and percent
        values.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            UTxO Supply Distribution.

        """
        return super().handle_request(self.NTW_UTXO_SUPPLY_DSTR, query_params)
    
    def get_btc_ntw_utxo_realized_supply_dstr(self, **query_params):
        """
        UTxO Realized Supply Distribution is a set of active supply with 
        balance (supply) bands weighted by the price at UTxO created time. 
        Similar to Realized Cap, this indicator summarizes the capitalization 
        held by whales or retails (each band). We provide the distribution 
        values in USD, and percent values.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            UTxO Realized Supply Distribution.

        """
        return super().handle_request(self.NTW_UTXO_REALIZED_SUPPLY_DSTR, query_params)
    
    def get_btc_ntw_utxo_count_supply_dstr(self, **query_params):
        """
        UTxO Count Supply Distribution is a set of active number of holders
        with balance (supply) bands. This indicator summarizes how many whales 
        and retails exist by each band. We provide the distribution values in
        native, and percent values.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            UTxO Count Supply Distribution.

        """
        return super().handle_request(self.NTW_UTXO_COUNT_SUPPLY_DSTR, query_params)
    
    def get_btc_ntw_spent_output_supply_dstr(self, **query_params):
        """
        Spent Output Supply Distribution is a set of active sum of spent 
        outputs with balance (supply) bands. This indicator summarizes how much
        UTxOs are destroyed by whales or retails (each band). We provide the 
        distribution values in native, USD, and percent values.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): Currently, we only support day.
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
            Spent Output Supply Distribution.

        """
        return super().handle_request(self.NTW_SPENT_OUTPUT_SUPPLY_DSTR, query_params)
    
    # -------------------------------------
    # BTC Miner Flows
    # -------------------------------------
    
    def get_btc_miner_reserve(self, **query_params):
        """
        This endpoint returns the full historical on-chain balance of Bitcoin 
        mining pools.

        Parameters
        ----------
        **query_params : TYPE
            miner (str, required): A mining pool from the table that CQ support
            window (str, optional): Currently, we only support day.
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
            The amount of BTC on the given miner on this window.

        """
        return super().handle_request(self.MINER_RESERVE, query_params)
    
    def get_btc_miner_netflow(self, **query_params):
        """
        The difference between coins flowing into mining pools and flowing out
        of mining pools. Netflow usually helps us to figure out an increase of
        idle coins waiting to be traded in a certain time frame.

        Parameters
        ----------
        **query_params : TYPE
            miner (str, required): A mining pool from the table that CQ support
            window (str, optional): Currently, we only support day.
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
            Total netflow.

        """
        return super().handle_request(self.MINER_NETFLOW, query_params)
    
    def get_btc_miner_inflow(self, **query_params):
        """
        This endpoint returns the inflow of BTC into mining pool wallets for as
        far back as CQ track. The average inflow is the average transaction 
        value for transactions flowing into mining pool wallets on a given day.

        Parameters
        ----------
        **query_params : TYPE
            miner (str, required): A mining pool from the table that CQ support
            window (str, optional): Currently, we only support day.
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
            Miner inflows.

        """
        return super().handle_request(self.MINER_INFLOW, query_params)
    
    def get_btc_miner_outflow(self, **query_params):
        """
        This endpoint returns the outflow of BTC into mining pool wallets for
        as far back as we track. The average outflow is the average transaction
        value for transactions flowing out of mining pool wallets on a given 
        day.

        Parameters
        ----------
        **query_params : TYPE
            miner (str, required): A mining pool from the table that CQ support
            window (str, optional): Currently, we only support day.
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
            Miner outflows.

        """
        return super().handle_request(self.MINER_OUTFLOW, query_params)
    
    def get_btc_miner_txn_count(self, **query_params):
        """
        Transactions flowing in/out of Bitcoin miners.

        Parameters
        ----------
        **query_params : TYPE
            miner (str, required): A mining pool from the table that CQ support
            window (str, optional): Currently, we only support day.
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
            Miner transactions, in and out.

        """
        return super().handle_request(self.MINER_TRANSACTIONS_COUNT, query_params)
    
    def get_btc_miner_addr_count(self, **query_params):
        """
        Number of addresses involved in inflow/outflow transactions.

        Parameters
        ----------
        **query_params : TYPE
            miner (str, required): A mining pool from the table that CQ support
            window (str, optional): Currently, we only support day.
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
            Miner addresses count, in and out.

        """
        return super().handle_request(self.MINER_ADDRESSES_COUNT, query_params)