# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 18:14:29 2025

@author: lauta
"""

from __future__ import annotations
from typing import Dict, Mapping, Optional
import requests


class RequestHandler:
    """
    Clase encargada de manejar las solicitudes HTTP hacia la API de CryptoQuant.

    Esta clase centraliza la configuración del endpoint base, encabezados de autenticación
    y la lógica para formatear los parámetros y procesar las respuestas.
    Permite obtener resultados tanto en formato JSON como CSV (texto plano).

    """

    def __init__(self, api_key: str):
        """
        Inicializa el manejador con la clave API de autenticación.

        Parameters
        ----------
        api_key : str
            Token de acceso personal proporcionado por CryptoQuant.
        """
        self.API_KEY_ = api_key
        self.resp: Optional[requests.Response] = None
        self.HEADERS_: Dict[str, str] = {"Authorization": "Bearer " + self.API_KEY_}
        self.HOST_: str = "https://api.cryptoquant.com/v1/"

    # ---------------------------------------------------------------------
    # Métodos internos (uso privado)
    # ---------------------------------------------------------------------

    def __append_fmt(self, dict_to_append: Optional[Mapping[str, str]]) -> Dict[str, str]:
        """
        Normaliza las claves de un diccionario de parámetros de consulta (`query_params`).

        Este método:
        - Elimina nombres reservados conflictivos (`from`, `type`, `filter`, `format`).
        - Reemplaza las claves con sufijo "_" (ej. `from_`) por su versión correcta
          para ajustarse a los parámetros esperados por la API.

        Parameters
        ----------
        dict_to_append : Mapping[str, str] or None
            Diccionario original de parámetros a normalizar.

        Returns
        -------
        dict
            Diccionario con las claves normalizadas, apto para ser enviado en la query.
        """
        normalized_params: Dict[str, str] = {}
        if dict_to_append:
            normalized_params.update(dict_to_append)

        # Eliminar nombres reservados para evitar colisiones
        for reserved in ("from", "type", "filter", "format"):
            normalized_params.pop(reserved, None)

        # Mapear variantes con sufijo "_"
        replacements = {
            "from_": "from",
            "type_": "type",
            "filter_": "filter",
            "format_": "format",
        }

        for current_key, target_key in replacements.items():
            if current_key in normalized_params:
                normalized_params[target_key] = normalized_params.pop(current_key)

        return normalized_params

    def __url_api(self, url_to_append: str) -> str:
        """
        Construye la URL completa para una solicitud específica de la API.

        Parameters
        ----------
        url_to_append : str
            Ruta parcial del recurso o endpoint dentro de la API.

        Returns
        -------
        str
            URL completa lista para ser usada en la llamada HTTP.
        """
        return self.HOST_ + url_to_append

    # ---------------------------------------------------------------------
    # Métodos públicos
    # ---------------------------------------------------------------------

    def handle_request(
        self,
        endpoint_url: str,
        query_params: Optional[Mapping[str, str]] = None,
    ):
        """
        Envía una solicitud GET a la API de CryptoQuant y maneja la respuesta.

        Según el valor del parámetro `format`, la respuesta se interpreta como:
        - `format='csv'`: Devuelve el cuerpo en texto plano CSV.
        - Por defecto: Devuelve un objeto JSON (tipo `dict`).
        Si el contenido no es JSON válido, devuelve el texto crudo.

        Parameters
        ----------
        endpoint_url : str
            Ruta relativa del endpoint (por ejemplo, `"btc/network/hashrate"`).
        query_params : Mapping[str, str], optional
            Parámetros de consulta (`window`, `interval`, `format_`, etc.).
            Las claves con sufijo `_` se normalizan automáticamente.

        Returns
        -------
        dict or str
            Objeto JSON (si `format` no es `'csv'`) o texto CSV (si `format='csv'`).

        Raises
        ------
        requests.HTTPError
            Si la API devuelve un código de estado diferente de 200.

        """
        # Construir URL completa
        endpoint_url_ = self.__url_api(endpoint_url)

        # Normalizar parámetros
        query_params_ = self.__append_fmt(query_params)

        # Realizar la solicitud HTTP
        self.resp = requests.get(
            url=endpoint_url_,
            headers=self.HEADERS_,
            params=query_params_,
        )

        # Evaluar la respuesta
        if self.resp.status_code == 200:
            fmt = query_params_.get("format", "").lower()

            # Si se solicitó CSV → devolver texto plano
            if fmt == "csv":
                return self.resp.text

            # Intentar decodificar JSON
            try:
                return self.resp.json()
            except ValueError:
                # Si no es JSON válido, devolver texto crudo
                return self.resp.text

        # Si la respuesta no fue exitosa → lanzar excepción
        self.resp.raise_for_status()
