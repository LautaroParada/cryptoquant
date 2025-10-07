# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 18:14:29 2025

@author: lauta
"""

from __future__ import annotations
from typing import Dict, Mapping, Optional
import requests

class RequestHandler:
    def __init__(self, api_key: str):
        # parametros generales de la API
        
        self.API_KEY_ = api_key
        self.resp = None
        self.HEADERS_ = {'Authorization': 'Bearer ' + self.API_KEY_}
        self.HOST_ = "https://api.cryptoquant.com/v1/"
        
    # ---------------------------------------
    # Metodos para procesar las llamadas de datos
    # ---------------------------------------
    
    def __append_fmt(
            self, 
            dict_to_append: Optional[Mapping[str, str]]
            ) -> Dict[str, str]:
        
        """
        """
        
        # actualizar el diccionario de parametros en base a los solicitados
        # por el usuario
        normalized_params: Dict[str, str] = {}
        if dict_to_append:
            normalized_params.update(dict_to_append)

        for reserved in ('from', 'type', 'filter', 'format'):
            normalized_params.pop(reserved, None)

        replacements = {
            'from_': 'from',
            'type_': 'type',
            'filter_': 'filter',
            'format_': 'format',
        }
        
        for current_key, target_key in replacements.items():
            if current_key in normalized_params:
                normalized_params[target_key] = normalized_params.pop(current_key)

        return normalized_params
    
    def __url_api(self, url_to_append: str):
        """
        Adjunta al host base la url de los datos a llamar a la API

        Parameters
        ----------
        url_to_append : str
            url especifica del activo a llamar.

        Returns
        -------
        url completa para solicitar a la API.

        """
        url_to_call = self.HOST_ + url_to_append
        return url_to_call
    
    def handle_request(
            self,
            endpoint_url: str,
            query_params: Optional[Mapping[str, str]] = None,
            ):
        
        """
        Metodo central para majenar las solicitudes a la API.
        Ya sea para exitosas (200) o fallidas (400, 500)
        
        Parametros
        ----------
        
        
        Retorno
        ----------
        
        """
        # Modificar el HOST al cual se le pedira datos
        endpoint_url_ = self.__url_api(
            endpoint_url
            )
        
        # Formato de los parametros
        query_params_ = self.__append_fmt(
            query_params
            )
        
        self.resp = requests.get(
            url = endpoint_url_,
            headers = self.HEADERS_,
            params = query_params_
            )
        
        # Determinar la respuesta del servidor
        if self.resp.status_code == 200:
            return self.resp.json()
        else:
            self.resp.raise_for_status()
    