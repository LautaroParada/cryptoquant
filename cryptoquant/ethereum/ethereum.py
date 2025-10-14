# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 10:30:02 2025

@author: lauta
"""

from cryptoquant.request_handler_class import RequestHandler

class Ethereum(RequestHandler):
    def __init__(self, api_key: str):
        super().__init__(api_key)