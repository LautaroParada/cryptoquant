# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 15:46:25 2025

@author: lauta
"""

from cryptoquant.request_handler_class import RequestHandler

class XRP(RequestHandler):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        
        # Entity List
        self.ENTITY_LIST = "xrp/status/entity-list"
        # Entity flows
        self.ENTITY_RESERVE = "xrp/entity-flows/reserve"
        self.ENTITY_SHARE = "xrp/entity-flows/share"
        self.ENTITY_TRANSACTION_COUNT = "xrp/entity-flows/transactions-count"
        self.ENTITY_INFLOW = "xrp/entity-flows/inflow"
        self.ENTITY_OUTFLOW = "xrp/entity-flows/outflow"
        self.ENTITY_ADDRESSES_COUNT = "xrp/entity-flows/addresses-count"
        self.ENTITY_WHALE_MOVEMENTS = "xrp/entity-flows/whale-movements"
        # Flow Indicators
        self.FLOW_EXCHANGE_INFLOW_VALUE_DISTRIBUTION = "xrp/flow-indicator/exchange-inflow-value-distribution"
        self.FLOW_EXCHANGE_OUTFLOW_VALUE_DISTRIBUTION = "xrp/flow-indicator/exchange-outflow-value-distribution"
        self.FLOW_EXCHANGE_INFLOW_COUNT_VALUE_DISTRIBUTION = "xrp/flow-indicator/exchange-inflow-count-value-distribution"
        self.FLOW_EXCHANGE_OUTFLOW_COUNT_VALUE_DISTRIBUTION = "xrp/flow-indicator/exchange-outflow-count-value-distribution"
        self.FLOW_EXCHANGE_SUPPLY_RATIO = "xrp/flow-indicator/exchange-supply-ratio"
        # Market data
        self.MARKET_PRICE_OHLCV = "xrp/market-data/price-ohlcv"
        self.MARKET_OPEN_INTEREST = "xrp/market-data/open-interest"
        self.MARKET_FUNDING_RATES = "xrp/market-data/funding-rates"
        self.MARKET_TAKER_BUY_SELL_STATS = "xrp/market-data/taker-buy-sell-stats"
        self.MARKET_LIQUIDATIONS = "xrp/market-data/liquidations"
        self.MARKET_CAPITALIZATION = "xrp/market-data/capitalization"
        self.MARKET_ESTIMATED_LEVERAGE_RATIO = "xrp/market-data/estimated-leverage-ratio"
        # Network data
        self.NETWORK_ADDRESSES_COUNT = "xrp/network-data/addresses-count"
        self.NETWORK_VELOCITY = "xrp/network-data/velocity"            
        self.NETWORK_BLOCK_INTERVAL = "xrp/network-data/block-interval"
        self.NETWORK_XRP_BURNT = "xrp/network-data/xrp-burnt"
        self.NETWORK_LEDGER_COUNT = "xrp/network-data/ledger-count"
        
    # -----------------------------------
    # Entity list
    # -----------------------------------
    
    def get_xrp_entity_list(self, **query_params):
        """
        This endpoint returns entity list to serve data.

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
        return super().handle_request(self.ENTITY_LIST, query_params)
    
    # -----------------------------------
    # Entity flows
    # -----------------------------------
    
    def get_xrp_entity_reserve(self, **query_params):
        """
        This namespace contains endpoints to retrieve metrics related to XRP 
        Entity Flows. Currently, We only supports Exchanges for available 
        entities. Supported Exchanges: Binance, Bitfinex, Bitget, Bithumb, 
        Bitstamp, Bybit, Gate.io, HTX Global, Kucoin, OKX, Upbit

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day, hour, and 10min.
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
            The amount of XRP on a given entity on this window.

        """
        return super().handle_request(self.ENTITY_RESERVE, query_params)
    
    def get_xrp_entity_share(self, **query_params):
        """
        This metric is calculated by dividing XRP holdings of the entity by the 
        total supply

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day and hour.
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
            The amount of XRP on a given entity on this window.

        """
        return super().handle_request(self.ENTITY_SHARE, query_params)
    
    def get_xrp_entity_trx_count(self, **query_params):
        """
        This endpoint returns the number of transactions flowing in/out of XRP 
        Entities.

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
            transactions flowing in/out of XRP 
            Entities.

        """
        return super().handle_request(self.ENTITY_TRANSACTION_COUNT, query_params)
    
    def get_xrp_entity_inflow(self, **query_params):
        """
        This endpoint returns the inflow of XRP into entity address for as far 
        back as we track.

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
            inflow and inflow_usd.

        """
        return super().handle_request(self.ENTITY_INFLOW, query_params)
    
    def get_xrp_entity_outflow(self, **query_params):
        """
        This endpoint returns the outflow of XRP out of entity address for as 
        far back as we track.

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
            outflow and outflow_usd.

        """
        return super().handle_request(self.ENTITY_OUTFLOW, query_params)
    
    def get_xrp_entity_addrs_count(self, **query_params):
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
            The number of addresse evoking inflow/outflow transactions
            to bank wallets.

        """
        return super().handle_request(self.ENTITY_ADDRESSES_COUNT, query_params)
    
    def get_xrp_entity_whale_movements(self, **query_params):
        """
        This endpoint returns the number of transactions involved in 
        inflow/outflow transactions and the transfer volume

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
            The number of transaction evoking inflow/outflow transactions to
            whale addresses.

        """
        return super().handle_request(self.ENTITY_WHALE_MOVEMENTS, query_params)
    
    # -----------------------------------
    # XRP Flow Indicator
    # -----------------------------------
    
    def get_xrp_flow_exch_inflow_value_dstr(self, **query_params):
        """
        Exchange Inflow Value Distribution is a metric that shows the amount 
        distribution of xrp tokens flowed into exchange wallets according to 
        its value.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day and hour.
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
            Exchange inflows distribution band by the amount of the transferred 
            tokens (xrp) at once.

        """
        return super().handle_request(self.FLOW_EXCHANGE_INFLOW_VALUE_DISTRIBUTION, query_params)
    
    def get_xrp_flow_exch_outflow_value_dstr(self, **query_params):
        """
        Exchange Outflow Value Distribution is a metric that shows the amount 
        distribution of xrp tokens flowed out from exchange wallets according 
        to its value.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day and hour.
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
            Exchange inflows distribution band by the amount of the transferred 
            tokens (xrp) at once.

        """
        return super().handle_request(self.FLOW_EXCHANGE_OUTFLOW_VALUE_DISTRIBUTION, query_params)
    
    def get_xrp_flow_exch_inflow_count_value_dstr(self, **query_params):
        """
        Exchange Inflow Count Value Distribution is a metric that shows the 
        number of transactions of xrp tokens flowed into exchange wallets 
        according to its value segment.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day and hour.
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
            Number of transactions of each exchnage inflows distribution band
            by the amount of the transferred tokens (xrp) at once.

        """
        return super().handle_request(self.FLOW_EXCHANGE_INFLOW_COUNT_VALUE_DISTRIBUTION, query_params)
    
    def get_xrp_flow_exch_outflow_count_value_dstr(self, **query_params):
        """
        Exchange Outflow Count Value Distribution is a metric that shows the 
        number of transactions of xrp tokens flowed into exchange wallets 
        according to its value segment.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day and hour.
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
            Number of transactions of each exchange outflows distribution band
            by the amount of the transferred tokens (xrp) at once.

        """
        return super().handle_request(self.FLOW_EXCHANGE_OUTFLOW_COUNT_VALUE_DISTRIBUTION, query_params)
    
    def get_xrp_flow_exch_supply_ratio(self, **query_params):
        """
        The ratio of exchange's xrp reserve compared to total supply of xrp.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day and hour.
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
            exchange supply ratio.

        """
        return super().handle_request(self.FLOW_EXCHANGE_SUPPLY_RATIO, query_params)
    
    # -----------------------------------
    # XRP Market Data
    # -----------------------------------
    
    def get_xrp_mkt_ohlcv(self, **query_params):
        """
        This endpoint returns metrics related to XRP's Price. Price OHLCV data 
        consists of five metrics.  open, the opening price at the beginning of 
        the window, close, USD closing price at the end of the window,  high, 
        the highest USD price in a given window, low, the lowest USD price in a
        given window, and volume, the total token volume traded in 24h.
        
        full documentation: https://cryptoquant.com/docs#tag/XRP-Market-Data/operation/getPriceOHLCVXRP

        Parameters
        ----------
        **query_params : TYPE
            market (str, optional): A market type from the tbale that CQ
                                    support.
            exchange (str, optional): An exchange supported by CryptoQuant.
            symbol (str, optional): A XRP pair symbol from the table that CQ
                                    support.
            window (str, optional): day, hour, min.
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
            Pirce OHLCV data.

        """
        return super().handle_request(self.MARKET_PRICE_OHLCV, query_params)
    
    def get_xrp_mkt_open_interest(self, **query_params):
        """
        This endpoint returns XRP Perpetual Open Interest from derivative 
        exchanges.
        
        full documentation: https://cryptoquant.com/docs#tag/XRP-Market-Data/operation/XRPgetOpenInterest

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            symbol (str, optional): A XRP pair symbol from the table that CQ
                                    support.
            window (str, optional): day, hour, min.
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
    
    def get_xrp_mkt_funding_rates(self, **query_params):
        """
        Funding rates represents traders' sentiments of which position they bet
        on in perpetual swaps market. Positive funding rates implies that many
        traders are bullish and long traders pay funding to short traders. 
        Negative funding rates implies many traders are bearish and short
        traders pay funding to long traders.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            symbol (str, optional): A XRP pair symbol from the table that CQ
                                    support.
            window (str, optional): day, hour, min.
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
        TYPE
            DESCRIPTION.

        """
        return super().handle_request(self.MARKET_FUNDING_RATES, query_params)
    
    def get_xrp_mkt_taker_buysell_stats(self, **query_params):
        """
        Taker Buy/Sell Stats represent takers' sentiment of which position they
        are taking in the market. This metric is calculated with perpetual swap
        trades in each exchange. taker_buy_volume is volume that takers buy. 
        taker_sell_volume is volume that takers sell. taker_total_volume is the
        sum of taker_buy_volume and taker_sell_volume. taker_buy_ratio is the 
        ratio of taker_buy_volume divided by taker_total_volume. taker_sell_ratio
        is the ratio of taker_sell_volume divided by taker_total_volume. 
        taker_buy_sell_ratio is the ratio of taker_buy_volume divided by 
        taker_sell_volume. Note we unify the unit of return value to USD for 
        each exchange where its contract specification may vary.

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day, hour, min.
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
            Taker buy, sell volume ratio.

        """
        return super().handle_request(self.MARKET_TAKER_BUY_SELL_STATS, query_params)
    
    def get_xrp_mkt_liquidations(self, **query_params):
        """
        Liquidations are sum of forced market orders to exit leveraged 
        positions caused by price volatility. Liquidations indicate current 
        price volatility and traders' sentiment which side they had been 
        betting. Note that Binance's liquidation data collection policy has 
        changed since 2021-04-27, which makes the distribution of the data has 
        changed after that.
        
        full documentation: https://cryptoquant.com/docs#tag/XRP-Market-Data/operation/XRPgetLiquidations

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            symbol (str, optional): A XRP pair symbol from the table that CQ
                                    support.
            window (str, optional): day, hour, and min
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
    
    def get_xrp_mkt_capitalization(self, **query_params):
        """
        This endpoint returns metrics related to market capitalization. First, 
        CQ provide market_cap, which is total market capitalization of XRP, 
        calculated by multiplying the total supply with its USD price.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day and hour.
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
            Market cap for xrp.

        """
        return super().handle_request(self.MARKET_CAPITALIZATION, query_params)
    
    def get_xrp_mkt_estimated_leverage_ratio(self, **query_params):
        """
        Estimated Leverage Ratio indicates how much leverage is used by users 
        on average. It is defined as the ratio of open interest divided by the
        reserve of an exchange. This information measures traders' sentiment 
        whether they take a high risk or low risk

        Parameters
        ----------
        **query_params : TYPE
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day, hour, and 10min.
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
            Estimated leverage ratio.

        """
        return super().handle_request(self.MARKET_ESTIMATED_LEVERAGE_RATIO, query_params)
    
    # -----------------------------------
    # XRP Network Data
    # -----------------------------------
    
    def get_xrp_ntx_addrs_count(self, **query_params):
        """
        NVT(Network Value to Transaction) ratio is the network value
        (supply_total * price_usd) divided by tokens_transferred_total. 
        nvt is a metric often used to determine whether the price is overvalued 
        or not. The theory behind this indicator is that the value of the token
        depends on how actively transactions take place on the network.

        Parameters
        ----------
        **query_params : TYPE
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
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            The number of active addresses.

        """
        return super().handle_request(self.NETWORK_ADDRESSES_COUNT, query_params)
    
    def get_xrp_ntx_velocity(self, **query_params):
        """
        Velocity measures how quickly units circulate in the network. It is 
        calculated by dividing on-chain transaction volume by market cap, 
        effectively being the inverse of the NVT Ratio.

        Parameters
        ----------
        **query_params : TYPE
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
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            Velocity.

        """
        return super().handle_request(self.NETWORK_VELOCITY, query_params)
    
    def get_xrp_ntx_block_interval(self, **query_params):
        """
        The average time between blocks generated displayed in seconds.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day and hour.
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
            The average time between blocks generated in seconds.

        """
        return super().handle_request(self.NETWORK_BLOCK_INTERVAL, query_params)
    
    def get_xrp_ntx_burnt(self, **query_params):
        """
        The amount of burnt XRP

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day and hour.
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
            Amount of XRP burnt.

        """
        return super().handle_request(self.NETWORK_XRP_BURNT, query_params)
    
    def get_xrp_ntx_ledger_count(self, **query_params):
        """
        The number of ledgers(XRPL version of 'block') created

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
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            Number of total ledger created.

        """
        return super().handle_request(self.NETWORK_LEDGER_COUNT, query_params)