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
        - [Flow Indicators](#flow-indicators-arrow_up)
        - [Market Indicators](#market-indicators-arrow_up)
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

#### Flow Indicators [:arrow_up:](#cryptoquant-sdk)

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


- **Miners’ Position Index (MPI)**: Returns the **Miner’s Position Index**, a ratio that compares the total amount of BTC moved by miners to its historical average. This indicator helps assess **selling pressure from miners** — higher values suggest that miners are transferring more BTC than usual to exchanges (potential sell-side activity), while lower values imply accumulation or reduced selling.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `kraken`, `coinbase`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
  ```python
  resp = client.get_btc_idx_mpi(exchange='kraken', window="day", limit=365)
  ```

- **Exchange Shutdown Indicator**: Detects anomalous on-chain flow patterns that typically precede or coincide with an exchange hack or operational halt. This metric identifies the characteristic sequence where massive outflows are followed by a sudden drop to zero**, signaling that an exchange has likely paused withdrawals or frozen wallets due to a security breach or critical issue. It serves as an early-warning signal of potential exchange-related riskand liquidity disruptions.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `kraken`, `coinbase`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
  resp = client.get_btc_idx_exchshutdown(exchange="binance", window="day", limit=90)
```

- **Exchange Whale Ratio (EWR)**: Measures the ratio of the top 10 inflow transactions to the total inflow volume on a given exchange. A high value indicates that large holders (“whales”) are depositing a significant share of total inflows, which may suggest increased selling pressure or distribution activity. Conversely, a lower value implies more balanced inflows across users, often associated with accumulation or stable market conditions.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `kraken`, `coinbase`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
  resp = client.get_btc_idx_whale(exchange="kraken", window="day", limit=365)
```

- **Fund Flow Ratio (FFR)**: Measures the ratio of BTC transferred to exchange wallets relative to the total BTC moved on-chain.  
  This indicator quantifies how much of the overall Bitcoin network activity is directed toward exchanges. A high Fund Flow Ratio means that a larger share of BTC transactions involve exchanges — often associated with increased trading activity or potential sell pressure. Conversely, a low ratio indicates that fewer BTC are being sent to exchanges, suggesting reduced trading activity or accumulation behavior.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `kraken`, `coinbase`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
  resp = client.get_btc_idx_fundflow(exchange="binance", window="day", limit=180)
```

- **Stablecoin Ratio (SR)**: Represents the ratio between an exchange’s BTC reserve and its total stablecoin reserve. This indicator reflects the relative balance between Bitcoin held and stablecoins available for trading. A high Stablecoin Ratio (more BTC relative to stablecoins) suggests potential sell pressure, while a low ratio (more stablecoins relative to BTC) indicates buying capacity or accumulation potential. Only exchanges with both BTC and at least one supported stablecoin are included in this metric.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `kraken`, `coinbase`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
  resp = client.get_btc_idx_stableratio(exchange="binance", window="day", limit=365)
```

- **Exchange Inflow Age Distribution**: Represents the distribution of Bitcoin inflows to exchanges categorized by the age of the coins being moved. This indicator provides insight into the behavior of long-term versus short-term holders sending BTC to exchanges. It helps identify whether older, dormant coins are entering circulation (a potential sign of selling from long-term holders) or if inflows are dominated by newer coins, which typically indicates routine trading activity. Values are provided both in native units and as percentages of total inflow volume.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `kraken`, `coinbase`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
  resp = client.get_btc_idx_agedistr(exchange="binance", window="day", limit=180)
```

- **Exchange Inflow Supply Distribution**: Represents the distribution of Bitcoin inflows to exchanges segmented by wallet balance tiers. This indicator helps identify whether inflows are dominated by large holders (whales) or smaller retail participants. By analyzing the amount of BTC held by entities sending coins to exchanges, it provides insight into market composition and potential shifts in dominance between large and small holders. Values are presented both in native BTC units and as percentages of total inflow volume.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `kraken`, `coinbase`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
  resp = client.get_btc_idx_supplydstr(exchange="kraken", window="day", limit=180)
```

- **Exchange Inflow CDD (Coin Days Destroyed)**: Represents the portion of Coin Days Destroyed (CDD) specifically attributed to coins flowing into exchanges. This indicator filters out general network noise to focus on movements that may signal selling activity. Higher values indicate that older coins, which have been held for longer periods, are being sent to exchanges—often interpreted as a potential increase in sell-side pressure. It serves as a refined version of traditional CDD tailored to detect exchange-related dumping behavior.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `kraken`, `coinbase`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
  resp = client.get_btc_idx_cdd(exchange="binance", window="day", limit=365)
```

- **Exchange Supply Ratio (ESR)**: Calculated as the ratio of Bitcoin held in exchange reserves to the total circulating supply. This indicator measures the proportion of total BTC supply stored on exchanges, providing insight into the potential liquidity and sell pressure in the market. A rising Exchange Supply Ratio suggests that more coins are being held on exchanges, often linked to increased readiness to sell or trade. Conversely, a declining ratio indicates that coins are being withdrawn to self-custody, typically interpreted as accumulation behavior.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `kraken`, `coinbase`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
  resp = client.get_btc_idx_exchsupplyratio(exchange="kraken", window="day", limit=365)
```

- **Miner Supply Ratio (MSR)**: Calculated as the ratio of Bitcoin held in miner reserves to the total circulating supply. This indicator measures the share of total BTC supply controlled by miners, offering insight into miner behavior and its potential impact on market dynamics. A higher Miner Supply Ratio indicates that miners are holding a larger portion of the total supply, often associated with accumulation or reduced selling activity. A lower ratio suggests that miners are reducing their holdings, which can imply increased selling pressure or liquidity injections into the market.

    - **Specific Parameters**  
        - ```miner```(str): Optional — Miner name (e.g., `f2pool`, `antpool`, `foundry`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
  resp = client.get_btc_idx_minersupplyratio(miner="f2pool", window="day", limit=365)
```

#### Market Indicators [:arrow_up:](#cryptoquant-sdk)

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


- **Estimated Leverage Ratio (ELR)**: Calculated by dividing an exchange’s open interest by its BTC reserve, this metric estimates the average leverage used by traders on that exchange. When the leverage ratio reaches elevated levels, the market tends to experience rapid volatility due to liquidations and over-leveraged positions. Unlike simple open interest, the Estimated Leverage Ratio accounts for the exchange’s BTC reserve size, providing a more accurate view of risk exposure and market sentiment. It helps assess how aggressive or conservative traders are in their positioning. Historical data may change over time as new exchange wallet addresses are identified and validated.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `bybit`, `bitmex`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
  ```python
  resp = client.get_btc_mkt_leverage(exchange="binance", window="day", limit=365)
  ```

- **Stablecoin Supply Ratio (SSR)**: Represents the ratio between Bitcoin’s market capitalization and the total supply of stablecoins. Since stablecoins act as a proxy for fiat currency within crypto markets, this metric helps assess the potential buying power available to purchase BTC. A high SSR indicates relatively low stablecoin liquidity compared to Bitcoin’s valuation, suggesting reduced buying power and potential sell pressure. Conversely, a low SSR implies greater stablecoin availability, often interpreted as increased market capacity to buy Bitcoin. The historical data for this indicator begins on 2017-11-28 00:00:00.

    - **Specific Parameters** 
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
  ```python
  resp = client.get_btc_mkt_ssr(window="day", limit=365)
```

- **Market Value to Realized Value (MVRV)**: Calculated as the ratio of Bitcoin’s market capitalization to its realized capitalization. This metric reflects the relationship between speculative market value and the actual cost basis of holders. A high MVRV indicates that the market value significantly exceeds the aggregate cost at which coins last moved, suggesting potential overvaluation and profit-taking conditions. Conversely, a low MVRV suggests that the market value is close to or below the holders’ cost basis, indicating potential undervaluation or accumulation phases.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
  ```python
  resp = client.get_btc_mkt_mvrv(window="day", limit=365)
  ```

- **Spent Output Profit Ratio (SOPR)**: Measures the overall profit ratio of market participants by comparing the value of spent outputs at the time they are spent to their value when they were created. It is calculated as the USD value of spent outputs at the spent time divided by the USD value of those outputs at their creation time. A SOPR value greater than 1 indicates that coins are being sold at a profit, while values below 1 imply that coins are being sold at a loss. This metric helps identify periods of profit-taking, market capitulation, or accumulation based on on-chain spending behavior.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
  ```python
  resp = client.get_btc_mkt_sopr(window="day", limit=365)
```

- **SOPR Ratio (Long-Term vs Short-Term Holders)**: Calculated as the ratio between the SOPR of long-term holders (LTH) and that of short-term holders (STH). A higher SOPR Ratio indicates that long-term holders are realizing more profit relative to short-term holders, which often occurs near market tops or during periods of strong distribution. Conversely, a lower ratio suggests that short-term participants are dominating realized profits, typically seen in early recovery or accumulation phases.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
  ```python
  resp = client.get_btc_mkt_soprratio(window="day", limit=365)
```

- **Realized Price**: Calculated by dividing Bitcoin’s realized capitalization by the total circulating supply. This metric represents the average price at which all coins in circulation were last transacted, effectively capturing the market’s aggregate cost basis. Realized Price is often used as an on-chain support or resistance level, indicating whether the current market price is trading above or below the average acquisition cost of participants.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
  ```python
  resp = client.get_btc_mkt_realizedprice(window="day", limit=365)
```

- **UTxO Realized Price Age Distribution**: Provides the distribution of realized prices categorized by the age of unspent transaction outputs (UTxOs). This metric helps visualize the cost basis of different holding cohorts by grouping coins according to how long they have remained unspent. By comparing realized prices across age bands, it becomes possible to assess whether long-term holders or newer entrants dominate market positioning and how their cost structures differ over time.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
  ```python
  resp = client.get_btc_mkt_utxo(window="day", limit=180)
```


#### Network Indicator [:arrow_up:](#cryptoquant-sdk)

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
---

## Disclaimer [:arrow_up:](#cryptoquant-sdk)
The information in this document is provided for informational and educational purposes only. Nothing herein should be construed as financial, legal, or tax advice. The author is not a licensed financial advisor or registered investment consultant.

This SDK is not affiliated with or endorsed by CryptoQuant. It is an independent, open-source tool intended for research and data analysis.

This document does not constitute an offer to buy or sell any financial instrument. Always perform your own due diligence and consult a qualified professional before making investment decisions.