from __future__ import annotations

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock

import requests

from cryptoquant.request_handler_class.request_handler import RequestHandler
from cryptoquant.exceptions import (
    CryptoQuantHTTPError,
    CryptoQuantTimeoutError,
    CryptoQuantConnectionError,
)


class RequestHandlerTests(TestCase):
    """Tests for parameter normalization in ``RequestHandler``."""

    def setUp(self) -> None:
        """Prepare a reusable request handler instance."""
        self.session = MagicMock(spec=requests.Session)
        self.handler = RequestHandler(
            api_key="test_api_key",
            session=self.session,
            default_timeout=5.0,
        )

    def _mock_response(self, status_code: int = 200) -> MagicMock:
        """Create a mock HTTP response with a JSON payload."""
        mock_response = MagicMock()
        mock_response.status_code = status_code
        mock_response.json.return_value = {"status": "ok"}
        mock_response.text = '{"status": "ok"}'
        mock_response.raise_for_status = MagicMock()
        return mock_response

    def test_handle_request_normalizes_to_param(self) -> None:
        """Ensure ``to_`` is forwarded as ``to`` and the suffix is removed."""
        self.session.get.return_value = self._mock_response()

        result = self.handler.handle_request(
            "dummy/endpoint",
            {"to_": "20240101"},
        )

        self.session.get.assert_called_once()
        params: Dict[str, Any] = self.session.get.call_args.kwargs["params"]
        self.assertEqual(params.get("to"), "20240101")
        self.assertNotIn("to_", params)
        self.assertEqual(result, {"status": "ok"})
        self.assertEqual(self.session.get.call_args.kwargs["headers"], self.handler.HEADERS_)
        self.assertEqual(self.session.get.call_args.kwargs["timeout"], 5.0)

    def test_handle_request_overrides_existing_to_param(self) -> None:
        """Ensure ``to_`` replaces any preexisting ``to`` value."""
        self.session.get.return_value = self._mock_response()

        self.handler.handle_request(
            "dummy/endpoint",
            {"to": "old", "to_": "20240101"},
            timeout=2.5,
        )

        params: Dict[str, Any] = self.session.get.call_args.kwargs["params"]
        self.assertEqual(params.get("to"), "20240101")
        self.assertNotIn("to_", params)
        self.assertEqual(self.session.get.call_args.kwargs["timeout"], 2.5)

    def test_http_error_raises_cryptoquant_http_error(self) -> None:
        """CryptoQuantHTTPError is raised for non-2xx responses."""
        mock_resp = MagicMock()
        mock_resp.status_code = 403
        http_exc = requests.exceptions.HTTPError(response=mock_resp)
        mock_resp.raise_for_status.side_effect = http_exc
        self.session.get.return_value = mock_resp

        with self.assertRaises(CryptoQuantHTTPError) as ctx:
            self.handler.handle_request("dummy/endpoint")

        self.assertEqual(ctx.exception.status_code, 403)
        self.assertIs(ctx.exception.response, mock_resp)

    def test_timeout_raises_cryptoquant_timeout_error(self) -> None:
        """CryptoQuantTimeoutError is raised on requests.Timeout."""
        self.session.get.side_effect = requests.exceptions.Timeout()

        with self.assertRaises(CryptoQuantTimeoutError):
            self.handler.handle_request("dummy/endpoint")

    def test_connection_error_raises_cryptoquant_connection_error(self) -> None:
        """CryptoQuantConnectionError is raised on requests.ConnectionError."""
        self.session.get.side_effect = requests.exceptions.ConnectionError()

        with self.assertRaises(CryptoQuantConnectionError):
            self.handler.handle_request("dummy/endpoint")

    def test_v2_endpoint_uses_v2_base_url(self) -> None:
        """Endpoints starting with 'v2/' are routed to the v2 base URL."""
        self.session.get.return_value = self._mock_response()

        self.handler.handle_request("v2/some/endpoint")

        call_url = self.session.get.call_args.kwargs["url"]
        self.assertTrue(call_url.startswith("https://api.cryptoquant.com/v2/"))
        self.assertIn("some/endpoint", call_url)
        self.assertNotIn("v2/v2", call_url)

    def test_v1_endpoint_uses_v1_base_url(self) -> None:
        """Normal endpoints are routed to the v1 base URL."""
        self.session.get.return_value = self._mock_response()

        self.handler.handle_request("btc/exchange-flows/reserve")

        call_url = self.session.get.call_args.kwargs["url"]
        self.assertTrue(call_url.startswith("https://api.cryptoquant.com/v1/"))

