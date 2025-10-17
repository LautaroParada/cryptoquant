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
        return super().handle_request(self.ENTITY_SHARE, query_params)