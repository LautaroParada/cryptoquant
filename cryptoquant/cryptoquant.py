# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 19:23:16 2025

@author: lauta
"""

from cryptoquant.discovery import Discovery
from cryptoquant.bitcoin import Bitcoin

class CryptoQuant(Discovery, Bitcoin):
    def __init__(self, api_key):
        # Sub estructuras de la API
        Discovery.__init__(self, api_key)
        Bitcoin.__init__(self, api_key)