# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 09:15:55 2025

@author: lauta
"""

from cryptoquant.request_handler_class import RequestHandler

class StableCoins(RequestHandler):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        
        