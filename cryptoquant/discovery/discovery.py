# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 18:55:33 2025

@author: lauta
"""

from cryptoquant.request_handler_class import RequestHandler

class Discovery(RequestHandler):
    def __init__(self, api_key: str):
        self.URL_ENDPOINT = "discovery/endpoints"
        super().__init__(api_key)
        
    def get_endpoints(self, **query_params):
        """
        Returns all endpoints CQ support with available parameters.

        Parameters
        ----------
        **query_params : TYPE
            A format type about return message type. Supported formats are json, csv.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return super().handle_request(self.URL_ENDPOINT, query_params)