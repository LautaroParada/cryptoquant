#!/usr/bin/env python3
"""
Simple demonstration of intraday data support in CryptoQuant SDK.

This script shows the key improvements made to support hourly data queries.
"""

# Import helper methods for timestamp formatting
from cryptoquant.request_handler_class import RequestHandler

# Import datetime utilities
from datetime import datetime

print("=" * 70)
print("CryptoQuant SDK - Intraday Data Support Demonstration")
print("=" * 70)

# Create a handler instance (no API key needed for validation demos)
handler = RequestHandler('demo_key')

print("\n1. TIMESTAMP VALIDATION")
print("-" * 70)

test_cases = [
    # (timestamp, window, description)
    ('20240101T120000', 'hour', 'Valid hourly timestamp'),
    ('20240101', 'hour', 'Invalid: missing time for hourly'),
    ('20240101', 'day', 'Valid daily timestamp (date only)'),
    ('20240101T120000', 'day', 'Valid daily timestamp (with time)'),
]

for timestamp, window, description in test_cases:
    is_valid = handler.validate_timestamp(timestamp, window)
    status = "✓" if is_valid else "✗"
    print(f"{status} {description}")
    print(f"  timestamp='{timestamp}', window='{window}'")

print("\n2. TIMESTAMP FORMATTING")
print("-" * 70)

# Test formatting from datetime objects
dt = datetime(2024, 1, 15, 14, 30, 0)

hourly_format = handler.format_timestamp_for_window(dt, 'hour')
daily_format = handler.format_timestamp_for_window(dt, 'day')

print(f"Input datetime: {dt}")
print(f"  For hourly queries: '{hourly_format}'")
print(f"  For daily queries:  '{daily_format}'")

print("\n3. AUTOMATIC VALIDATION IN REQUESTS")
print("-" * 70)

print("✓ Valid hourly query parameters:")
valid_params = {
    'window': 'hour',
    'from_': '20240101T000000',
    'to_': '20240101T120000',
    'exchange': 'binance'
}
normalized = handler._RequestHandler__append_fmt(valid_params)
print(f"  Input:  {valid_params}")
print(f"  Output: {normalized}")

print("\n✗ Invalid hourly query parameters (missing time):")
invalid_params = {
    'window': 'hour',
    'from_': '20240101',  # Missing time
    'to_': '20240101',    # Missing time
    'exchange': 'binance'
}
try:
    normalized = handler._RequestHandler__append_fmt(invalid_params)
    print("  ERROR: Should have raised ValueError!")
except ValueError as e:
    print(f"  Validation error caught: {str(e)[:80]}...")

print("\n4. KEY FEATURES SUMMARY")
print("-" * 70)
print("✓ Automatic timestamp validation for window='hour'")
print("✓ Clear error messages when timestamps are incorrect")
print("✓ Helper methods for formatting timestamps")
print("✓ Backward compatible with existing daily queries")
print("✓ Support for both JSON and CSV formats")

print("\n" + "=" * 70)
print("Demonstration complete!")
print("=" * 70)
print("\nTo use intraday data in your code:")
print("  1. Set window='hour'")
print("  2. Use YYYYMMDDTHHMMSS format for timestamps")
print("  3. Use helper methods for formatting datetime objects")
print("\nSee examples/intraday_data_example.py for complete examples.")
print()
