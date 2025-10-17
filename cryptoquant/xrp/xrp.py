# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 15:46:25 2025

@author: lauta
"""

from cryptoquant.request_handler_class import RequestHandler

class XRP(RequestHandler):
    def __init__(self, api_key: str):
        super().__init__(api_key)