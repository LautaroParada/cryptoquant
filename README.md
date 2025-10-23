# CryptoQuant SDK

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://shields.io/)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)

---

# Contents

1. [General Description](#general-description-arrow_up)
2. [Requirements](#requirements-arrow_up)
3. [Installation](#installation-arrow_up)
4. [Demo](#demo-arrow_up)
	- [REST API](#rest-api-arrow_up)
5. [Documentation](#documentation-arrow_up)
	- [Available Endpoints](#available-edpoints-arrow_up)
	- [Bitcoin](#bitcoin-arrow_up)
		- [Entity Status](#entity-status-arrow_up)
		- [Exchange Flows](#exchange-flows-arrow_up)
6. [Disclaimer](#disclaimer-arrow_up)

---

## General Description [:arrow_up:](#cryptoquant-sdk)

This SDK is the **unofficial Python client** 🐍 for the [CryptoQuant REST API](https://cryptoquant.com/).  
It provides a unified interface to query all available metrics (including on-chain data, market flows, exchange reserves, and stablecoin analytics) through a consistent, auditable structure.

---

## Requirements [:arrow_up:](#cryptoquant-sdk)

- You need to **request an API key** from [CryptoQuant](https://cryptoquant.com/).
- Compatible with:
  - Python `>=3.8`

---

## Installation [:arrow_up:](#cryptoquant-sdk)

```python
pip install cryptoquant
```
---

## Demo [:arrow_up:](#cryptoquant-sdk)

### REST API [:arrow_up:](#cryptoquant-sdk)

Basic usage example: Initialize the client and retrieve the list of available API endpoints.

```python
# Import the main SDK class.
# This class unifies all API modules (Bitcoin, Ethereum, Stablecoins, etc.)
# and provides a single interface to interact with the CryptoQuant REST API.
from cryptoquant import CryptoQuant

# Import the 'os' module to access environment variables.
# It's considered best practice to store API keys outside of source code.
import os

# Load your CryptoQuant API key from an environment variable.
api_key = os.environ['CQ_API']

# Create an instance of the main SDK client,
# passing the API key for authentication.
# This automatically initializes all internal submodules and request handlers.
client = CryptoQuant(api_key)

# Make a request to the discovery endpoint.
# This method queries the API and returns a list of all available endpoints
# along with their optional and required parameters.
resp = client.get_endpoints()

```

It's highly recommendable to save your API keys in the environment variable. A short tutorial can be founded in the [following video](https://www.youtube.com/watch?v=IolxqkL7cD8):

[![Demo enviroment variables](https://j.gifs.com/LZlj1D.gif)](https://www.youtube.com/watch?v=IolxqkL7cD8)

---

## Documentation [:arrow_up:](#cryptoquant-sdk)
Please be aware that some descriptions will come directly from the API's documentation because no further explanations were needed for the specific method. Additionally, for the sake of simplicity, I will use the following convention along with the whole document:

```python
from cryptoquant import CryptoQuant
# create the instance of the SDK
api_key = os.environ['CQ_API']
client = CryptoQuant(api_key)
```

### Available Endpoints [:arrow_up:](#cryptoquant-sdk)
- **Endpoints**: Discover all available endpoints.
	- Parameters:
		- ```format_```(str): Optional — Default: `json`. Defines the response format. Supported formats: `json`, `csv`.

	- Usage:
```python
resp = client.get_endpoints()
```

### Bitcoin [:arrow_up:](#cryptoquant-sdk)

#### Entity Status [:arrow_up:](#cryptoquant-sdk)
- **Entities**: Returns the list of Bitcoin-related entities, such as exchanges, banks, and miners.  
	- Parameters:  
		- ```type_```(str): Required — Specifies the entity type to query.  
		  For exchange entities, the `market_type` field indicates whether the exchange operates in the **spot** or **derivatives** market.  
		  Entities without a `market_type` (e.g., miners) will return `0` for this field.  
		- ```format_```(str): Optional — Default: `json`. Defines the response format. Supported formats: `json`, `csv`.  
	- Usage:  
```python
resp = client.get_btc_exch_entity(type_="miner")
```

#### Exchange Flows [:arrow_up:](#cryptoquant-sdk)

##### Common Parameters (applies to all methods of this section)

- ```window```(str, optional): Defines the data granularity. Supported values: `day`, `hour`, `block`.  
- ```from_```(str or int, optional): Starting point of the query. Format: `YYYYMMDDTHHMMSS` (UTC).  
  - If `window=day`, format can be `YYYYMMDD`.  
  - If `window=block`, can specify block height (e.g., `510000`).  
  - Defaults to earliest available timestamp.  
- ```to_```(str or int, optional): Ending point of the query. Format: `YYYYMMDDTHHMMSS` (UTC).  
  - If `window=day`, format can be `YYYYMMDD`.  
  - If `window=block`, can specify block height (e.g., `510000`).  
  - Defaults to latest available timestamp.  
- ```limit```(int, optional): Maximum number of data points to return (range: 1–100,000).  
- ```format_```(str, optional): Response format. Supported values: `json` (default) or `csv`.  

- **Reserves**: Returns the total BTC reserves held on a specific exchange. This metric reflects the total balance of Bitcoin stored in wallets identified as belonging to that exchange. A decline in reserves can indicate outflows or potential accumulation by users.  

	- **Specific Parameters**  
		- ```exchange```(str): Required — Exchange name (e.g., `binance`, `coinbase`, `kraken`).

	- **Usage**  
```python
resp = client.get_btc_exch_reserve(exchange="binance")
```
- **Netflow**: Returns the net BTC flow for a specific exchange. Defined as inflow minus outflow (Inflow − Outflow = Netflow). Positive values indicate accumulation (more inflows than outflows), while negative values indicate net withdrawals (more outflows than inflows).  

    - **Specific Parameters**  
        - `exchange` (str): Required — Exchange name (e.g., `binance`, `kraken`, `coinbase`).

    - **Usage**  
```python
resp = client.get_btc_exch_netflow(exchange="kraken")
```

- **Inflow**: Returns the inflow of BTC into exchange wallets for as far back as available. The average inflow represents the average transaction value for BTC deposits into exchange wallets on a given day.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `kraken`, `coinbase`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_exch_inflow(exchange="kraken")
```

- **Outflow**: Returns the outflow of BTC from exchange wallets for as far back as available. The average outflow represents the average transaction value for BTC withdrawals from exchange wallets on a given day.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `kraken`, `coinbase`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_exch_outflow(exchange="binance")
```

- **Transactions**: Returns the number of BTC transactions between exchange wallets for the selected exchange. This endpoint provides the count of on-chain transactions associated with the exchange during the specified time window. It can be used to analyze transaction activity levels or detect unusual spikes in internal movements.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `kraken`, `coinbase`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_exch_txn(exchange="kraken")
```

- **Addresses**: Returns the number of BTC addresses involved in inflow and outflow transactions for a specific exchange. This endpoint measures the total count of unique Bitcoin addresses that interacted with the exchange during the selected period. It can be used to estimate user activity or identify changes in wallet participation over time.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `kraken`, `coinbase`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_exch_addrs(exchange="binance")
```

- **In-house Flows**: Returns the BTC transfer volume that occurred **within the same exchange**,  
  meaning movements between wallets belonging to the same exchange entity.  
  This metric reflects internal fund movements that do not represent user deposits or withdrawals.  
  It is useful for distinguishing between external flows (user-driven) and internal rebalancing operations.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `kraken`, `coinbase`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_exch_inhouseflow(exchange="kraken")
```
---

## Disclaimer [:arrow_up:](#cryptoquant-sdk)
The information in this document is provided for informational and educational purposes only. Nothing herein should be construed as financial, legal, or tax advice. The author is not a licensed financial advisor or registered investment consultant.

This SDK is not affiliated with or endorsed by CryptoQuant. It is an independent, open-source tool intended for research and data analysis.

This document does not constitute an offer to buy or sell any financial instrument. Always perform your own due diligence and consult a qualified professional before making investment decisions.