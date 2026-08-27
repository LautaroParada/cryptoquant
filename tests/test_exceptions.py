"""Tests for the CryptoQuant SDK exception hierarchy."""

from __future__ import annotations

from unittest import TestCase

import cryptoquant
from cryptoquant.exceptions import (
    CryptoQuantError,
    CryptoQuantHTTPError,
    CryptoQuantConnectionError,
    CryptoQuantTimeoutError,
    CryptoQuantValidationError,
)


class ExceptionHierarchyTests(TestCase):
    """Tests for exception class relationships."""

    def test_http_error_is_subclass_of_base(self) -> None:
        exc = CryptoQuantHTTPError("msg", status_code=404)
        self.assertIsInstance(exc, CryptoQuantError)

    def test_connection_error_is_subclass_of_base(self) -> None:
        exc = CryptoQuantConnectionError("msg")
        self.assertIsInstance(exc, CryptoQuantError)

    def test_timeout_error_is_subclass_of_base(self) -> None:
        exc = CryptoQuantTimeoutError("msg")
        self.assertIsInstance(exc, CryptoQuantError)

    def test_validation_error_is_subclass_of_base(self) -> None:
        exc = CryptoQuantValidationError("msg")
        self.assertIsInstance(exc, CryptoQuantError)

    def test_base_error_is_subclass_of_exception(self) -> None:
        exc = CryptoQuantError("msg")
        self.assertIsInstance(exc, Exception)


class HTTPErrorAttributesTests(TestCase):
    """Tests for CryptoQuantHTTPError attributes."""

    def test_status_code_accessible(self) -> None:
        exc = CryptoQuantHTTPError("Not Found", status_code=404)
        self.assertEqual(exc.status_code, 404)

    def test_response_accessible(self) -> None:
        mock_resp = object()
        exc = CryptoQuantHTTPError("Forbidden", status_code=403, response=mock_resp)
        self.assertIs(exc.response, mock_resp)

    def test_response_defaults_to_none(self) -> None:
        exc = CryptoQuantHTTPError("Server Error", status_code=500)
        self.assertIsNone(exc.response)

    def test_message_preserved(self) -> None:
        exc = CryptoQuantHTTPError("Rate limited", status_code=429)
        self.assertEqual(str(exc), "Rate limited")


class PublicImportTests(TestCase):
    """Tests that all exceptions are importable from the top-level package."""

    def test_all_exceptions_importable_from_cryptoquant(self) -> None:
        self.assertTrue(hasattr(cryptoquant, "CryptoQuantError"))
        self.assertTrue(hasattr(cryptoquant, "CryptoQuantHTTPError"))
        self.assertTrue(hasattr(cryptoquant, "CryptoQuantConnectionError"))
        self.assertTrue(hasattr(cryptoquant, "CryptoQuantTimeoutError"))
        self.assertTrue(hasattr(cryptoquant, "CryptoQuantValidationError"))

    def test_imported_classes_are_correct(self) -> None:
        self.assertIs(cryptoquant.CryptoQuantHTTPError, CryptoQuantHTTPError)
        self.assertIs(cryptoquant.CryptoQuantError, CryptoQuantError)
