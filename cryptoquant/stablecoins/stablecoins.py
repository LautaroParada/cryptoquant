# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 09:15:55 2025

@author: lauta
"""

from cryptoquant.request_handler_class import RequestHandler

class StableCoins(RequestHandler):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        
        # Entity List
        self.ENTITY_LIST = "stablecoin/status/entity-list"
        # Exchange Flows
        self.RESERVE = "stablecoin/exchange-flows/reserve"
        
    # -----------------------------
    # Entity List
    # -----------------------------
    
    def get_stable_entity_list(self, **query_params):
        """
        This endpoint returns entity list to serve data. Please note that 
        all_token will return bad request for this endpoint. Make sure to use a
        specific stablecoin symbol. The meaning of the market_type value of the
        exchange object is as follows. For exchange objects, the market_type 
        field tells whether the exchange is a spot exchange or a derivative 
        exchange. Entities without a market type, such as miners or banks, will 
        return 0 for market_type.

        Parameters
        ----------
        **query_params : TYPE
            token (str, required): A stablecoin from the table that CQ support.
            type (str, required): A type from the entity exchange.
            format (str, optional): A format type about return message type. 
                                    Supported formats are json, csv.

        Returns
        -------
        dict
            Entity list on a given type.

        """
        return super().handle_request(self.ENTITY_LIST, query_params)
    
    def get_stable_exch_reserve(self, **query_params):
        """
        This endpoint returns the full historical on-chain balance of 
        Stablecoin exchanges.

        Parameters
        ----------
        **query_params : TYPE
            token (str, required): A stablecoin from the table that CQ support.
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
            The amount of Stablecoin on a given exchange on this window.

        """
        return super().handle_request(self.RESERVE, query_params)