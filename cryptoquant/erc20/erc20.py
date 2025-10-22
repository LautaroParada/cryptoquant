# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 12:57:13 2025

@author: lauta
"""

from cryptoquant.request_handler_class import RequestHandler

class Erc20(RequestHandler):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        
        # Entity list
        self.ENTITY_LIST = "erc20/status/entity-list"
        # Exchange flows
        self.EXCHANGE_FLOWS_RESERVE = "erc20/exchange-flows/reserve"
        self.EXCHANGE_FLOWS_NETFLOW = "erc20/exchange-flows/netflow"
        self.EXCHANGE_FLOWS_INFLOW = "erc20/exchange-flows/inflow"
        self.EXCHANGE_FLOWS_OUTFLOW = "erc20/exchange-flows/outflow"
        self.EXCHANGE_FLOWS_TRANSACTIONS_COUNT = "erc20/exchange-flows/transactions-count"
        
    # -------------------------------
    # Entity list
    # -------------------------------
    
    def get_erc20_entity_list(self, **query_params):
        """
        This endpoint returns entity list to serve data. The meaning of the 
        market_type value of the exchange object is as follows. For exchange 
        objects, the market_type field tells whether the exchange is a spot 
        exchange or a derivative exchange. Entities without a market type, such 
        as miners or banks, will return 0 for market_type.

        Exchange Market Type	Description
        0	                    Undefined
        1	                    Spot Exchange
        2	                    Derivative Exchange

        Parameters
        ----------
        **query_params : TYPE
            token (str, required): A ERC20 token from the table that CQ support.
            type_ (str, required): A type from the entity in exchange.
            format (str, optional): A format type about return message type. 
                                    Supported formats are json, csv.

        Returns
        -------
        dict
            Entity list on a given type.

        """
        return super().handle_request(self.ENTITY_LIST, query_params)
    
    # -------------------------------
    # Exchange Flows
    # -------------------------------
    
    def get_erc20_exch_reserve(self, **query_params):
        """
        This endpoint returns the full historical on-chain ERC20 token balance 
        of exchanges.

        Parameters
        ----------
        **query_params : TYPE
            token (str, required): A ERC20 token from the table that CQ support.
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
            The amount of ERC 20 token on a given exchange on this window.

        """
        return super().handle_request(self.EXCHANGE_FLOWS_RESERVE, query_params)
    
    def get_erc20_exch_netflow(self, **query_params):
        """
        The difference between coins flowing into exchanges and flowing out of 
        exchanges. Netflow usually helps us to figure out an increase of idle 
        coins waiting to be traded in a certain time frame.

        Parameters
        ----------
        **query_params : TYPE
            token (str, required): A ERC20 token from the table that CQ support.
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
            Total netflow.

        """
        return super().handle_request(self.EXCHANGE_FLOWS_NETFLOW, query_params)
    
    def get_erc20_exch_inflow(self, **query_params):
        """
        This endpoint returns the inflow of ERC20 token into exchange wallets 
        for as far back as we track. The average inflow is the average 
        transaction value for transactions flowing into exchange wallets on a 
        given day.

        Parameters
        ----------
        **query_params : TYPE
            token (str, required): A ERC20 token from the table that CQ support.
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
            Inflow statistics.

        """
        return super().handle_request(self.EXCHANGE_FLOWS_INFLOW, query_params)
    
    def get_erc20_exch_outflow(self, **query_params):
        """
        This endpoint returns the outflow of ERC20 token into exchange wallets
        for as far back as we track. The average outflow is the average 
        transaction value for transactions flowing into exchange wallets on a 
        given day.

        Parameters
        ----------
        **query_params : TYPE
            token (str, required): A ERC20 token from the table that CQ support.
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
            outflow statistics.

        """
        return super().handle_request(self.EXCHANGE_FLOWS_OUTFLOW, query_params)
    
    def get_erc20_exch_trx_count(self, **query_params):
        """
        This endpoint returns the number of transactions flowing in/out of 
        ERC20 token exchanges.

        Parameters
        ----------
        **query_params : TYPE
            token (str, required): A ERC20 token from the table that CQ support.
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
            Transactions in and out.

        """
        return super().handle_request(self.EXCHANGE_FLOWS_TRANSACTIONS_COUNT, query_params)