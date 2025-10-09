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
        super().__init__(api_key)
    
    #-------------------------------------
    # Exchange endpoints
    #-------------------------------------
    
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