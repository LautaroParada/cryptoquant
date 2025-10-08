# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 14:19:40 2025

@author: lauta
"""

from cryptoquant.request_handler_class import RequestHandler

class Bitcoin(RequestHandler):
    def __init__(self, api_key: str):
        self.ENTITY_URL = "btc/status/entity-list"
        super().__init__(api_key)
        
    def get_bitcoin_entity(self, **query_params):
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
            type_: A type from the entity in exchange, bank, miner.
            format_: A format type about return message type. Supported 
                    formats are json, csv. Default is json

        Returns
        -------
        dict
            The status object is return with most of requests and indicates 
            if the request was successful. If it is not successful, error 
            information is included.

        """
        return super().handle_request(self.ENTITY_URL, query_params) 