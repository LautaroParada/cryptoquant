# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 14:19:40 2025

@author: lauta
"""

from cryptoquant.request_handler_class import RequestHandler

class Bitcoin(RequestHandler):
    def __init__(self, api_key: str):
        self.ENTITY_URL = "btc/status/entity-list"
        self.EXCHANGE_FLOWS = "btc/exchange-flows/reserve"
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
            type_ (str, required): A type from the entity in exchange, bank, 
                                    miner.
            format_ (str:optional): A format type about return message type. 
                            Supported formats are json, csv. Default is json

        Returns
        -------
        dict
            Entity list on a given type.

        """
        return super().handle_request(self.ENTITY_URL, query_params)
    
    def get_bitcoin_reserve(self, **query_params):
        """
        This endpoint returns the full historical on-chain balance 
        of Bitcoin exchanges.

        Parameters
        ----------
        **query_params :
            exchange (str, required): An exchange supported by CryptoQuant.
            window (str, optional): day, hour, and block.
            from_ (any, optional): This defines the starting time for which data
                                will be gathered, formatted as YYYYMMDDTHHMMSS 
                                (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                                If window=day is used, it can also be formatted 
                                as YYYYMMDD (date). If window=block is used, you
                                can also specify the exact block height (e.g. 510000). 
                                If this field is not specified, response will 
                                include data from the earliest time.
           to_ (any, optinal): This defines the ending time for which data will
                               be gathered, formatted as YYYYMMDDTHHMMSS 
                               (indicating YYYY-MM-DDTHH:MM:SS, UTC time). 
                               If window=day is used, it can also be formatted 
                               as YYYYMMDD (date). If window=block is used, you
                               can also specify the exact block height (e.g. 510000).
                               If this field is not specified, response will 
                               include data from the latest time
           limit (int, optional): The maximum number of entries to return before
                                  the latest data point (or before to if specified).
                                  This field ranges from 1 to 100,000.
           format (str, optional): A format type about return message type. 
                                   Supported formats are json, csv

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return super().handle_request(self.EXCHANGE_FLOWS, query_params)