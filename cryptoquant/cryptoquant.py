# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 19:23:16 2025

@author: lauta
"""

from cryptoquant.discovery import Discovery
from cryptoquant.bitcoin import Bitcoin
from cryptoquant.ethereum import Ethereum
from cryptoquant.xrp import XRP
from cryptoquant.stablecoins import StableCoins
from cryptoquant.trx import TRX
from cryptoquant.erc20 import Erc20

class CryptoQuant(Discovery, Bitcoin, Ethereum, XRP, StableCoins, TRX, Erc20):
    def __init__(self, api_key):
        # Sub estructuras de la API
        Discovery.__init__(self, api_key)
        Bitcoin.__init__(self, api_key)
        Ethereum.__init__(self, api_key)
        XRP.__init__(self, api_key)
        StableCoins.__init__(self, api_key)
        TRX.__init__(self, api_key)
        Erc20.__init__(self, api_key)