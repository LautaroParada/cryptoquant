# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 12:57:13 2025

@author: lauta
"""

from cryptoquant.request_handler_class import RequestHandler

class Erc20(RequestHandler):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        