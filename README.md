# CryptoQuant Python SDK

Unofficial Python SDK for the [CryptoQuant API](https://docs.cryptoquant.com) — unified access to on-chain and market data for Bitcoin, Ethereum, Stablecoins, ERC-20 tokens, XRP, TRX, and Altcoins.

![CI](https://github.com/LautaroParada/cryptoquant/actions/workflows/ci.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/cryptoquant.svg)](https://badge.fury.io/py/cryptoquant)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Installation

```bash
pip install cryptoquant
```

## Quick Start

```python
from cryptoquant import CryptoQuant

client = CryptoQuant(api_key="your_api_key")

# Stablecoin exchange flows
data = client.get_stable_exch_inflow(
    token="usdc",
    exchange="all_exchange",
    window="day",
    limit=30,
)
```

## Error Handling

```python
from cryptoquant import (
    CryptoQuant,
    CryptoQuantHTTPError,
    CryptoQuantTimeoutError,
    CryptoQuantConnectionError,
)

try:
    data = client.get_stable_exch_inflow(token="usdc", exchange="binance", window="hour")
except CryptoQuantHTTPError as e:
    print(f"API error {e.status_code}: {e}")
except CryptoQuantTimeoutError:
    print("Request timed out")
except CryptoQuantConnectionError:
    print("Network error")
```

## Supported Assets

| Asset | Module | Categories |
|---|---|---|
| Bitcoin | `Bitcoin` | Exchange flows, miner flows, network/market indicators, mempool, Lightning |
| Ethereum | `Ethereum` | Exchange flows, ETH 2.0, fund data, market/network data |
| Stablecoins | `StableCoins` | Exchange flows, flow indicators, market data, network data |
| ERC-20 | `Erc20` | Exchange flows, flow indicators, market/network data |
| XRP | `XRP` | Entity flows, DEX/AMM data, market/network data |
| TRX | `TRX` | Market data, network data, DeFi |
| Altcoins | `AltCoins` | Market data (OHLCV) |

## Time Windows

CryptoQuant supports four time windows. Each endpoint supports a subset:

| Window | Description | `from_`/`to_` format |
|---|---|---|
| `day` | Daily aggregation | `YYYYMMDD` or `YYYYMMDDTHHMMSS` |
| `hour` | Hourly aggregation | `YYYYMMDDTHHMMSS` |
| `min` | Per-minute (market data only) | `YYYYMMDDTHHMMSS` |
| `block` | Per-block (on-chain data) | `YYYYMMDDTHHMMSS` or block height integer |

## API Versions

The SDK transparently routes requests to the correct API version:
- Endpoints starting with `v2/` → `https://api.cryptoquant.com/v2/`
- All other endpoints → `https://api.cryptoquant.com/v1/`

No configuration needed.

## Advanced Usage

### Custom timeout

```python
client = CryptoQuant(api_key="...", default_timeout=60.0)
```

### Incremental fetch with from_/to_

```python
data = client.get_stable_exch_inflow(
    token="usdt_eth",
    exchange="binance",
    window="hour",
    from_="20240101T000000",
    to_="20240101T235959",
)
```

### CSV output

```python
csv_data = client.get_stable_exch_reserve(
    token="usdc",
    exchange="all_exchange",
    window="day",
    format_="csv",
)
```

## Development

```bash
git clone https://github.com/LautaroParada/cryptoquant.git
cd cryptoquant
pip install -e ".[dev]"
pytest tests/ -v
```

## License

MIT