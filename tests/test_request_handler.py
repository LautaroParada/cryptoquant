from __future__ import annotations

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from cryptoquant.request_handler_class.request_handler import RequestHandler


class RequestHandlerTests(TestCase):
    """Tests for parameter normalization in ``RequestHandler``."""

    def setUp(self) -> None:
        """Prepare a reusable request handler instance."""
        self.handler = RequestHandler(api_key="test_api_key")

    def _mock_response(self) -> MagicMock:
        """Create a mock HTTP response with a JSON payload."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "ok"}
        mock_response.text = '{"status": "ok"}'
        return mock_response

    def test_handle_request_normalizes_to_param(self) -> None:
        """Ensure ``to_`` is forwarded as ``to`` and the suffix is removed."""
        with patch(
            "cryptoquant.request_handler_class.request_handler.requests.get",
            return_value=self._mock_response(),
        ) as mock_get:
            result = self.handler.handle_request(
                "dummy/endpoint",
                {"to_": "20240101"},
            )

        mock_get.assert_called_once()
        params: Dict[str, Any] = mock_get.call_args.kwargs["params"]
        self.assertEqual(params.get("to"), "20240101")
        self.assertNotIn("to_", params)
        self.assertEqual(result, {"status": "ok"})

    def test_handle_request_overrides_existing_to_param(self) -> None:
        """Ensure ``to_`` replaces any preexisting ``to`` value."""
        with patch(
            "cryptoquant.request_handler_class.request_handler.requests.get",
            return_value=self._mock_response(),
        ) as mock_get:
            self.handler.handle_request(
                "dummy/endpoint",
                {"to": "old", "to_": "20240101"},
            )

        params: Dict[str, Any] = mock_get.call_args.kwargs["params"]
        self.assertEqual(params.get("to"), "20240101")
        self.assertNotIn("to_", params)
