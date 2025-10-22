# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 11:53:22 2025

@author: lauta
"""

from cryptoquant.request_handler_class import RequestHandler

class TRX(RequestHandler):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        
        # Market data
        self.MARKET_OHLCV = "trx/market-data/price-ohlcv"
        self.MARKET_CAPITALIZATION = "trx/market-data/capitalization"
        # Network data
        self.NETWORK_SUPPLY = "trx/network-data/supply"
        
    # -----------------------------
    # Market Data
    # -----------------------------
    
    def get_trx_mkt_ohlcv(self, **query_params):
        """
        This endpoint returns metrics related to TRX's Price, Price OHLCV data 
        consists of five metrics.
        
        full documentation: https://cryptoquant.com/docs#tag/TRX-Market-Data/operation/getPriceOHLCV

        Parameters
        ----------
        **query_params : TYPE
            market (str, optional): A market type from the tbale that CQ
                                    support.
            exchange (str, optional): An exchange supported by CryptoQuant.
            symbol (str, optional): A XRP pair symbol from the table that CQ
                                    support.
            window (str, optional): day.
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
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            Price OHLCV data for trx.

        """
        return super().handle_request(self.MARKET_OHLCV, query_params)
    
    def get_trx_mkt_capitalization(self, **query_params):
        """
        CQ provide market_cap, which is total market capitalization of TRX, 
        calculated by multiplying the total supply with its USD price.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day.
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
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            Market cap in usd.

        """
        return super().handle_request(self.MARKET_CAPITALIZATION, query_params)
    
    # -----------------------------
    # Network Data
    # -----------------------------
    
    def get_trx_ntx_supply(self, **query_params):
        """
        This endpoint returns the metrics related to the supply of TRX.

        Metric	            Description
        supply_total	    The total amount of tokens in existence.
        supply_circulating	The amount of tokens that are circulating in the market.
        supply_minted	    The amount of tokens minted in the given window.
        supply_burned	    The amount of tokens burned in the given window.
        supply_staked	    The amount of tokens staked in Tron Super Representative members.

        Parameters
        ----------
        **query_params : TYPE
            window (str, optional): day.
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
                                   Supported formats are json, csv.

        Returns
        -------
        dict
            Supply statistics.

        """
        return super().handle_request(self.NETWORK_SUPPLY, query_params)