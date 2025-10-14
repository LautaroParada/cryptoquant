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