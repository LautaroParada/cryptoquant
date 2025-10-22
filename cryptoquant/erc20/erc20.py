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