"""
Example: Using CryptoQuant SDK for Intraday (Hourly) Data Queries

This example demonstrates how to fetch intraday data from the CryptoQuant API
using the enhanced SDK with proper timestamp formatting for hourly data.

The SDK now includes:
1. Automatic validation of timestamps for intraday queries
2. Helper methods to format timestamps correctly
3. Clear error messages when timestamps are improperly formatted
"""

import os
from datetime import datetime, timedelta
from cryptoquant import CryptoQuant
from cryptoquant.request_handler_class import RequestHandler

# Load API key from environment variable
api_key = os.environ.get('CQ_API', 'your_api_key_here')

# Initialize the CryptoQuant client
client = CryptoQuant(api_key)

print("=" * 70)
print("CryptoQuant SDK - Intraday Data Examples")
print("=" * 70)

# ============================================================================
# Example 1: Fetching hourly BTC exchange reserves
# ============================================================================
print("\n[Example 1] Fetching hourly BTC exchange reserves for Binance")
print("-" * 70)

try:
    # Define the time range for intraday data
    # For window='hour', timestamps MUST include time: YYYYMMDDTHHMMSS
    response = client.get_btc_exch_reserve(
        exchange='binance',
        window='hour',
        from_='20240101T000000',  # January 1, 2024 at 00:00:00
        to_='20240101T235959',    # January 1, 2024 at 23:59:59
        limit=24
    )
    
    print(f"✓ Successfully fetched {len(response.get('result', {}).get('data', []))} hourly data points")
    print(f"Response keys: {list(response.keys())}")
    
except ValueError as e:
    print(f"✗ Validation error: {e}")
except Exception as e:
    print(f"✗ API error: {e}")

# ============================================================================
# Example 2: Fetching hourly BTC netflows with proper timestamp formatting
# ============================================================================
print("\n[Example 2] Fetching hourly BTC netflows with timestamp helper")
print("-" * 70)

try:
    # Use the helper method to format timestamps from datetime objects
    start_time = datetime(2024, 1, 15, 0, 0, 0)
    end_time = datetime(2024, 1, 15, 12, 0, 0)
    
    # Format timestamps for hourly window
    from_ts = RequestHandler.format_timestamp_for_window(start_time, 'hour')
    to_ts = RequestHandler.format_timestamp_for_window(end_time, 'hour')
    
    print(f"Formatted timestamps: from={from_ts}, to={to_ts}")
    
    response = client.get_btc_exch_netflow(
        exchange='kraken',
        window='hour',
        from_=from_ts,
        to_=to_ts,
        limit=12
    )
    
    print(f"✓ Successfully fetched hourly netflow data")
    
except ValueError as e:
    print(f"✗ Validation error: {e}")
except Exception as e:
    print(f"✗ API error: {e}")

# ============================================================================
# Example 3: Daily data still works as before (backward compatible)
# ============================================================================
print("\n[Example 3] Fetching daily BTC exchange reserves (backward compatible)")
print("-" * 70)

try:
    # For window='day', both YYYYMMDD and YYYYMMDDTHHMMSS formats work
    response = client.get_btc_exch_reserve(
        exchange='binance',
        window='day',
        from_='20240101',    # Date-only format works for daily
        to_='20240131',
        limit=31
    )
    
    print(f"✓ Successfully fetched {len(response.get('result', {}).get('data', []))} daily data points")
    
except Exception as e:
    print(f"✗ Error: {e}")

# ============================================================================
# Example 4: Error handling - Missing time component for hourly data
# ============================================================================
print("\n[Example 4] Error handling - Incorrect timestamp format for hourly data")
print("-" * 70)

try:
    # This will raise a ValueError because window='hour' requires time component
    response = client.get_btc_exch_reserve(
        exchange='binance',
        window='hour',
        from_='20240101',      # ✗ Missing time - will fail validation
        to_='20240101',        # ✗ Missing time - will fail validation
    )
    
    print("✗ Should have raised a validation error!")
    
except ValueError as e:
    print(f"✓ Validation error caught as expected:")
    print(f"  {e}")

# ============================================================================
# Example 5: Fetching multiple metrics with hourly granularity
# ============================================================================
print("\n[Example 5] Fetching multiple hourly metrics")
print("-" * 70)

try:
    # Define common parameters
    params = {
        'exchange': 'binance',
        'window': 'hour',
        'from_': '20240115T000000',
        'to_': '20240115T120000',
        'limit': 12
    }
    
    # Fetch multiple metrics
    print("Fetching hourly data for:")
    
    # Reserve
    print("  - Exchange reserves...", end=" ")
    reserves = client.get_btc_exch_reserve(**params)
    print("✓")
    
    # Inflow
    print("  - Exchange inflows...", end=" ")
    inflows = client.get_btc_exch_inflow(**params)
    print("✓")
    
    # Outflow
    print("  - Exchange outflows...", end=" ")
    outflows = client.get_btc_exch_outflow(**params)
    print("✓")
    
    print(f"\n✓ Successfully fetched all hourly metrics")
    
except Exception as e:
    print(f"\n✗ Error: {e}")

# ============================================================================
# Example 6: CSV format for hourly data
# ============================================================================
print("\n[Example 6] Fetching hourly data in CSV format")
print("-" * 70)

try:
    response = client.get_btc_exch_reserve(
        exchange='coinbase',
        window='hour',
        from_='20240101T000000',
        to_='20240101T060000',
        limit=6,
        format_='csv'
    )
    
    # Response will be CSV text
    if isinstance(response, str):
        print("✓ Successfully fetched CSV data:")
        lines = response.split('\n')[:5]  # Show first 5 lines
        for line in lines:
            print(f"  {line}")
        print(f"  ... ({len(response.split('\n'))} total lines)")
    
except Exception as e:
    print(f"✗ Error: {e}")

# ============================================================================
# Example 7: Using timestamp validation before making requests
# ============================================================================
print("\n[Example 7] Pre-validating timestamps before making API calls")
print("-" * 70)

timestamps_to_test = [
    ('20240101', 'hour'),
    ('20240101T120000', 'hour'),
    ('20240101', 'day'),
    ('20240101T120000', 'day'),
]

for timestamp, window in timestamps_to_test:
    is_valid = RequestHandler.validate_timestamp(timestamp, window)
    status = "✓ Valid" if is_valid else "✗ Invalid"
    print(f"{status}: timestamp='{timestamp}' for window='{window}'")

print("\n" + "=" * 70)
print("Examples completed!")
print("=" * 70)

# ============================================================================
# Tips for using intraday data:
# ============================================================================
print("\n📝 Tips for using intraday (hourly) data:\n")
print("1. Always use window='hour' for intraday queries")
print("2. Timestamps must be in YYYYMMDDTHHMMSS format (e.g., '20240101T120000')")
print("3. Use RequestHandler.format_timestamp_for_window() to format datetime objects")
print("4. Use RequestHandler.validate_timestamp() to pre-validate timestamps")
print("5. The SDK will automatically validate and provide helpful error messages")
print("6. Daily data (window='day') still works with YYYYMMDD format for backward compatibility")
print()
