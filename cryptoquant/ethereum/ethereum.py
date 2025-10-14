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