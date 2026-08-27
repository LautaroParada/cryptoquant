class CryptoQuantError(Exception):
    """Base exception for all CryptoQuant SDK errors."""


class CryptoQuantHTTPError(CryptoQuantError):
    """Raised when the API returns a non-2xx HTTP status code."""

    def __init__(self, message: str, status_code: int, response=None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response


class CryptoQuantConnectionError(CryptoQuantError):
    """Raised when a network connection error occurs."""


class CryptoQuantTimeoutError(CryptoQuantError):
    """Raised when a request times out."""


class CryptoQuantValidationError(CryptoQuantError):
    """Raised when input parameters fail validation before the request is sent."""
