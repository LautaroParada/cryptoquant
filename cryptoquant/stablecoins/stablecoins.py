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