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