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
	1. [Available Endpoints](#available-endpoints-arrow_up)
	2. [Bitcoin](#bitcoin-arrow_up)
		- [Entity Status](#entity-status-arrow_up)
		- [Exchange Flows](#exchange-flows-arrow_up)
        - [Flow Indicators](#flow-indicators-arrow_up)
        - [Market Indicators](#market-indicators-arrow_up)
        - [Network Indicators](#network-indicators-arrow_up)
            - [Classical valuation models](#classical-valuation-models-arrow_up)
            - [Network activity and profitability](#network-activity-and-profitability-arrow_up)
            - [Realized and PnL data](#realized-and-pnl-data-arrow_up)
            - [UTXO Distribution](#utxo-distribution-arrow_up)
        - [Miner Flows](#miner-flows-arrow_up)
        - [Inter Entity Flows](#inter-entity-flows-arrow_up)
        - [Fund Data](#fund-data-arrow_up)
        - [Market or Liquidity Data](#market-or-liquidity-data-arrow_up)
        - [Miner Data](#miner-data-arrow_up)
        - [Network Data](#network-data-arrow_up)
            - [Monetary activity and circulation](#monetary-activity-and-circulation-arrow_up)
            - [Network usage](#network-usage-arrow_up)
            - [Block metrics](#block-metrics-arrow_up)
            - [Structure of the UTXO set](#structure-of-the-utxo-set-arrow_up)
            - [Fees](#fees-arrow_up)
            - [Mining economy](#mining-economy-arrow_up)
        - [Mempool Statistics](#mempool-statistics-arrow_up)
        - [Lightning Network Statistics](#lightning-network-statistics-arrow_up)
    3. [Ethereum](#ethereum-arrow_up)
        - [ETH Entity Status](#eth-entity-status-arrow_up)
        - [Exchange Flows](#exchange-flows-arrow_up)
        - [ETH Flow Indicators](#eth-flow-indicators-arrow_up)
        - [ETH Market Indicators](#eth-market-indicators-arrow_up)
        - [ETH 2.0](#eth-20-arrow_up)
        - [ETH Fund Data](#eth-fund-data-arrow_up)
        - [ETH Market Data](#eth-market-data-arrow_up)
        - [ETH Network Data](#eth-network-data-arrow_up)
            - [Supply and Velocity](#supply-and-velocity-arrow_up)
            - [Contracts and Transactions](#contracts-and-transactions-arrow_up)
            - [ETH Addresses](#eth-addresses-arrow_up)
            - [Token Transfers](#token-transfers-arrow_up)
            - [Failed Transactions](#failed-transactions-arrow_up)
            - [ETH Block Metrics](#eth-block-metrics-arrow_up)
            - [Fees and Gas Metrics](#fees-and-gas-metrics-arrow_up)
            - [ETH Mining and Network Performance](#eth-mining-and-network-performance-arrow_up)
    4. [XRP](#xrp-arrow_up)
        - [XRP Entity Status](#xrp-entity-status-arrow_up)
        - [XRP Entity Flows](#xrp-entity-flows-arrow_up)
        - [XRP Flow Indicators](#xrp-flow-indicators-arrow_up)
        - [XRP Market Data](#xrp-market-data-arrow_up)
        - [XRP Network Data](#xrp-network-data-arrow_up)
        - [XRP Network Indicator](#xrp-network-indicator-arrow_up)
        - [XRP Dex Data](#xrp-dex-data-arrow_up)
        - [XRP AMM Data](#xrp-amm-data-arrow_up)
    5. [TRX](#trx-arrow_up)
        - [TRX Market data](#trx-market-data-arrow_up)
        - [TRX Network Data](#trx-network-data-arrow_up)
        - [TRX DEFI](#trx-defi-arrow_up)
    6. [StableCoins](#Stablecoins-arrow_up)
        - [StableCoin Entity List](#stablecoin-entity-list-arrow_up)
        - [StableCoin Exchange Flows](#stablecoin-exchange-flows-arrow_up)
        - [Stablecoin Flow Indicator](#stablecoin-flow-indicator-arrow_up)
        - [Stablecoin Market Data](#stablecoin-market-data-arrow_up)
        - [Stablecoin Network Data](#stablecoin-network-data-arrow_up)
    7. [ERC20](#erc20-arrow_up)
        - [ERC20 Entity Status](#erc20-entity-status-arrow_up)
        - [ERC20 Exchange Flows](#erc20-exchange-flows-arrow_up)
        - [ERC20 Flow Indicator](#erc20-flow-indicator-arrow_up)
        - [ERC20 Market Data](#erc20-market-data-arrow_up)
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

I strongly recommend saving your API keys in your environment variables. You can find a short tutorial in the [following video](https://www.youtube.com/watch?v=IolxqkL7cD8):

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


#### Network Indicators [:arrow_up:](#cryptoquant-sdk)

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

##### Classical valuation models [:arrow_up:](#cryptoquant-sdk)

- **Stock-to-Flow (S2F)**: Evaluates Bitcoin’s scarcity by comparing the existing circulating supply to the rate of new issuance. The metric assumes that, like gold or other scarce commodities, Bitcoin’s value is influenced by its limited and predictable supply. Stock-to-Flow is calculated by dividing the total circulating coins by the annual production (newly mined coins). Higher S2F values indicate greater scarcity, which historically has been associated with long-term price appreciation trends.

    - **Specific Parameters** 
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_stock2flow(window="day", limit=365)
```

- **Network Value to Transactions (NVT) Ratio**: Calculated as Bitcoin’s network value (total supply multiplied by price in USD) divided by the total value of tokens transferred on-chain. This metric is often used to assess whether Bitcoin is overvalued or undervalued relative to its transaction activity. The underlying theory is that the fundamental value of the network is derived from its usage — when the NVT ratio is high, it may indicate overvaluation or reduced transactional utility, while a low NVT suggests that network activity is strong relative to valuation.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_nvt(window="day", limit=365)
```

- **NVT Golden Cross**: A modified version of the traditional NVT ratio designed to identify local market tops and bottoms. The indicator compares short-term and long-term moving averages of the NVT ratio to generate dynamic signals of potential trend reversals. Values above approximately 2.2 suggest increased downside risk and potential overvaluation, while values below -1.6 indicate strong upside potential or undervaluation.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_nvtgoldencross(window="day", limit=365)
```

- **Network Value to Metcalfe Ratio (NVM)**: A valuation metric derived from Metcalfe’s Law, which states that the value of a network grows in proportion to the square of its number of active users. NVM is calculated by dividing Bitcoin’s market capitalization by the number of daily active addresses, providing a way to assess whether network activity justifies its market value. Lower NVM values suggest the network may be undervalued relative to user activity, while higher values indicate potential overvaluation or reduced user engagement.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_nvm(window="day", limit=365)
```

- **Puell Multiple**: Calculated as the ratio between the current daily mining revenue (in USD) and its 365-day moving average.  
  This metric highlights periods when miner revenue is significantly above or below historical norms, helping to identify potential market tops and bottoms. Low Puell Multiple values often occur near cyclical lows, suggesting reduced miner profitability and possible accumulation opportunities, while high values are typically observed near market peaks, indicating potential overvaluation. The indicator was developed by David Puell.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_puell(window="day", limit=365)
```

##### Network activity and profitability [:arrow_up:](#cryptoquant-sdk)

- **Coin Days Destroyed (CDD)**: Measures the total activity of spent coins weighted by their holding time, giving more significance to movements of long-held coins. It is calculated as the sum of each spent output’s value multiplied by the number of days it remained unspent. The supply-adjusted version (sa_cdd) normalizes this value by dividing CDD by the total coin supply, allowing comparisons across time. The binary version of CDD signals whether the current supply-adjusted CDD exceeds its historical average since the genesis block (1 if above average, 0 if below). Elevated values often indicate that long-term holders or whales are moving coins, which can suggest increased market activity or profit realization.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_cdd(window="day", limit=365)
```

- **Mean Coin Age (MCA)**: Represents the average age of all unspent transaction outputs (UTxOs), weighted by their value. It is conceptually similar to Coin Days Destroyed (CDD) but focuses on unspent rather than spent coins, providing a view of how long coins have remained dormant in the network. A rising Mean Coin Age indicates that coins are staying unspent for longer periods, suggesting accumulation and reduced on-chain activity, while a declining value implies renewed spending or increased market participation. The related metric, Mean Coin Dollar Age (MCDA), extends this concept by weighting UTxOs by both their age and the price of Bitcoin at the time they were created.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_mca(window="day", limit=365)
```

- **Sum Coin Age (SCA)**: Represents the cumulative age of all unspent transaction outputs (UTxOs), weighted by their value.  
  It is closely related to Coin Days Destroyed (CDD) but focuses on coins that remain unspent, reflecting the aggregate holding duration of all circulating Bitcoin.  
  A growing Sum Coin Age indicates that more coins are remaining dormant, suggesting long-term holding or reduced market activity.  
  The complementary metric, Sum Coin Dollar Age (SCDA), multiplies UTxO age and value by the Bitcoin price at the time of creation, providing a dollar-weighted perspective on network dormancy.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_sca(window="day", limit=365)
```

- **Sum Coin Age Distribution (SCAD)**: Shows the distribution of Bitcoin held by long-term and short-term holders based on UTxO data. Similar to the UTxO distribution, this metric is weighted by the number of days each coin has remained unspent, emphasizing the distribution of long-term holders across different holding ranges. Each value is calculated as the sum of products of UTxO age and value within a specific range, divided by the total sum across all ranges. An increasing proportion of long-term holder distribution typically signals a bullish market phase, as it reflects accumulation and reduced spending activity.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_scad(window="day", limit=365)
```

- **Net Unrealized Profit and Loss (NUPL)**: Measures the difference between Bitcoin’s market capitalization and realized capitalization, normalized by market cap. It is calculated as (market_cap − realized_cap) / market_cap and reflects the overall unrealized profit or loss held by market participants. A positive NUPL value (market_cap > realized_cap) indicates that, on average, holders are in profit—often corresponding to increased selling pressure or overvaluation risk. Conversely, a negative NUPL value suggests that holders are in unrealized loss, typically associated with market capitulation or accumulation phases. Related submetrics include Net Unrealized Profit (NUP), which measures profits from UTxOs in gain, and Net Unrealized Loss (NUL), which captures losses from UTxOs in decline.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_nupl(window="day", limit=365)
```

- **Net Realized Profit/Loss (NRPL)**: Represents the net amount of profit or loss realized by all Bitcoin holders when coins are spent on-chain. It is calculated relative to the price at which each coin last moved, capturing the difference between the current spending price and the historical acquisition cost. Positive NRPL values indicate that, on aggregate, coins are being spent at a profit, while negative values show that coins are being sold at a loss. This metric helps evaluate market sentiment and behavioral shifts, such as phases of profit-taking, capitulation, or renewed confidence among holders.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_nrpl(window="day", limit=365)
```

##### Realized and PnL data [:arrow_up:](#cryptoquant-sdk)


- **Profit and Loss (UTxO)**: Evaluates the number of unspent transaction outputs (UTxOs) that are in profit or loss by comparing the Bitcoin price at the time of creation with the price at the time of destruction. A UTxO is considered in profit if the price at which it is spent is higher than its creation price, and in loss if the opposite is true. This metric provides a detailed view of the profitability distribution of spent outputs, helping to identify whether market participants are realizing gains or losses at a given point in time.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_pnlutxo(window="day", limit=365)
```

- **Profit and Loss (Supply)**: Measures the total value of Bitcoin supply currently in profit or loss by comparing the creation and destruction prices of UTxOs, weighted by their value. Unlike the Profit and Loss (UTxO) metric, which counts outputs equally, this version assigns greater importance to larger holdings, providing a more accurate view of how much supply is profitable at a given time.  It effectively quantifies the portion of the active Bitcoin supply that is in profit or loss, helping assess overall market health and investor sentiment.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_pnlsupply(window="day", limit=365)
```

- **Average Dormancy**: Represents the average number of days destroyed per coin transacted, providing insight into how long coins typically remain dormant before being moved. This metric is calculated as the total Coin Days Destroyed (CDD) divided by the number of coins transacted. The Supply-Adjusted Average Dormancy (SA Average Dormancy) normalizes this value by the total circulating supply to account for long-term growth in mined coins. Higher dormancy values indicate that older coins are being spent, often suggesting profit-taking or market transitions, while lower values imply more frequent movement of recently created coins.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**
```python
resp = client.get_btc_ntw_dormancy(window="day", limit=365)
```

##### UTXO Distribution [:arrow_up:](#cryptoquant-sdk)

- **UTxO Age Distribution**: Displays the distribution of Bitcoin’s active supply categorized by the age of unspent transaction outputs (UTxOs). This indicator provides insight into the behavior of long-term and short-term holders by showing how much of the circulating supply has remained unspent within different time bands. It helps identify accumulation, distribution, or dormancy patterns among holders and how these behaviors correspond to price movements. The distribution values are provided in native BTC units, USD value, and percentage of total supply.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_utxo_age_distr(window="day", limit=180)
```

- **UTxO Realized Age Distribution**: Represents the distribution of Bitcoin’s active supply by UTxO age bands, weighted by the price at the time each UTxO was created. Similar in concept to Realized Capitalization, this metric reflects how network capitalization is distributed among long-term and short-term holders across different age cohorts. It helps assess which groups of holders dominate the market’s realized value and how their behavior changes over time. Distribution values are provided in native BTC units, USD value, and percentage of total supply.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_utxo_realized_age_dstr(window="day", limit=180)
```

- **UTxO Count Age Distribution**: Shows the distribution of the number of unspent transaction outputs (UTxOs) grouped by age bands. This indicator summarizes how many long-term and short-term holders exist within each cohort, providing a view of holder composition across time. It helps reveal the balance between recently active wallets and long-dormant holders, offering insights into market maturity and behavioral shifts. The distribution values are provided in native counts and as percentages of the total UTxO set.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_utxo_count_age_dstr(window="day", limit=180)
```

- **Spent Output Age Distribution**: Represents the distribution of spent transaction outputs (UTxOs) categorized by the age of the coins at the time they were spent. This indicator shows how much of the total spent volume originates from long-term versus short-term holders, providing insight into holder behavior and potential market turning points. High spending activity from older age bands can indicate long-term holders realizing profits or exiting positions, while dominance of younger age bands suggests routine trading activity. The distribution values are available in native BTC units, USD value, and percentage of total spent outputs.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_spent_output_age_dstr(window="day", limit=180)
```

- **UTxO Supply Distribution**: Displays the distribution of Bitcoin’s active supply segmented by wallet balance bands. This indicator distinguishes between whale and retail behavior by showing how much BTC is held across different balance ranges and how these holdings evolve with price movements. It helps track concentration of wealth, accumulation patterns, and the relative influence of large versus small holders on market dynamics. The distribution values are provided in native BTC units and as percentages of total supply.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_utxo_supply_dstr(window="day", limit=180)
```

- **UTxO Realized Supply Distribution**: Represents the distribution of Bitcoin’s active supply segmented by wallet balance bands and weighted by the price at which each UTxO was created. Similar to the Realized Capitalization concept, this indicator shows how network capitalization is distributed among whales and retail holders across different balance ranges. It provides insight into which holder groups control the most realized value in the network and how these proportions shift over time. The distribution values are provided in USD and as percentages of the total realized supply.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_utxo_realized_supply_dstr(window="day", limit=180)
```

- **UTxO Count Supply Distribution**: Shows the distribution of the number of holders grouped by wallet balance bands. This indicator illustrates how many entities fall into each holding category, distinguishing between whales and retail participants. It helps analyze the composition of the Bitcoin holder base, revealing changes in wealth concentration, entry of new participants, or distribution from large to small holders. The distribution values are provided in native counts and as percentages of the total number of holders.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_utxo_count_supply_dstr(window="day", limit=180)
```

- **Spent Output Supply Distribution**: Represents the distribution of spent Bitcoin outputs grouped by wallet balance bands. This indicator shows how much of the total spent supply originates from whales versus retail holders, highlighting which groups are actively realizing profits or moving funds. It provides context for market dynamics by revealing whether large holders are distributing (selling) or small holders are driving transaction activity. The distribution values are provided in native BTC units, USD value, and as percentages of total spent supply.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_ntw_spent_output_supply_dstr(window="day", limit=180)
```

#### Miner Flows [:arrow_up:](#cryptoquant-sdk)

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

- **Miner Reserve**: Returns the historical on-chain balance of Bitcoin mining pools.  
  This metric tracks the total amount of BTC held in miner-associated wallets over time, reflecting miners’ cumulative holdings.  
  Increases in miner reserves indicate accumulation or reduced selling activity, while decreases suggest distribution or operational selling to cover costs.  
  Monitoring miner reserves provides insight into miners’ confidence and their potential influence on market supply.

    - **Specific Parameters**  
        - ```miner```(str): Required — Miner or pool name (e.g., `f2pool`, `antpool`, `foundry`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_miner_reserve(miner="viabtc", window="day", limit=365)
```

- **Miner Netflow**: Represents the net amount of Bitcoin flowing into or out of mining pool wallets, calculated as inflow minus outflow. This metric helps identify whether miners are accumulating or distributing their holdings during a specific time period. A positive netflow indicates that more coins are entering miner wallets than leaving, suggesting accumulation or reduced selling pressure. Conversely, a negative netflow means that more coins are flowing out, typically signaling increased selling activity or operational expenses.

    - **Specific Parameters**  
        - ```miner```(str): Required — Miner or pool name (e.g., `f2pool`, `viabtc`, `antpool`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_miner_netflow(miner="all_miner", window="day", limit=365)
```

- **Miner Inflow**: Returns the amount of Bitcoin flowing into mining pool wallets over time. This metric measures the total BTC transferred to miner-associated addresses, typically representing block rewards or internal fund movements. The average inflow value reflects the mean transaction size of BTC entering mining wallets during a given day. High inflows may indicate accumulation, reward consolidation, or repositioning of funds across miner wallets.

    - **Specific Parameters**  
        - ```miner```(str): Required — Miner or pool name (e.g., `f2pool`, `viabtc`, `antpool`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_miner_inflow(miner="all_miner", window="day", limit=365)
```

- **Miner Outflow**: Returns the amount of Bitcoin flowing out of mining pool wallets over time. This metric measures the total BTC transferred from miner-associated addresses, typically representing operational expenses, exchange deposits, or selling activity. The average outflow value reflects the mean transaction size of BTC leaving mining wallets on a given day. Sustained increases in outflows often indicate higher selling pressure or liquidity needs among miners.

    - **Specific Parameters**  
        - ```miner```(str): Required — Miner or pool name (e.g., `f2pool`, `viabtc`, `antpool`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_miner_outflow(miner="all_miner", window="day", limit=365)
```

- **Miner Transaction Count**: Returns the total number of Bitcoin transactions flowing into and out of mining pool wallets. This metric reflects the overall transaction activity of miners, capturing both inflows and outflows within a given period. Higher transaction counts may indicate increased operational activity, fund management, or redistribution of rewards among mining entities.

    - **Specific Parameters**  
        - ```miner```(str): Required — Miner or pool name (e.g., `f2pool`, `viabtc`, `antpool`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_miner_txn_count(miner="all_miner", window="day", limit=365)
```

- **Miner Address Count**: Returns the number of unique addresses involved in inflow and outflow transactions related to mining pool wallets. This metric reflects the level of activity and address utilization among miners. A rising address count may indicate diversification of wallet structures or increased operational complexity, while a declining count suggests consolidation of funds into fewer addresses or reduced activity.

    - **Specific Parameters**  
        - ```miner```(str): Required — Miner or pool name (e.g., `f2pool`, `viabtc`, `antpool`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_miner_addr_count(miner="all_miner", window="day", limit=365)
```

- **Miner In-House Flow**: Returns the volume of Bitcoin transferred internally between wallets belonging to the same mining pool. This metric captures movements of BTC that remain within a miner’s ecosystem, such as fund reallocation or internal management of rewards. The average in-house flow represents the mean transaction value of these internal transfers on a given day. High in-house flow can indicate operational restructuring, reward distribution, or wallet reorganization by miners.

    - **Specific Parameters**  
        - ```miner```(str): Required — Miner or pool name (e.g., `f2pool`, `viabtc`, `antpool`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_miner_inhouse_flow(miner="all_miner", window="day", limit=365)
```

#### Inter Entity Flows [:arrow_up:](#cryptoquant-sdk)
Inter-entity flows help assess capital movements between structural actors in the ecosystem. For example, a sustained increase in `miner_2_exch` suggests selling pressure, while increases in `exch_2_exch` may reflect liquidity adjustments or arbitrage.

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

- **Exchange-to-Exchange Flow**: Returns metrics related to Bitcoin transfers between exchange wallets. This endpoint provides several measures, including `flow_total` (total BTC transferred from one exchange to another), `flow_mean` (average BTC transferred per transaction), and `transactions_count_flow` (the number of transactions between exchanges). These flows help assess inter-exchange liquidity movements, potential arbitrage activity, and overall exchange connectivity within the network.

    - **Specific Parameters**  
        - ```from_exchange```(str): Required — Origin exchange name (e.g., `binance`, `bitmex`, `kraken`, etc).  
        - ```to_exchange```(str): Required — Destination exchange name (e.g., `binance`, `bitmex`, `kraken`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_inter_exch_2_exch(from_exchange="binance", to_exchange="kraken", window="day", limit=365)
```

- **Miner-to-Exchange Flow**: Returns metrics related to Bitcoin transfers from mining pool wallets to exchanges. This endpoint provides several measures, including `flow_total` (total BTC transferred from a mining pool to an exchange), `flow_mean` (average BTC transferred per transaction), and `transactions_count_flow` (the number of transactions from miners to exchanges). This indicator helps evaluate miners’ selling behavior and potential market impact, as higher outflows to exchanges often signal increased selling pressure or liquidity provisioning.

    - **Specific Parameters**  
        - ```from_miner```(str): Required — Origin miner or pool name (e.g., `f2pool`, `viabtc`, `antpool`, etc).  
        - ```to_exchange```(str): Required — Destination exchange name (e.g., `binance`, `bitmex`, `kraken`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_inter_miner_2_exch(from_miner="antpool", to_exchange="binance", window="day", limit=365)
```

- **Exchange-to-Miner Flow**: Returns metrics related to Bitcoin transfers from exchange wallets to mining pool wallets. This endpoint provides several measures, including `flow_total` (total BTC transferred from an exchange to a mining pool), `flow_mean` (average BTC transferred per transaction), and `transactions_count_flow` (the number of transactions from exchanges to miners). This indicator helps track fund movements from trading venues back to mining entities, which can reflect pool payments, operational funding, or redistribution of mined rewards.

    - **Specific Parameters**  
        - ```from_exchange```(str): Required — Origin exchange name (e.g., `binance`, `bitmex`, `kraken`, etc).  
        - ```to_miner```(str): Required — Destination miner or pool name (e.g., `f2pool`, `viabtc`, `antpool`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

  - **Usage**  
```python
resp = client.get_btc_inter_exch_2_miner(from_exchange="kraken", to_miner="f2pool", window="day", limit=365)
```

- **Miner-to-Miner Flow**: Returns metrics related to Bitcoin transfers between mining pool wallets. This endpoint provides several measures, including `flow_total` (total BTC transferred from one mining pool to another), `flow_mean` (average BTC transferred per transaction), and `transactions_count_flow` (the number of transactions between mining pools). These flows can indicate internal fund redistribution, cooperative transfers, or structural changes among mining entities and pools.

    - **Specific Parameters**  
        - ```from_miner```(str): Required — Origin miner or pool name (e.g., `f2pool`, `viabtc`, `antpool`, etc).  
        - ```to_miner```(str): Required — Destination miner or pool name (e.g., `f2pool`, `viabtc`, `antpool`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_inter_miner_2_miner(from_miner="f2pool", to_miner="antpool", window="day", limit=365)
```

#### Fund Data [:arrow_up:](#cryptoquant-sdk)
This section is key for analyzing the behavior of institutional capital, as it reflects whether funds are receiving net inflows, whether the market values the products above or below their NAV, and how institutional adoption in Bitcoin is evolving.

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

- **Fund Market Price**: Returns metrics related to the USD price of fund-related securities such as GBTC (Grayscale Bitcoin Trust). The price of these instruments reflects investor sentiment in regulated markets, where one share of GBTC represents approximately 0.001 BTC under management. This endpoint provides multiple price metrics including `price_usd_open` (opening price at the start of the window), `price_usd_close` (closing price at the end of the window), `price_usd_high` (highest price within the window), `price_usd_low` (lowest price within the window), and `price_usd_adj_close` (adjusted closing price). Not all symbols are supported.

    - **Specific Parameters**  
        - ```symbol```(str): Required — Fund symbol (e.g., `gbtc`, `ibit`, `fbtc`, etc).  
        - ```fund```(str): Required — Fund manager name (e.g., `grayscale`, `blackrock`, `fidelity`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_fund_mkt_price(symbol="gbtc", window="day", limit=365)
```

- **Fund Market Volume**: Returns the traded volume of fund-related securities such as GBTC on regulated markets. The trading volume of these instruments reflects investor sentiment and market participation among institutional and retail investors. Metrics are calculated on a daily basis and include `volume`, representing the total traded volume within the specified window.

    - **Specific Parameters**  
        - ```symbol```(str): Required — Fund symbol (e.g., `gbtc`, `ibit`, `fbtc`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_fund_mkt_volume(symbol="gbtc", window="day", limit=365)
```

- **Fund Market Premium**: Measures the premium or discount of fund-related securities such as GBTC by comparing their market price to their Net Asset Value (NAV). It is calculated as `(market price − NAV) / NAV`, where NAV represents the current value of the underlying holdings (e.g., BTC price multiplied by BTC per share). A higher premium suggests bullish market sentiment but may also signal increased downside risk, while a lower or negative premium indicates bearish sentiment with potential upside opportunity. For all supported symbols, the market premium is calculated using the volume-weighted average ratio (VWAP) based on USD-denominated trading volume.

    - **Specific Parameters**  
        - ```symbol```(str): Required — Fund symbol (e.g., `gbtc`, `ibit`, `fbtc`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_fund_mkt_premium(symbol="gbtc", window="day", limit=365)
```

- **Fund Digital Asset Holdings**: Returns the total digital asset holdings of each fund, representing how much Bitcoin is held under management. For example, the Grayscale Bitcoin Trust (GBTC) metric reflects the amount of BTC Grayscale holds for its investors. This indicator serves as a proxy for institutional sentiment, as increasing holdings generally signal growing investor confidence and bullish outlooks in regulated markets, while declining holdings may indicate profit-taking or reduced exposure.

    - **Specific Parameters**  
        - ```symbol```(str): Required — Fund symbol (e.g., `gbtc`, `ibit`, `fbtc`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_fund_digital_assets_holdings(symbol="gbtc", window="day", limit=365)
```

#### Market or Liquidity Data [:arrow_up:](#cryptoquant-sdk)
This section is used to monitor liquidity, leverage, and market microstructure. It allows for the assessment of phases of over-leveraging, imbalances between orders, or liquidity stress that can anticipate price movements.

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

- **BTC Price OHLCV**: Returns Bitcoin price metrics across spot and perpetual markets, including CryptoQuant’s BTC Index Price and USD or USDT-denominated prices from individual exchanges. It provides `open`, `close`, `high`, `low`, and `volume` values for each interval (minute, hour, day). The BTC Index Price is calculated using VWAP aggregated from major exchanges such as Binance, Bitfinex, Bittrex, Bitmex, Bybit, Deribit, Gemini, HTX Global, Kraken, and OKX. For exchange-specific data, specify `market`, `exchange`, and `symbol`. Volume units vary by exchange (BTC, USD, or USDT), and daily data are computed from UTC 00:00:00, except for HTX and OKX, which use UTC 16:00:00.

    - **Specific Parameters**  
        - ```market```(str): Optional — Market type (`spot` or `perpetual`).  
        - ```exchange```(str): Optional — Exchange name (e.g., `binance`, `bitmex`, `kraken`, `okx`, etc).  
        - ```symbol```(str): Optional — Trading pair symbol (e.g., `btc_usd`, `btc_usdt`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_liq_ohlcv(market="spot", exchange="binance", symbol="btc_usdt", window="day", limit=365)
```

- **BTC Perpetual Open Interest**: Returns the total USD-denominated open interest for Bitcoin perpetual futures across major derivative exchanges. This metric represents the total value of outstanding derivative contracts and provides insight into market leverage and trader positioning. Open interest is unified to USD across all exchanges, regardless of contract specifications. Supported exchanges include Binance, Bitfinex, Bitmex, Bybit, Deribit, Gate.io, HTX Global, Kraken, and OKX. Higher open interest levels often indicate increased speculative activity or leverage buildup, while declining values suggest position unwinding or reduced participation.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `bitmex`, `bybit`, `okx`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_liq_open_interest(exchange="binance", window="day", limit=365)
```

- **BTC Funding Rates**: Returns the funding rates for Bitcoin perpetual swap contracts across major derivative exchanges. Funding rates reflect traders’ sentiment and the directional bias of open positions in the perpetual futures market. Positive funding rates indicate that long traders are dominant and paying funding to short traders (bullish sentiment), while negative rates indicate that short traders are dominant and paying funding to long traders (bearish sentiment). Supported exchanges include Binance, Bybit, Bitmex, Deribit, HTX Global, and OKX.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `bitmex`, `bybit`, `okx`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_liq_funding_rates(exchange="binance", window="day", limit=365)
```

- **BTC Taker Buy/Sell Stats**: Returns metrics representing taker activity and sentiment in the Bitcoin perpetual swap market across major derivative exchanges. These metrics include `taker_buy_volume` (volume bought by takers), `taker_sell_volume` (volume sold by takers), `taker_total_volume` (sum of buy and sell volume), `taker_buy_ratio` (buy volume divided by total volume), `taker_sell_ratio` (sell volume divided by total volume), and `taker_buy_sell_ratio` (buy volume divided by sell volume). All values are standardized in USD to ensure comparability across exchanges. Supported exchanges include Binance, Bybit, Bitmex, Deribit, HTX Global, and OKX.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `bitmex`, `bybit`, `okx`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_liq_taker_stats(exchange="binance", window="day", limit=365)
```

- **BTC Liquidations**: Returns the total value of forced market orders triggered to close leveraged positions across major derivative exchanges. Liquidations occur when traders’ margins are insufficient to maintain positions during price volatility and thus provide insight into leverage imbalances and trader sentiment. High liquidation volumes often coincide with sharp market moves and increased volatility. Note that Binance’s liquidation data collection policy changed after 2021-04-27, which may affect data distribution post-update. Supported exchanges include Binance, Bitfinex, Bitmex, Bybit, Deribit, Gate.io, HTX Global, and OKX.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange name (e.g., `binance`, `bitmex`, `bybit`, `okx`, etc).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_liq_liquidations(exchange="binance", window="day", limit=365)
```

- **BTC Market Capitalization**: Returns Bitcoin market capitalization metrics, including standard and adjusted on-chain valuation models. The `market_cap` represents the total market capitalization, calculated by multiplying total supply by USD price. The `realized_cap` measures the aggregate value of all UTXOs at the price they last moved, discounting coins that are lost or dormant for long periods—essentially serving as an on-chain version of VWAP. The `average_cap` is a lifetime moving average of market capitalization, derived by dividing the cumulative daily market cap by the network’s age, representing the true historical mean. The `delta_cap` is calculated as `realized_cap − average_cap` and is often used to identify market bottoms, while `thermo_cap` represents the cumulative value of mined coins weighted by price, offering a perspective on total on-chain investment and potential overvaluation.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_liq_capitalization(window="day", limit=365)
```

- **Coinbase Premium Index**: Measures the price difference between Coinbase (BTC/USD) and Binance (BTC/USDT) to assess spot market buying pressure from U.S.-based investors. The metric includes the Coinbase Premium Index, calculated as the percentage difference between Coinbase and Binance prices, and the Coinbase Premium Gap, which represents the absolute price difference between the two exchanges. A higher premium indicates stronger buying demand on Coinbase, often interpreted as institutional or U.S. market-driven accumulation.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_liq_coinbase_idx(window="day", limit=365)
```

#### Miner Data [:arrow_up:](#cryptoquant-sdk)

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

- **BTC Miner Company Data**: Returns on-chain and production-based statistics for publicly listed Bitcoin mining companies. The dataset includes `coinbase_rewards` (daily BTC mined directly from coinbase transactions, applied only to MARA), `other_mining_rewards` (daily BTC received as pool payouts), `total_rewards` (sum of coinbase and other mining rewards in BTC), and `accumulated_monthly_rewards` (running monthly total of rewards). Additional metrics include `unique_txn` (number of reward-related transactions), `active_address_count` (number of addresses receiving block rewards), `reported_production` (self-reported monthly BTC production), and `report_accuracy` (ratio of on-chain monthly rewards to reported production × 100, reflecting reporting precision). USD-based metrics include `closing_usd` (daily BTC price), `total_daily_rewards_closing_usd` (daily total rewards in USD), and `accumulated_monthly_rewards_closing_usd` (monthly accumulated rewards in USD). Supported miners include MARA, RIOT, CORE, HIVE, CLSK, BITF, CIPHER, WULF, and IREN.

    - **Specific Parameters**  
        - ```miner```(str): Required — Public mining company symbol (e.g., `mara`, `riot`, `hive`, `bitf`, `core`, `clsk`, `cipher`, `wulf`, `iren`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_miner_company_data(miner="mara", window="day", limit=365)
```

#### Network Data [:arrow_up:](#cryptoquant-sdk)
Bitcoin on-chain network data including but not limited to token movements, fees, supply, address movements, etc. All metrics have data entries starting from the genesis block (block height 0, datetime 2009-01-03 18:15:05).

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

##### Monetary activity and circulation [:arrow_up:](#cryptoquant-sdk)

- **BTC Supply**: Returns metrics related to Bitcoin’s total and newly issued supply. It includes `supply_total`, representing the total number of bitcoins in existence (sum of all coins issued through coinbase rewards), and `supply_new`, representing the number of new bitcoins created within a given time window. These metrics provide insight into Bitcoin’s issuance schedule and the effects of halving events on supply growth.

    - **Specific Parameters**   
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_net_supply(window="day", limit=365)
```

- **BTC Velocity**: Returns metrics related to the velocity of Bitcoin, calculated as the trailing one-year cumulative transaction volume divided by the current circulating supply. This metric reflects how actively Bitcoin is being used or transferred within the network and serves as an indicator of on-chain economic activity. Higher velocity values suggest greater transaction frequency and market circulation, while lower values indicate reduced on-chain activity or holding behavior.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_net_velocity(window="day", limit=365)
```

- **BTC Tokens Transferred**: Returns metrics related to Bitcoin’s on-chain transaction volume, representing the total number of tokens moved between addresses. It includes `tokens_transferred_total` (total BTC transferred), `tokens_transferred_mean` (average BTC transferred per transaction), and `tokens_transferred_median` (median BTC transferred per transaction). These metrics help evaluate the scale and distribution of Bitcoin transaction activity over time.

    - **Specific Parameters**    
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_net_tokens_transferred(window="day", limit=365)
```

##### Network usage [:arrow_up:](#cryptoquant-sdk)

- **BTC Transaction Count**: Returns metrics related to the number of Bitcoin transactions processed on-chain. It includes `transactions_count_total`, representing the total number of transactions within a given window, and `transactions_count_mean`, representing the average number of transactions over that period. These metrics provide insight into network utilization, user activity, and overall transactional demand.

    - **Specific Parameters**   
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_net_trx_count(window="day", limit=365)
```

- **BTC Address Count**: Returns metrics related to the number of active Bitcoin addresses participating in transactions. It includes `addresses_count_active` (total unique addresses active as either sender or receiver), `addresses_count_sender` (number of addresses active as senders), and `addresses_count_receiver` (number of addresses active as receivers). These metrics help measure network participation, user activity, and overall adoption trends within the Bitcoin ecosystem.

    - **Specific Parameters**   
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_net_addr_count(window="day", limit=365)
```

##### Block metrics [:arrow_up:](#cryptoquant-sdk)

- **BTC Block Bytes**: Returns the mean size of all Bitcoin blocks generated within a given time window, measured in bytes. This metric reflects block utilization and network throughput efficiency, helping to assess transaction density and overall demand for block space.

    - **Specific Parameters**    
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_net_block_bytes(window="day", limit=365)
```

- **BTC Block Count**: Returns the total number of Bitcoin blocks generated within a specified time window. This metric indicates the pace of block production and helps monitor network performance, mining activity, and block confirmation rates over time.

    - **Specific Parameters**   
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_net_block_count(window="day", limit=365)
```

- **BTC Block Interval**: Returns the average time between Bitcoin blocks generated, expressed in seconds. This metric measures the consistency of block production and serves as an indicator of network health and mining difficulty adjustments. Shorter intervals may reflect increased hash power, while longer intervals can indicate reduced mining activity or rising difficulty.

    - **Specific Parameters**   
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_net_block_interval(window="day", limit=365)
```

##### Structure of the UTXO set [:arrow_up:](#cryptoquant-sdk)

- **BTC UTXO Count**: Returns the total number of unspent transaction outputs (UTXOs) existing at a specified point in time. This metric reflects the structure and fragmentation of the Bitcoin ledger, providing insights into user behavior, wallet activity, and the overall complexity of the UTXO set.

    - **Specific Parameters**   
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_net_utxo_count(window="day", limit=365)
```

##### Fees [:arrow_up:](#cryptoquant-sdk)

- **BTC Fees**: Returns statistics related to transaction fees paid to Bitcoin miners. Fees are calculated by subtracting newly issued bitcoins from the total block reward of each block. Provided metrics include `fees_total` (sum of all fees), `fees_block_mean` (average fee per block), and `fees_reward_percent` (percentage of fees relative to total block rewards). Each metric can also be expressed in USD, offering a clearer view of miner revenue composition and network demand.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_net_fees(window="day", limit=365)
```

- **BTC Fees per Transaction**: Returns statistics related to the average transaction fees paid to Bitcoin miners. Fees are derived by subtracting newly issued bitcoins from the total block reward of each block and dividing by the number of transactions to determine the mean and median fee per transaction. Provided metrics include `fees_transaction_mean` (average fee per transaction) and `fees_transaction_median` (median fee per transaction). Both values can also be expressed in USD, offering insights into network congestion and user cost to transact on-chain.

    - **Specific Parameters**   
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_net_fees_trx(window="day", limit=365)
```

##### Mining economy [:arrow_up:](#cryptoquant-sdk)

- **BTC Block Reward**: Returns the total value of Bitcoin block rewards, including both the newly issued coins (mining rewards) and transaction fees earned by miners. This metric represents the overall miner revenue from block production and is also available in USD for easier valuation and comparison across time periods.

    - **Specific Parameters**    
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_net_blockreward(window="day", limit=365)
```

- **BTC Mining Difficulty**: Returns the mean difficulty required to mine a new Bitcoin block within a given time window. This metric reflects the overall computational power and competitiveness of the network. Increases in difficulty indicate growing miner participation and network security, while decreases suggest reduced hash power or miner activity.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_net_difficulty(window="day", limit=365)
```

- **BTC Hashrate**: Returns the mean computational speed at which miners across the Bitcoin network solve hash problems, expressed in gigahashes per second (GH/s). This metric serves as a key indicator of network security and mining activity. Higher hashrate values reflect stronger network resilience and miner participation, while lower values can indicate reduced mining power or profitability.

    - **Specific Parameters**  
        - No exchange parameter required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_net_hashrate(window="day", limit=365)
```

#### Mempool Statistics [:arrow_up:](#cryptoquant-sdk)
Mempool data allows anticipating fee pressure, detecting confirmation bottlenecks, and analyzing transactional activity in real time. Essentially, they reflect the demand for block space before actual confirmation.

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

- **Mempool Stats by Relative Fee**: Returns statistics of unconfirmed Bitcoin transactions in the mempool, categorized by fee levels. It provides three metrics: `tx_count` (total number of unconfirmed transactions), `total_size` (aggregate size of pending transactions in megabytes), and `total_fee` (total fees of unconfirmed transactions in BTC). These metrics help analyze network congestion and estimate the fee levels required for timely confirmation. Metrics are available for hourly and daily windows.

    - **Specific Parameters**  
        - ```metric_type```(str): Required — Type of metric to query (`tx_count`, `total_size`, `total_fee`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_mem_stats_by_relative_fee(metric_type="tx_count", window="day", limit=365)
```

- **Mempool Stats in Total**: Returns aggregated statistics of unconfirmed Bitcoin transactions across the entire mempool. It provides three metrics: `tx_count` (average number of unconfirmed transactions within the selected time range), `total_size` (average aggregate size of transactions in megabytes), and `total_fee` (average total fee of unconfirmed transactions in BTC). These metrics reflect overall network congestion and fee market pressure, helping assess how busy the network is during specific periods. Metrics are available for hourly and daily windows.

    - **Specific Parameters**  
        - ```metric_type```(str): Required — Type of metric to query (`tx_count`, `total_size`, `total_fee`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_mem_stats_in_total(metric_type="tx_count", window="day", limit=365)
```

#### Lightning Network Statistics [:arrow_up:](#cryptoquant-sdk)
Monitoring the Lightning Network allows for analyzing the evolution of Bitcoin's layer 2 infrastructure: growth of nodes, locked capital (available liquidity), and operational decentralization. This data is key to measuring the real adoption of Bitcoin as a means of payment, beyond purely speculative use or store of value.

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

- **Lightning Network Stats**: Returns key statistics derived from the Bitcoin Lightning Network, providing insight into its capacity, structure, and fee dynamics. Metrics include `network_capacity` (total BTC available across all channels), `network_capacity_usd` (same in USD), `capacity_per_channel_mean` and `capacity_per_channel_mean_usd` (average channel capacity), `capacity_per_node_mean` and `capacity_per_node_mean_usd` (average node capacity), `number_of_node` (total active nodes), `number_of_channel` (total open payment channels), `channel_per_node_mean` (average number of channels per node), `node_age_days` and `channel_age_days` (average lifespan of nodes and channels), and median fee metrics (`base_fee_median`, `base_fee_median_usd`, `fee_rate_median`, `fee_rate_median_usd`). These metrics allow analysis of Lightning’s liquidity distribution, decentralization, and fee competitiveness. Metrics are available for hourly and daily windows.

    - **Specific Parameters**   
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_btc_light_stats(window="day", limit=365)
```

### Ethereum [:arrow_up:](#cryptoquant-sdk)

#### ETH Entity Status [:arrow_up:](#cryptoquant-sdk)

- **Entities**: Returns the list of Ethereum-related entities, such as exchanges, banks, etc.  
    - Parameters:  
        - ```type_```(str): Required — Specifies the entity type to query.  
          For exchange entities, the `market_type` field indicates whether the exchange operates in the **spot** or **derivatives** market.  
          Entities without a `market_type` (e.g., miners) will return `0` for this field.  
        - ```format_```(str): Optional — Default: `json`. Defines the response format. Supported formats: `json`, `csv`.  
    - Usage:  
```python
resp = client.get_eth_entity_list(type_="exchange")
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

- **Exchange Reserve**: Returns the full historical on-chain balance of Ethereum exchanges. This metric represents the total amount of ETH held in exchange wallets over time and is commonly used to analyze accumulation or distribution trends among market participants. A decreasing exchange reserve may indicate withdrawals to cold wallets (bullish signal), while an increasing reserve can imply potential selling pressure.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Name of the exchange supported by CryptoQuant (e.g., `binance`, `kraken`, `bitmex`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_exch_reserve(exchange="binance")
```

- **Exchange Netflow**: Returns the difference between ETH flowing into exchanges and ETH flowing out of exchanges. This metric helps identify whether coins are moving toward exchanges (potential selling pressure) or being withdrawn to external wallets (potential accumulation). Positive netflow indicates more ETH entering exchanges, while negative netflow indicates more ETH leaving them.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Name of the exchange supported by CryptoQuant (e.g., `binance`, `kraken`, `bitmex`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_exch_netflow(exchange="kraken", window="day", limit=90)
```

- **Exchange Inflow**: Returns the total inflow of ETH into exchange wallets over time. This metric measures the amount of ETH deposited to exchanges and helps identify potential increases in selling pressure or liquidity movements. Higher inflows often suggest traders are preparing to sell or rebalance positions on centralized exchanges.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Name of the exchange supported by CryptoQuant (e.g., `binance`, `kraken`, `bitmex`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_exch_inflow(exchange="bitmex", window="day", limit=30)
```

- **Exchange Outflow**: Returns the total outflow of ETH from exchange wallets over time. This metric represents the amount of ETH withdrawn from exchanges, often interpreted as a signal of accumulation or reduced short-term selling pressure. Sustained high outflows may indicate investor confidence and long-term holding behavior.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Name of the exchange supported by CryptoQuant (e.g., `binance`, `kraken`, `bitmex`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_exch_outflow(exchange="bitmex", window="day", limit=30)
```

- **Exchange Transaction Count**: Returns the total number of transactions flowing in and out of Ethereum exchanges within a given time window. This metric reflects the overall activity of exchange wallets and can indicate shifts in user behavior or liquidity dynamics. A surge in transaction count may signal increased market participation or heightened volatility.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Name of the exchange supported by CryptoQuant (e.g., `binance`, `kraken`, `bitmex`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_exch_trx_count(exchange="bitmex", window="day", limit=90)
```

- **Exchange Addresses Count**: Returns the number of unique addresses involved in inflow and outflow transactions for Ethereum exchanges. This metric indicates the level of on-chain activity interacting with exchange wallets and can be used to gauge participation intensity or wallet concentration dynamics over time.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Name of the exchange supported by CryptoQuant (e.g., `binance`, `kraken`, `bitmex`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_exch_addrs_count(exchange="binance", window="day", limit=60)
```

#### ETH Flow Indicators [:arrow_up:](#cryptoquant-sdk)


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

- **Exchange Supply Ratio**: Calculates the proportion of ETH reserves held on exchanges relative to the total circulating supply. This metric helps assess how much of the overall supply is kept in exchange wallets and is often used to gauge market liquidity and potential selling pressure. A lower ratio generally suggests reduced exchange-held supply, implying stronger long-term holding sentiment.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Name of the exchange supported by CryptoQuant (e.g., `binance`, `kraken`, `bitmex`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_flow_exch_supply_ratio(exchange="kraken", window="day", limit=180)
```

#### ETH Market Indicators [:arrow_up:](#cryptoquant-sdk)


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

- **Estimated Leverage Ratio**: Estimates the average leverage level of traders on a given exchange by dividing its open interest by the exchange’s ETH reserve. This ratio provides a refined view of market sentiment—higher values suggest aggressive positioning and potential volatility, while lower values indicate more conservative behavior. Unlike raw open interest, this metric adjusts for the growth of the exchange’s reserves, offering a normalized perspective on leverage exposure.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Name of the exchange supported by CryptoQuant (e.g., `binance`, `kraken`, `bitmex`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_mkt_estimated_leverage_ratio(exchange="bitmex", window="day", limit=90)
```

#### ETH 2.0 [:arrow_up:](#cryptoquant-sdk)
Genesis event of ETH 2.0 requires at least 16,384 of 32-ETH validator deposits seven days before Dec 1. If not, the genesis event would postpone seven days after. CQ have only valid transactions in the calculations. Looking at the ETH2 deposit contract, Only from 32 to 1000 deposits are considered as valid deposits. When Phase 0 success rate hits 100% and Phase 0 unique validator hits 16,384, the Ethereum genesis event starts.

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

- **Total Value Staked**: Returns the valid ETH balance of the Ethereum 2.0 deposit contract. This metric represents the total amount of ETH locked for staking and actively participating in network validation. An increasing value staked indicates growing validator participation and overall network security, while stagnation or decline can signal reduced staking activity or withdrawals post-Shanghai upgrade.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_20_total_value_staked(window="day", limit=90)
```

- **Total Inflow Staking**: Returns the total amount of ETH deposited into the Ethereum 2.0 deposit contract within the selected time window. This metric tracks staking inflows, helping identify trends in validator onboarding and overall network participation. Higher inflows indicate increased staking activity and confidence in network rewards or security.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_20_total_inflow_staking(window="day", limit=60)
```

- **Staking Transaction Count**: Returns the total number of valid transactions sent to the Ethereum 2.0 deposit contract. This metric measures how many staking deposits occurred within a given period and can be used to assess validator onboarding activity and overall staking momentum.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_20_staking_trx_count(window="day", limit=30)
```

- **Validator Count Total**: Returns the total number of active validators participating in Ethereum 2.0 staking. This metric reflects the size and decentralization of the validator set. A growing number of validators generally indicates stronger network participation and security, while plateaus may suggest saturation or changing staking incentives.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_20_staking_validator_total(window="day", limit=180)
```

- **Depositor Count Total**: Returns the total number of unique accounts that have deposited at least 32 ETH into the Ethereum 2.0 deposit contract. This metric indicates the total number of independent staking participants and serves as a proxy for network decentralization and validator diversity.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_20_depositor_count_total(window="day", limit=180)
```

- **Depositor Count New**: Returns the number of new unique accounts that deposited at least 32 ETH into the Ethereum 2.0 deposit contract during the selected time window. This metric highlights the pace of new validator entries and provides insight into the growth rate of staking participation over time.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_20_depositor_count_new(window="day", limit=90)
```

- **Staking Rate**: Returns the percentage of the total ETH supply currently locked in the Ethereum 2.0 deposit contract. This metric measures the share of circulating ETH actively staked, providing insights into network participation and capital commitment. A higher staking rate generally reflects stronger confidence in protocol stability and long-term yield expectations.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_20_staking_rate(window="day", limit=90)
```

- **Phase 0 Success Rate**: Returns the percentage of the valid ETH balance in the Ethereum 2.0 deposit contract relative to the initial 524,288 ETH target required for network activation. This metric historically indicated the progress toward launching the Beacon Chain and can still be referenced to assess staking milestones and validator participation thresholds.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_20_phase_0_success_rate(window="day", limit=180)
```

#### ETH Fund Data [:arrow_up:](#cryptoquant-sdk)
Retreive metrics related to regulated funds such as trust, including market price, market volume, market premium, and digital asset holdings. These metrics are useful to measure sentiments of investors such as institutions in regulated market. All Symbol will be updated no later then UTC 12:00, this may be changed depending on update time of source data. Also the return value may be changed because of late updated fund.

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

**Supported Symbols**  
| Fund Name | Symbol | Source | Status |
| :--- | :--- | :--- | :--- |
| All Symbol (ETH) | `all_symbol` | All Fund | Validated |
| Grayscale Ethereum Trust | `ethe` | Grayscale Investments | Validated |
| Grayscale Ethereum Mini Trust | `eth` | Grayscale Investments | Validated |
| iShares Ethereum Trust ETF | `etha` | BlackRock | Validated |
| Fidelity Ethereum Fund ETF | `feth` | Fidelity | Validated |
| Bitwise Ethereum ETF | `ethw` | Bitwise | Validated |
| 21Shares Ethereum Core ETP | `ceth` | 21Shares | Validated |
| Invesco Galaxy Ethereum ETF | `qeth` | Invesco | Validated |
| VanEck Ethereum ETF | `ethv` | VanEck | Validated |
| Franklin Ethereum ETF | `ezet` | Franklin Templeton | Validated |
| Purpose Ether ETF | `ethh_u` | Purpose Investments | Validated |

- **Fund Market Price**: Returns USD-denominated price metrics for regulated Ethereum-related funds (e.g., ETHE, ETHA, FETH). This endpoint provides five metrics per time window: `price_usd_open`, `price_usd_close`, `price_usd_high`, `price_usd_low`, and `price_usd_adj_close`. These values represent the market valuation of ETH-backed products and are useful for assessing investor sentiment and pricing dynamics in traditional financial markets.

    - **Specific Parameters**  
        - ```symbol```(str): Required — Fund symbol to query (e.g., `ethe`, `feth`, `ethv`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_fund_market_price(symbol="ethe", window="day", limit=90)
```

- **Fund Market Volume**: Returns the traded volume of Ethereum-related fund stocks (e.g., ETHE, FETH, ETHV) in USD. This metric reflects investor sentiment and trading activity in regulated markets. The data is aggregated daily, providing one metric — `volume` — which represents the total traded volume within each time window.

    - **Specific Parameters**  
        - ```symbol```(str): Required — Fund symbol to query (e.g., `ethe`, `feth`, `ethv`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_fund_market_volumen(symbol="ethv", window="day", limit=60)
```

- **Fund Market Premium**: Returns the premium of Ethereum-related fund symbols (e.g., ETHE, ETHA, FETH) relative to their Net Asset Value (NAV). The premium is calculated as `(market price - NAV) / NAV`, where NAV represents the current value of underlying holdings (ETH price × ETH per share). A higher premium indicates bullish market sentiment but also increased downside risk, while a lower premium indicates bearish sentiment with potential upside. The `All Symbol` premium is derived using the Volume Weighted Average Ratio (VWAP) across all validated funds.

    - **Specific Parameters**  
        - ```symbol```(str): Required — Fund symbol to query (e.g., `ethe`, `etha`, `ethv`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_fund_market_premium(symbol="etha", window="day", limit=90)
```

- **Fund Digital Asset Holdings**: Returns the total ETH holdings of each regulated fund (e.g., ETHE, ETHA, CETH). This metric represents the amount of ETH held by institutional investment vehicles such as trusts and ETFs. Larger holdings generally indicate stronger institutional demand and bullish sentiment in traditional markets, while reductions can signal redemptions or decreased investor exposure.

    - **Specific Parameters**  
        - ```symbol```(str): Required — Fund symbol to query (e.g., `ethe`, `ceth`, `ethv`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_fund_digital_asset_holdings(symbol="ceth", window="day", limit=180)
```

#### ETH Market Data [:arrow_up:](#cryptoquant-sdk)
CQ provide USD and USDT spot price of ETH from global exchanges and ETH index price. CryptoQuant's ETH index price is VWAP(Volume Weighted Average Price) of aggregated price data from all exchanges we provide. For more detailed information, please refer to the description of each metric.

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

Supported Exchanges By Market

| Name | Market | Supported Exchanges |
| :--- | :--- | :--- |
| Spot | `spot` | All Exchange\*, Binance, Binance US, Bitfinex, Bittrex, Coinbase Advanced, FTX\*\*, Gemini, HTX Global, Kraken, OKX |
| Perpetual | `perpetual` | All Exchange\*, Binance, Bitmex, Bybit, Deribit, FTX\*\*, HTX Global, OKX |

\* Default exchange
\*\* Use in cautions due to the deprecation (no data update)

Supported Pairs By Exchange
- Spot

| Name | Exchange | Symbol | Volume Unit | Available Since |
| :--- | :--- | :--- | :--- | :--- |
| All Exchange | `all_exchange` | `eth_usd` | ETH | The earliest time in the exchanges below. |
| Binance | `binance` | `eth_usd` `eth_usdt` | ETH | 2017-08-17 04:00:00 |
| Binance US | `binance_us` | `eth_usd` `eth_usdt` | ETH | 2019-09-18 14:58:00 2019-09-23 08:36:00 |
| Bitfinex | `bitfinex` | `eth_usd` `eth_usdt` | ETH | 2016-03-09 16:04:00 2019-03-11 10:03:00 |
| Bittrex | `bittrex` | `eth_usd` `eth_usdt` | USD USDT | 2018-06-21 02:17:00 2017-04-21 13:30:00 |
| Coinbase Advanced | `coinbase_advanced` | `eth_usd` | ETH | 2016-05-18 00:14:00 |
| FTX** | `ftx` | `eth_usd` `eth_usdt` | USD USDT | 2019-09-14 21:07:00 2020-03-28 14:40:00 |
| Gemini | `gemini` | `eth_usd` | ETH | 2019-08-30 00:00:00 |
| HTX Global | `htx_global` | `eth_usd` `eth_usdt` | ETH | 2019-11-19 00:00:00 |
| Kraken | `kraken` | `eth_usd` `eth_usdt` | ETH | 2015-08-07 14:03:00 2019-12-19 16:49:00 |
| OKX | `okx` | `eth_usd` `eth_usdt` | ETH | 2019-10-01 00:00:00 |

\*\* Use in cautions due to the deprecation (no data update)

| Market | Supported Windows |
| :--- | :--- |
| Spot | `min`, `hour`, `day`* |
| Perpetual | `min`, `hour`, `day`* |

\* Default symbol

- **Market OHLCV**: Returns Open, High, Low, Close, and Volume (OHLCV) metrics for Ethereum prices. This endpoint provides two types of prices: CryptoQuant’s ETH Index Price and the USD or USDT price aggregated from global exchanges. Metrics are available for minute, hour, and day intervals. The OHLCV dataset includes five metrics per window: `open` (opening price), `close` (closing price), `high` (highest price), `low` (lowest price), and `volume` (total traded volume). The ETH Index Price is calculated as the Volume Weighted Average Price (VWAP) of ETH data aggregated across all supported exchanges.

    - **Specific Parameters** 
        - ```market```(str): Optional - Market type, `spot` or `perpetual`
        - ```exchange```(str): Optional — Name of the exchange (e.g., `binance`, `kraken`, `bitmex`). Defaults to aggregated index data if not specified.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_mkt_ohlcv(exchange="binance", window="day", limit=180)
```

- **Market Open Interest**: Returns ETH perpetual futures open interest from major derivative exchanges. This metric represents the total value of outstanding derivative contracts and is standardized to USD across exchanges, regardless of contract specifications. Rising open interest alongside price increases often indicates strong bullish sentiment, while rising open interest during price declines may suggest growing short positions.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Name of the derivatives exchange (e.g., `binance`, `bitmex`, `kraken`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_mkt_open_interest(exchange="bitmex", window="day", limit=90)
```

| Name | Exchange | Symbol | Available Since |
| :--- | :--- | :--- | :--- |
| All Exchanges | `all_exchange` | `all_symbol` | The earliest time in the exchanges below. |
| Binance | `binance` | `all_symbol` `eth_usd` `eth_usdt` | The earliest time in the symbols. 2020-08-18 00:00:00 2020-05-14 00:00:00 |
| Bitfinex | `bitfinex` | `all_symbol` `eth_usdt` | The earliest time in the symbols. 2020-06-01 00:00:00 |
| Bitmex | `bitmex` | `all_symbol` `eth_usd` | The earliest time in the symbols. 2019-03-30 00:00:00 |
| Bybit | `bybit` | `all_symbol` `eth_usd` `eth_usdt` | The earliest time in the symbols. 2019-11-07 00:00:00 2020-10-21 00:00:00 |
| Deribit | `deribit` | `all_symbol` `eth_usd` | The earliest time in the symbols. 2019-03-31 00:00:00 |
| FTX\*\* | `ftx` | `all_symbol` `eth_usd` | The earliest time in the symbols. 2020-05-09 00:00:00 |
| Gate.io | `gate_io` | `all_symbol` `eth_usd` `eth_usdt` | The earliest time in the symbols. 2020-07-01 00:00:00 2020-07-01 00:00:00 |
| HTX | `htx_global` | `all_symbol` `eth_usd` `eth_usdt` | The earliest time in the symbols. 2020-06-24 00:00:00 2021-08-26 05:00:00 |
| Kraken | `kraken` | `all_symbol` `eth_usd` | The earliest time in the symbols. 2019-03-30 00:00:00 |
| OKX | `okx` | `all_symbol` `eth_usd` `eth_usdt` | The earliest time in the symbols. 2019-09-05 00:00:00 2020-01-01 00:00:00 |

\*\* Use in cautions due to the deprecation (no data update)

- **Market Funding Rates**: Returns the funding rates of ETH perpetual swap markets across supported derivative exchanges. Funding rates represent trader sentiment and the balance between long and short positions. Positive funding rates indicate that traders are predominantly long (bullish) and pay funding to short traders, while negative rates indicate a bearish bias where short traders pay funding to longs.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Name of the derivatives exchange (e.g., `binance`, `bitmex`, `kraken`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_mkt_funding_rates(exchange="binance", window="day", limit=60)
```

| Name | Exchange | Symbol | Available Since |
| :--- | :--- | :--- | :--- |
| All Exchanges | `all_exchange` | | The earliest time in the exchanges below. |
| Binance | `binance` | ETH-USDT | 2019-11-29 00:00:00 |
| Bybit | `bybit` | ETH-USD | 2019-01-25 08:00:00 |
| Bitmex | `bitmex` | ETH-USD | 2018-08-02 12:00:00 |
| Deribit | `deribit` | ETH-PERPETUAL | 2019-10-04 00:00:00 |
| HTX Global | `htx_global` | ETH-USD | 2020-07-04 00:01:00 |
| OKX | `okx` | ETH-USD | 2019-04-02 02:00:00 |

- **Market Taker Buy/Sell Stats**: Returns taker-side trading statistics from ETH perpetual swap markets. These metrics reflect real-time trader sentiment and activity balance between buyers and sellers.  
  The dataset includes:  
  `taker_buy_volume` — total USD volume bought by takers,  
  `taker_sell_volume` — total USD volume sold by takers,  
  `taker_total_volume` — sum of buy and sell volume,  
  `taker_buy_ratio` — buy volume divided by total volume,  
  `taker_sell_ratio` — sell volume divided by total volume,  
  and `taker_buy_sell_ratio` — buy volume divided by sell volume.  
  All values are unified to USD across exchanges regardless of contract specifications.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Name of the derivatives exchange (e.g., `binance`, `bitmex`, `kraken`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_mkt_taker_buy_sell_stats(exchange="kraken", window="day", limit=90)
```

| Name | Exchange | Symbol | Available Since |
| :--- | :--- | :--- | :--- |
| All Exchanges | `all_exchange` | | The earliest time in the exchanges below. |
| Binance | `binance` | ETH-USDT | 2019-12-04 00:00:00 |
| Bybit | `bybit` | ETH-USD | 2019-12-04 00:00:00 |
| Bitmex | `bitmex` | ETH-USD | 2018-09-01 00:00:00 |
| Deribit | `deribit` | ETH-PERPETUAL | 2019-09-04 00:00:00 |
| HTX Global | `htx_global` | ETH-USD | 2020-04-18 00:00:00 |
| OKX | `okx` | ETH-USD | 2019-08-04 00:00:00 |

- **Market Liquidations**: Returns the total value of forced market orders (liquidations) triggered by price volatility in ETH perpetual markets. Liquidations occur when leveraged positions are forcibly closed, offering insights into trader sentiment and market stress. Large liquidation events typically correspond to high volatility periods. *Note:* Binance’s liquidation data collection policy changed on **2021-04-27**, which may cause a structural shift in the data distribution after that date.

    - **Specific Parameters**  
        - ```exchange```(str): Required — Name of the derivatives exchange (e.g., `binance`, `bitmex`, `kraken`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
    ```python
    resp = client.get_eth_mkt_liquidations(exchange="binance", window="day", limit=60)
    ```
| Name | Exchange | Symbol | Available Since |
| :--- | :--- | :--- | :--- |
| All Exchanges | `all_exchange` | `all_symbol` | The earliest time in the exchanges below. |
| Binance | `binance` | `all_symbol` `eth_usdt` `eth_usd` | The earliest time in the symbols. 2019-11-30 00:00:00 2020-08-21 00:00:00 |
| Bitfinex | `bitfinex` | `all_symbol` `eth_usdt` | The earliest time in the symbols. 2019-09-17 00:00:00 |
| Bitmex | `bitmex` | `all_symbol` `eth_usd` | The earliest time in the symbols. 2019-04-02 00:00:00 |
| Bybit | `bybit` | `all_symbol` `eth_usd` `eth_usdt` | The earliest time in the symbols. 2020-12-20 00:00:00 2020-12-18 00:00:00 |
| Deribit | `deribit` | `all_symbol` `eth_usd` | The earliest time in the symbols. 2019-05-25 00:00:00 |
| FTX** | `ftx` | `all_symbol` `eth_usd` | The earliest time in the symbols. 2019-08-04 00:00:00 |
| Gate.io | `gate_io` | `all_symbol` `eth_usd` `eth_usdt` | The earliest time in the symbols. 2018-12-28 11:00:00 2019-11-21 11:00:00 |
| HTX Global | `htx_global` | `all_symbol` `eth_usd` `eth_usdt` | The earliest time in the symbols. 2020-06-26 00:00:00 2021-09-23 14:00:00 |
| OKX | `okx` | `all_symbol` `eth_usd` `eth_usdt` | The earliest time in the symbols. 2020-12-20 00:00:00 2020-12-17 00:00:00 |

\*\* Use in cautions due to the deprecation (no data update)

- **Coinbase Premium Index**: Returns the Coinbase Premium Index and Premium Gap, which measure the price difference between Coinbase (ETH/USD) and Binance (ETH/USDT). The Coinbase Premium Index represents the percentage difference between the two prices, while the Coinbase Premium Gap represents the absolute gap in USD. A higher premium indicates stronger spot buying pressure from Coinbase, often reflecting heightened demand from U.S.-based institutional investors.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_mkt_coinbase_premium_index(window="day", limit=180)
```

- **Market Capitalization**: Returns the total market capitalization of Ethereum, calculated by multiplying the circulating supply by its USD price. This metric reflects the overall market valuation of ETH and is commonly used to gauge its relative size, growth, and dominance within the crypto asset class.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_mkt_capitalization(window="day", limit=180)
```

#### ETH Network Data [:arrow_up:](#cryptoquant-sdk)
Ethereum on-chain network data including but not limited to token movements, fees, supply, address movements, etc. All metrics have data entries starting from the genesis block (block height 0, datetime 2015-07-30 15:26:13).

#### Supply and Velocity [:arrow_up:](#cryptoquant-sdk)
Basic macroeconomic metrics that reflect the circulation and use of ETH.

- **Supply**: Returns metrics related to the total and newly issued supply of Ethereum. This endpoint provides two key metrics: `supply_total`, representing the total amount of ETH in existence (sum of all ETH issued through block rewards), and `supply_new`, representing the amount of newly issued ETH within the selected time window. These metrics help track ETH’s monetary base and inflation dynamics over time.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_supply(window="day", limit=365)
```

- **Velocity**: Returns metrics related to Ethereum’s monetary velocity. Velocity is calculated by dividing the trailing 1-year estimated transaction volume (the cumulative sum of transferred tokens) by the current supply. This metric indicates how actively ETH circulates in the economy — higher velocity suggests more transactional use, while lower velocity indicates a tendency toward holding or staking behavior.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_velocity(window="day", limit=180)
```

#### Contracts and Transactions [:arrow_up:](#cryptoquant-sdk)
Smart contract activity and transaction volume. Includes total count, EOA, internal/external contracts.

- **Contracts Count**: Returns metrics related to the number of smart contracts on the Ethereum network. This endpoint provides three key metrics: `contracts_created_new`, the number of newly created contracts; `contracts_destroyed_new`, the number of contracts destroyed; and `contracts_count_total`, the total unique number of existing contracts. These metrics help evaluate the growth and churn of the smart contract ecosystem over time.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_contracts_count(window="day", limit=180)
```

- **Transaction Count**: Returns metrics related to the number of transactions processed on the Ethereum network. This endpoint provides two key metrics: `transactions_count_total`, representing the total number of transactions within each time window, and `transactions_count_mean`, representing the average number of transactions. These metrics are useful for analyzing on-chain activity, throughput, and overall network utilization.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_trx_count(window="day", limit=180)
```

- **Transactions Between EOAs**: Returns the number of transactions occurring between Externally Owned Accounts (EOAs) on the Ethereum network. This metric isolates peer-to-peer activity, excluding smart contract interactions, and is useful for assessing organic user-driven transaction behavior.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_trx_eoa(window="day", limit=90)
```

- **Contract Calls External**: Returns the number of external smart contract calls executed on the Ethereum network. External contract calls are transactions initiated from Externally Owned Accounts (EOAs) to smart contracts. This metric helps measure user interaction with decentralized applications and on-chain protocols.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_trx_contract_calls_external(window="day", limit=90)
```

- **Contract Calls Internal**: Returns the number of internal smart contract calls on the Ethereum network. Internal calls occur when one smart contract interacts with another during transaction execution. This metric reflects the level of composability and complexity within decentralized applications and protocol interactions.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_trx_contract_calls_internal(window="day", limit=90)
```

- **Contract Calls Count**: Returns the total number of smart contract calls on the Ethereum network, including both internal and external calls. This metric provides a comprehensive view of smart contract activity and is useful for assessing overall dApp usage, protocol complexity, and on-chain computational demand.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_trx_contract_calls_count(window="day", limit=180)
```

- **Transaction Count (All)**: Returns the total number of Ethereum transactions, including both regular transactions and internal contract calls. This metric provides a complete picture of on-chain activity by capturing all executions occurring within the Ethereum network.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_trx_count_all(window="day", limit=180)
```

#### ETH Addresses [:arrow_up:](#cryptoquant-sdk)
Number of active addresses or participants.

- **Address Count**: Returns metrics related to the number of active Ethereum addresses. This endpoint provides three metrics: `addresses_count_active`, the total number of unique addresses active as either sender or receiver; `addresses_count_sender`, the number of addresses active as senders; and `addresses_count_receiver`, the number of addresses active as receivers. These metrics help measure network participation, user growth, and transaction activity dynamics.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_addr_count(window="day", limit=180)
```

- **Address Count (All)**: Returns metrics related to the number of used Ethereum addresses, including those involved in internal contract calls. This endpoint provides three metrics: `addresses_count_active`, the total number of unique addresses active as either sender or receiver; `addresses_count_sender`, the number of addresses active as senders; and `addresses_count_receiver`, the number of addresses active as receivers. This comprehensive metric captures both direct and contract-mediated activity, offering a full view of network address utilization.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_addr_count_all(window="day", limit=180)
```

#### Token Transfers [:arrow_up:](#cryptoquant-sdk)
Count and volume of transferred tokens, including EOAs, contracts, and totals.

- **Tokens Transferred Count**: Returns metrics related to the number of token transfer executions on the Ethereum network. This endpoint provides two metrics: `tokens_transferred_count_total`, representing the total number of token transfers executed, and `tokens_transferred_count_mean`, representing the average number of token transfers within the selected time window. These metrics are useful for assessing token activity, user interaction with ERC-20 contracts, and overall network utilization.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_tokens_transferred_count(window="day", limit=180)
```

- **Tokens Transferred Count (EOA)**: Returns the number of token transfer executions between Externally Owned Accounts (EOAs) on the Ethereum network. This metric isolates peer-to-peer token movements that exclude smart contract interactions, helping to analyze organic user-driven token activity and direct transfers between individual holders.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_tokens_transferred_count_eoa(window="day", limit=90)
```

- **Tokens Transferred Count (External Calls)**: Returns the number of token transfer executions triggered by external contract calls. These transactions are initiated from Externally Owned Accounts (EOAs) to smart contracts, reflecting user interactions with decentralized applications, DeFi protocols, and tokenized systems.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_tokens_transferred_count_calls_external(window="day", limit=90)
```

- **Tokens Transferred Count (Internal Calls)**: Returns the number of token transfer executions triggered by internal contract calls. These transfers occur when one smart contract interacts with another during transaction execution, reflecting the composability and internal activity of decentralized protocols on Ethereum.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_tokens_transferred_count_calls_internal(window="day", limit=90)
```

- **Tokens Transferred Count (All Contract Calls)**: Returns the number of token transfer executions triggered by smart contract calls, including both internal and external calls. This metric provides a comprehensive view of token movement facilitated through contract interactions, helping to assess overall DeFi and dApp transaction activity on Ethereum.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_tokens_transferred_count_calls(window="day", limit=90)
```

- **Tokens Transferred Count (All)**: Returns the total number of token transfer executions on the Ethereum network, including those triggered by internal contract calls. This metric captures all token movements across EOAs and smart contracts, offering a complete overview of token transfer activity and overall network usage.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_tokens_transferred_count_all(window="day", limit=180)
```

- **Tokens Transferred**: Returns metrics related to the total transaction volume of token transfers on the Ethereum network. This endpoint provides several metrics: `tokens_transferred_total`, the total number of tokens transferred within the window; `tokens_transferred_mean`, the average number of tokens transferred per transaction; and `tokens_transferred_median`, the median value of tokens transferred per transaction. All values are also available in USD units. These metrics help evaluate token flow intensity and economic activity within the Ethereum ecosystem.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_tokens_transferred(window="day", limit=180)
```

- **Tokens Transferred (EOA)**: Returns metrics related to the total transaction volume of token transfers between Externally Owned Accounts (EOAs). This endpoint isolates peer-to-peer token movements excluding smart contract interactions, providing insights into direct user-driven economic activity and organic token circulation on the Ethereum network.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_tokens_transferred_eoa(window="day", limit=90)
```

- **Tokens Transferred (External Calls)**: Returns metrics related to the transaction volume of token transfers executed through external contract calls. These transactions are initiated by Externally Owned Accounts (EOAs) interacting with smart contracts, and they reflect user engagement with decentralized applications, DeFi protocols, and tokenized ecosystems.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_tokens_transferred_calls_external(window="day", limit=90)
```

- **Tokens Transferred (Internal Calls)**: Returns metrics related to the transaction volume of token transfers executed through internal contract calls. These transfers occur when smart contracts interact with one another during execution, representing composable activity across DeFi protocols and automated on-chain processes within the Ethereum network.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_tokens_transferred_calls_internal(window="day", limit=90)
```

- **Tokens Transferred (All Contract Calls)**: Returns metrics related to the transaction volume of token transfers executed through smart contract calls, including both internal and external calls. This metric provides a complete view of token flow mediated by contract interactions, capturing activity across DeFi protocols, DEXs, and other on-chain applications.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_tokens_transferred_calls(window="day", limit=90)
```

- **Tokens Transferred (All)**: Returns metrics related to the total transaction volume of token transfers on the Ethereum network, including those executed through internal contract calls. This comprehensive metric captures all token movement — between EOAs and smart contracts — offering a complete picture of token flow and on-chain activity.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_tokens_transferred_all(window="day", limit=180)
```

#### Failed Transactions [:arrow_up:](#cryptoquant-sdk)
Monitoring failures in transactions and token transfers.

- **Failed Transaction Count**: Returns metrics related to the number of failed transactions on the Ethereum network. This endpoint provides the metric `failed_transactions_count_total`, representing the total number of transactions that did not successfully execute. Monitoring failed transactions helps assess network congestion, gas price inefficiencies, and smart contract execution errors.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_failed_trx_count(window="day", limit=90)
```

- **Failed Token Transfer Count**: Returns metrics related to the number of failed transactions involving token transfers. This endpoint provides the metric `failed_tokens_transferred_count_total`, representing the total number of token transfer transactions that failed to execute successfully. Tracking failed token transfers helps identify contract issues, gas misconfigurations, and stress conditions in ERC-20 token activity.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_failed_tokens_transferred_count(window="day", limit=90)
```

#### ETH Block Metrics [:arrow_up:](#cryptoquant-sdk)
Structural information of the blockchain: size, count, interval, rewards.

- **Block Bytes**: Returns the mean size (in bytes) of all blocks generated on the Ethereum network within the selected time window. This metric reflects the average block utilization and data throughput of the blockchain, helping to assess network congestion and on-chain activity density.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_block_bytes(window="day", limit=180)
```

- **Block Count**: Returns the total number of blocks generated on the Ethereum network within the selected time window. This metric helps evaluate block production consistency, network health, and potential variations in block generation rates over time.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_block_count(window="day", limit=180)
```

- **Block Interval**: Returns the average time (in seconds) between blocks generated on the Ethereum network within the selected time window. This metric reflects block production speed and can indicate changes in network difficulty, validator performance, or overall network conditions.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_block_interval(window="day", limit=180)
```

- **Block Reward**: Returns the total sum of block rewards generated on the Ethereum network, including both mining or staking rewards and transaction fees. The value is also available in USD units. This metric provides insight into validator/miner incentives and overall network revenue distribution within the selected time window.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_blockreward(window="day", limit=180)
```

- **Block Reward (Excluding Uncle Blocks)**: Returns the total sum of block rewards on the Ethereum network, excluding uncle blocks. The value is also provided in USD units. This metric isolates rewards from successfully validated canonical blocks, helping to analyze validator earnings and network efficiency without the influence of uncle block rewards.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_blockreward_except_uncle(window="day", limit=180)
```

- **Uncle Block Count**: Returns the total number of uncle blocks generated on the Ethereum network within the selected time window. Uncle blocks are valid blocks that were not included in the main chain but still contribute to network security and decentralization. This metric helps evaluate block propagation efficiency and network latency.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_uncle_block_count(window="day", limit=180)
```

- **Uncle Block Reward**: Returns the total sum of uncle block rewards on the Ethereum network, including mining or staking rewards and transaction fees. The value is also available in USD units. This metric provides insight into the additional rewards distributed for uncle blocks, reflecting network redundancy and participation efficiency.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_uncle_blockreward(window="day", limit=180)
```

#### Fees and Gas Metrics [:arrow_up:](#cryptoquant-sdk)
Network usage cost, burns, tips, and base/maximum fees.

- **Fees**: Returns statistics related to transaction fees paid on the Ethereum network. This endpoint provides three metrics: `fees_total`, the total sum of all fees; `fees_block_mean`, the average fee per block; and `fees_reward_percent`, the percentage of total fees relative to the overall block reward. All metrics are provided in both ETH and USD units. These values help assess network congestion, user demand, and miner/validator revenue composition.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_fees(window="day", limit=180)
```

- **Fees Burnt**: Returns statistics related to the total amount of transaction fees burnt on the Ethereum network, introduced after the London upgrade (EIP-1559). This endpoint provides two metrics: `fees_burnt_total` (in ETH) and `fees_burnt_total_usd` (in USD). Data is available from block height **12,965,000** (timestamp: *2021-08-05 12:33:42 UTC*) onward. These metrics reflect ETH’s deflationary pressure and the impact of fee-burning on overall supply dynamics.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_fees_burnt(window="day", limit=180)
```

- **Fees Tips**: Returns statistics related to transaction fees directly paid to Ethereum miners (or validators), introduced after the London upgrade (EIP-1559). This endpoint provides two metrics: `fees_tips_total` (in ETH) and `fees_tips_total_usd` (in USD). Data is available from block height **12,965,000** (timestamp: *2021-08-05 12:33:42 UTC*) onward. These metrics represent miner/validator revenue from priority fees and help assess transaction urgency dynamics post-upgrade.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_fees_tips(window="day", limit=180)
```

- **Fees per Transaction**: Returns statistics related to the fees paid per transaction on the Ethereum network. This endpoint provides two metrics: `fees_transaction_mean`, the average fee per transaction, and `fees_transaction_median`, the median fee per transaction. Both metrics are available in ETH and USD units. These values are useful for analyzing transaction cost trends and user behavior during varying network congestion levels.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_fees_trx(window="day", limit=180)
```

- **Fees per Transaction (Burnt)**: Returns statistics related to the average and median amount of transaction fees burnt on the Ethereum network, introduced after the London upgrade (EIP-1559). This endpoint provides two metrics: `fees_burnt_transaction_mean`, the average burnt fee per transaction, and `fees_burnt_transaction_median`, the median burnt fee per transaction. Both metrics are available in ETH and USD units. Data is available from block height **12,965,000** (timestamp: *2021-08-05 12:33:42 UTC*) onward.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_fees_trx_burnt(window="day", limit=180)
```

- **Fees per Transaction (Tips)**: Returns statistics related to the average and median amount of transaction fees directly paid to Ethereum miners or validators, introduced after the London upgrade (EIP-1559). This endpoint provides two metrics: `fees_tips_transaction_mean`, the average tip fee per transaction, and `fees_tips_transaction_median`, the median tip fee per transaction. Both metrics are available in ETH and USD units. Data is available from block height **12,965,000** (timestamp: *2021-08-05 12:33:42 UTC*) onward.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_fees_trx_tips(window="day", limit=180)
```

- **Gas**: Returns statistics related to gas usage across all Ethereum transactions. This endpoint provides four metrics: `gas_used_total`, the total amount of gas used; `gas_used_mean`, the average amount of gas used; `gas_price_mean`, the average gas price (in Gwei per gas); and `gas_limit_mean`, the average gas limit. These metrics are essential for analyzing network efficiency, transaction cost dynamics, and gas utilization trends over time.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_gas(window="day", limit=180)
```

- **Base Fee**: Returns the base fee per gas used to burn transaction fees on the Ethereum network, introduced after the London upgrade (EIP-1559). This endpoint provides the metric `base_fee_mean`, representing the average base fee per gas (in Gwei) over the selected blocks. The base fee is a critical component of Ethereum’s fee mechanism, determining the portion of transaction fees that are permanently burnt.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_base_fee(window="day", limit=180)
```

- **Max Fee**: Returns the maximum fee per gas that users are willing to pay when submitting transactions, introduced after the London upgrade (EIP-1559). This endpoint provides the metric `max_fee_mean`, representing the average maximum fee per gas (in Gwei) across transactions within the selected time window. This metric helps evaluate users’ willingness to pay for block inclusion and their response to network congestion.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_max_fee(window="day", limit=180)
```

- **Max Priority Fee**: Returns the maximum priority fee per gas paid as a tip to miners or validators, introduced after the London upgrade (EIP-1559). This endpoint provides the metric `max_priority_fee_mean`, representing the average maximum priority fee per gas (in Gwei) across transactions within the selected time window. This metric helps analyze user incentives for faster transaction inclusion and the dynamics of priority bidding in the Ethereum network.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_max_priority_fee(window="day", limit=180)
```

#### ETH Mining and Network Performance [:arrow_up:](#cryptoquant-sdk)
Difficulty, hash rate, and other security/block processing indicators.

- **Difficulty**: Returns the mean mining difficulty for new blocks on the Ethereum network within the selected time window. This metric reflects how computationally hard it was to mine a block and serves as an indicator of network security and total hash power participation, particularly relevant for the pre-Merge Proof-of-Work era.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_difficulty(window="day", limit=180)
```

- **Hashrate**: Returns the mean speed at which miners on the Ethereum network solved cryptographic hash problems, measured in gigahashes per second (GH/s). This metric represents the total computational power securing the network and is a key indicator of network security and miner participation during the Proof-of-Work era.

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.

    - **Usage**  
```python
resp = client.get_eth_ntx_hashrate(window="day", limit=180)
```

### XRP [:arrow_up:](#cryptoquant-sdk)

| Section Name | Objective | Number of Endpoints |
| :------------ | :--------- | :----------------: |
| **Entity List** | Provides a list of available entities (e.g., exchanges) for which XRP data can be retrieved. Serves as the reference entry point for other entity-based metrics. | 1 |
| **Entity Flows** | Tracks XRP movements between entities, including reserves, inflows, outflows, and address activity. Helps analyze accumulation, distribution, and network liquidity flows. | 7 |
| **Flow Indicators** | Measures the composition and distribution of inflows/outflows across exchanges, as well as their ratio to total supply. Useful for understanding capital concentration and flow dynamics. | 5 |
| **Market Data** | Covers XRP market performance metrics, including OHLCV prices, open interest, funding rates, taker activity, liquidations, capitalization, and leverage ratio. | 7 |
| **Network Data** | Provides on-chain activity and protocol-level metrics such as active addresses, velocity, fees, supply, and transaction volume. Used to assess network health and utilization. | 7 |
| **Network Indicator** | Contains the NVT Ratio (Network Value to Transaction), a valuation indicator comparing market cap to transaction activity. | 1 |
| **DEX Data** | Focuses on the XRPL Decentralized Exchange (DEX), including on-chain price, liquidity, trading volume, and transaction count. | 4 |
| **AMM Data** | Provides analytics for Automated Market Makers (AMMs) on XRPL, including price, liquidity, fees, and swap statistics for validated non-XRP/XRP pairs. | 4 |


#### XRP Entity Status [:arrow_up:](#cryptoquant-sdk)

- **Entities**: Returns tentity list to serve data. 
    - Parameters:  
        - ```type_```(str): Required — Specifies the entity type to query.  
          For exchange entities, the `market_type` field indicates whether the exchange operates in the **spot** or **derivatives** market.  
          Entities without a `market_type` (e.g., miners) will return `0` for this field.  
        - ```format_```(str): Optional — Default: `json`. Defines the response format. Supported formats: `json`, `csv`.  
    - Usage:  
```python
resp = client.get_eth_entity_list(type_="exchange")
```

| Entity Type | Description |
| :--- | :--- |
| exchange | centralized exchange |
| builder | entities contributing to xrp ledger |
| team | xrp project related team or related individuals |
| foundation | xrp foundation |
| custody | custody service |
| otc | otc service |
| bank | bank |
| bridge | bridge |

#### XRP Entity Flows [:arrow_up:](#cryptoquant-sdk)
Retrieve metrics related to XRP Entity Flows. Currently, CQ only supports Exchanges for available entities:

| Name |
| :--- |
| Binance |
| Bitfinex |
| Bitget |
| Bithumb |
| Bitstamp |
| Bybit |
| Gate.io |
| HTX Global |
| Kucoin |
| OKX |
| Upbit |

**Note:** These methods does not support Point-In-Time (PIT) accuracy due to periodic updates to wallet address clustering. Historical data may change as new exchange wallets are discovered, added, and validated.

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

- **Entity Reserve**: Returns the full historical on-chain balance of XRP Ledger entities. This metric reflects the amount of XRP held in each supported entity wallet (e.g., exchanges or custodians) over time.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Entity or exchange supported by CryptoQuant (e.g., `binance`, `bitstamp`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_entity_reserve(exchange="binance")
```

- **Entity Share**: Returns the proportion of XRP held by each entity relative to the total circulating supply. This metric is calculated by dividing the XRP holdings of the entity by the total XRP supply, providing insight into concentration and market share among major holders.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Entity or exchange supported by CryptoQuant (e.g., `binance`, `bitstamp`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_entity_share(exchange="binance")
```

- **Entity Transaction Count**: Returns the total number of transactions flowing into or out of XRP entities. This metric captures the on-chain activity level of exchange wallets and other major entities, helping identify changes in transaction behavior over time.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Entity or exchange supported by CryptoQuant (e.g., `binance`, `bitstamp`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_entity_trx_count(exchange="binance")
```

- **Entity Inflow**: Returns the total inflow of XRP into entity wallets for as far back as available. This metric measures the amount of XRP deposited into the addresses of supported entities, indicating accumulation pressure or exchange deposit activity.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Entity or exchange supported by CryptoQuant (e.g., `binance`, `bitstamp`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_entity_inflow(exchange="binance")
```

- **Entity Outflow**: Returns the total outflow of XRP from entity wallets for as far back as available. This metric measures the amount of XRP withdrawn from the addresses of supported entities, indicating distribution pressure or withdrawal activity from exchanges.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Entity or exchange supported by CryptoQuant (e.g., `binance`, `bitstamp`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_entity_outflow(exchange="binance")
```

- **Entity Addresses Count**: Returns the number of unique addresses involved in inflow or outflow transactions for a given entity. This metric reflects the breadth of wallet activity interacting with exchange or entity addresses over time.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Entity or exchange supported by CryptoQuant (e.g., `binance`, `bitstamp`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_entity_addrs_count(exchange="binance")
```

- **Entity Whale Movements**: Returns the number of large transactions and their corresponding transfer volumes related to entity inflows and outflows. This metric tracks whale activity within the XRP Ledger, providing insights into significant on-chain movements that may influence market liquidity and sentiment.  

    - **Specific Parameters**  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_entity_whale_movements(window="day")
```

#### XRP Flow Indicators [:arrow_up:](#cryptoquant-sdk)
Rretrieve metrics related to XRP Flow Indicators.

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

- **Exchange Inflow Value Distribution**: Shows the distribution of XRP inflows into exchange wallets categorized by transfer value. This metric highlights how deposited amounts are segmented across different transaction sizes, helping identify accumulation behavior and deposit concentration patterns.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange supported by CryptoQuant (e.g., `binance`, `bitstamp`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_flow_exch_inflow_value_dstr(exchange="binance")
```

- **Exchange Outflow Value Distribution**: Shows the distribution of XRP outflows from exchange wallets categorized by transfer value. This metric illustrates how withdrawn amounts are segmented across different transaction sizes, helping detect large-scale withdrawals or distribution activity.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange supported by CryptoQuant (e.g., `binance`, `bitstamp`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_flow_exch_outflow_value_dstr(exchange="binance")
```

- **Exchange Inflow Count Value Distribution**: Shows the number of XRP transactions flowing into exchange wallets, categorized by value segment. This metric reflects how frequently deposits of different sizes occur, helping identify retail versus institutional deposit activity patterns.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange supported by CryptoQuant (e.g., `binance`, `bitstamp`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_flow_exch_inflow_count_value_dstr(exchange="binance")
```

- **Exchange Outflow Count Value Distribution**: Shows the number of XRP transactions flowing out of exchange wallets, categorized by value segment. This metric reflects how frequently withdrawals of different sizes occur, helping identify patterns of distribution, liquidity movement, or large-scale capital exits from exchanges.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange supported by CryptoQuant (e.g., `binance`, `bitstamp`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_flow_exch_outflow_count_value_dstr(exchange="binance")
```

- **Exchange Supply Ratio**: Represents the ratio of XRP reserves held on exchanges compared to the total circulating supply of XRP. This metric helps evaluate how much of the total supply is stored on trading platforms, offering insight into liquidity availability and potential sell-side pressure.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Exchange supported by CryptoQuant (e.g., `binance`, `bitstamp`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_flow_exch_supply_ratio(exchange="binance")
```

#### XRP Market Data [:arrow_up:](#cryptoquant-sdk)
Rretrieve metrics related to XRP Market Data.

- Supported Exchanges By Market

| Name | Market | Supported Exchanges |
| :--- | :--- | :--- |
| Spot | `spot` | All Exchange*, Binance, Binance US, Bitfinex, Kucoin, Coinbase Advanced, Kraken, HTX Global |
| Perpetual | `perpetual` | All Exchange*, Binance, Deribit, Bitmex, OKX |

\* Default exchange

Supported Pairs By Exchange
- Spot

| Name | Exchange | Symbol |
| :--- | :--- | :--- |
| All Exchanges | `all_exchange` | `xrp_usd` * |
| Binance | `binance` | `xrp_usdt` `xrp_fdusd` `xrp_btc` `xrp_eth` `xrp_bnb` `xrp_rub` `xrp_tusd` |
| Binance US | `binance_us` | `xrp_usdt` * |
| Coinbase Advanced | `coinbase_advanced` | `xrp_eur` `xrp_usdt` `xrp_usd` * |
| Bitfinex | `bitfinex` | `xrp_usdt` `xrp_btc` `xrp_usd` * |
| HTX Global | `htx_global` | `xrp_usdt` * |
| Kucoin | `kucoin` | `xrp_usdc` `xrp_tusd` `xrp_btc` `xrp_eth` `xrp_usdt` * |
| Kraken | `kraken` | `xrp_usdt` `xrp_eur` `xrp_aud` `xrp_eth` `xrp_btc` `xrp_usd` * |

- Perpetual

| Name | Exchange | Symbol |
| :--- | :--- | :--- |
| All Exchanges | `all_exchange` | `xrp_usd` * `xrp_usdt` |
| Binance | `binance` | `xrp_usd` * |
| Deribit | `deribit` | `xrp_usdc` * |
| Okx | `okx` | `xrp_usdt` * |
| Bitmex | `bitmex` | `xrp_usdt` `xrp_usd` * |

- Supported Windows By Market

| Market | Supported Windows |
| :--- | :--- |
| Spot | `min`, `hour`, `day`* |
| Perpetual | `min`, `hour`, `day`* |

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

- **Price OHLCV**: Returns XRP price metrics including open, high, low, close, and volume (OHLCV). This dataset provides the USD-denominated opening price at the start of each window, the closing price at the end, the highest and lowest prices within the interval, and the total traded token volume.  

    - **Specific Parameters**  
        - ```market```(str): Optional — Market type supported by CryptoQuant.  
        - ```exchange```(str): Optional — Exchange supported by CryptoQuant (e.g., `binance`, `bitstamp`, `okx`).  
        - ```symbol```(str): Optional — XRP trading pair symbol supported by CryptoQuant.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_mkt_ohlcv(exchange="binance", window="day")
```

- **Open Interest**: Returns the total XRP perpetual open interest from supported derivative exchanges. This metric measures the total value of outstanding perpetual futures contracts, reflecting traders’ participation level and leveraged exposure in the market.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Derivative exchange supported by CryptoQuant (e.g., `binance`, `bybit`, `okx`).  
        - ```symbol```(str): Optional — XRP trading pair symbol supported by CryptoQuant.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_mkt_open_interest(exchange="binance")
```

| Name | Exchange | Symbol |
| :--- | :--- | :--- |
| All Exchanges | `all_exchange` | `all_symbol` * |
| Binance | `binance` | `xrp_usdt` `xrp_usd` `all_symbol` * |
| Bybit | `bybit` | `xrp_usdt` `xrp_usd` `all_symbol` * |
| Bitmex | `bitmex` | `xrp_usd` * |
| HTX Global | `htx_global` | `xrp_usd` * |
| OKX | `okx` | `xrp_usdt` `xrp_usd` `all_symbol` * |


- **Funding Rates**: Represents traders’ sentiment in the perpetual swaps market. Positive funding rates indicate a bullish bias, where long traders pay funding to short traders. Negative rates indicate a bearish bias, where short traders pay funding to long traders. This metric helps assess market positioning and directional conviction among leveraged traders.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Derivative exchange supported by CryptoQuant (e.g., `binance`, `bybit`, `okx`).  
        - ```symbol```(str): Optional — XRP trading pair symbol supported by CryptoQuant.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_mkt_funding_rates(exchange="binance")
```

| Name | Exchange | Symbol |
| :--- | :--- | :--- |
| All Exchanges | `all_exchange` | `all_symbol` * |
| Binance | `binance` | `xrp_usdt` `xrp_usd` `all_symbol` * |
| Bybit | `bybit` | `xrp_usdt` `xrp_usd` `all_symbol` * |
| Bitmex | `bitmex` | `xrp_usd` * |
| HTX Global | `htx_global` | `xrp_usd` * |
| OKX | `okx` | `xrp_usdt` `xrp_usd` `all_symbol` * |

- **Taker Buy/Sell Stats**: Represents takers’ sentiment and positioning in the perpetual swaps market. This metric aggregates taker-side trades to quantify buy and sell activity:  
  - `taker_buy_volume`: volume bought by takers.  
  - `taker_sell_volume`: volume sold by takers.  
  - `taker_total_volume`: total traded volume by takers.  
  - `taker_buy_ratio`: `taker_buy_volume` / `taker_total_volume`.  
  - `taker_sell_ratio`: `taker_sell_volume` / `taker_total_volume`.  
  - `taker_buy_sell_ratio`: `taker_buy_volume` / `taker_sell_volume`.  
  All returned values are standardized in USD to ensure cross-exchange comparability.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Derivative exchange supported by CryptoQuant (e.g., `binance`, `bybit`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_mkt_taker_buysell_stats(exchange="all_exchange")
```

| Name | Exchange | Symbol |
| :--- | :--- | :--- |
| All Exchanges | `all_exchange` | `all_symbol` * |
| Binance | `binance` | `xrp_usdt` * |
| Bybit | `bybit` | `xrp_usd` * |
| Bitmex | `bitmex` | `xrp_usd` * |
| HTX Global | `htx_global` | `xrp_usd` * |
| OKX | `okx` | `xrp_usd` * |

- **Liquidations**: Represents the total value of forced market orders used to close leveraged positions due to price volatility. This metric indicates market stress and reveals traders’ positioning bias — whether liquidations are concentrated on long or short positions.  
  *Note:* Binance’s liquidation data collection policy changed on **2021-04-27**, which may affect data distribution after that date.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Derivative exchange supported by CryptoQuant (e.g., `binance`, `bybit`, `okx`).  
        - ```symbol```(str): Optional — XRP trading pair symbol supported by CryptoQuant.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_mkt_liquidations(exchange="binance")
```

| Name | Exchange | Symbol |
| :--- | :--- | :--- |
| All Exchanges | `all_exchange` | `all_symbol` * |
| Binance | `binance` | `xrp_usdt` `xrp_usd` `all_symbol` * |
| Bybit | `bybit` | `xrp_usdt` `xrp_usd` `all_symbol` * |
| Bitmex | `bitmex` | `xrp_usd` * |
| HTX Global | `htx_global` | `xrp_usdt` * |
| OKX | `okx` | `xrp_usdt` `xrp_usd` `all_symbol` * |
| Bitfinex | `bitfinex` | `xrp_usdt` |

- **Market Capitalization**: Returns metrics related to the total market capitalization of XRP. The `market_cap` value represents the overall valuation of XRP, calculated by multiplying the total circulating supply by its USD price. This metric reflects the aggregate market value of XRP and is a key indicator of its relative scale and dominance within the crypto market.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_mkt_capitalization(window="day")
```

- **Estimated Leverage Ratio (ELR)**: Indicates how much leverage is used by traders on average across exchanges. It is calculated as the ratio of open interest divided by the exchange’s reserve balance. This metric provides insight into traders’ overall risk appetite — higher values suggest increased use of leverage and higher liquidation risk during volatility.  

  *Note:* This endpoint does **not** support Point-In-Time (PIT) accuracy due to periodic updates in wallet address clustering. Historical values may change as new exchange wallets are identified and validated.  

    - **Specific Parameters**  
        - ```exchange```(str): Required — Derivative exchange supported by CryptoQuant (e.g., `binance`, `bybit`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_mkt_estimated_leverage_ratio(exchange="binance")
```

#### XRP Network Data [:arrow_up:](#cryptoquant-sdk)
Retrieve metrics related to XRP Network Data.

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

- **Active Addresses Count**: Returns the number of active XRP addresses used on the network. This metric measures on-chain activity by counting distinct addresses involved in transactions within each time window, serving as a proxy for user activity and network utilization.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_ntx_addrs_count(window="day")
```

| Metric | Description |
| :--- | :--- |
| `addresses_count_active` | The total number of unique addresses that were active (either sender or receiver) on the blockchain in a given window. |
| `addresses_count_sender` | The number of addresses that were active as a sender. |
| `addresses_count_receiver` | The number of addresses that were active as a receiver. |


- **Velocity**: Measures how quickly XRP units circulate within the network. It is calculated by dividing the on-chain transaction volume by the market capitalization, effectively serving as the inverse of the NVT Ratio. Higher values indicate faster token turnover and greater transactional utility on-chain.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_ntx_velocity(window="day")
```

- **Block Interval**: Returns the average time between consecutive blocks (ledgers) generated on the XRP Ledger, expressed in seconds. This metric reflects the network’s block production rate and can be used to monitor performance or detect temporary slowdowns in block validation.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_ntx_block_interval()
```

- **XRP Burnt**: Returns the total amount of XRP that has been permanently removed (burned) from circulation. This metric tracks deflationary events on the XRP Ledger, often resulting from transaction fees or network-level burns, and reflects the long-term supply dynamics of the asset.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_ntx_burnt()
```

- **Ledger Count**: Returns the total number of ledgers (the XRP Ledger equivalent of “blocks”) created over time. This metric tracks the ongoing growth of the XRP Ledger and provides insight into its operational activity and block production consistency.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_ntx_ledger_count()
```

- **Network Fees**: Returns the total amount of fees paid on the XRP Ledger within each time window. This metric reflects transaction cost dynamics and can be used to assess network congestion or changes in fee policy over time.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_ntx_fees()
```

- **Transaction Count**: Returns the total number of transactions processed on the XRP Ledger within each time window. This metric reflects overall network activity and is commonly used to evaluate throughput, adoption trends, and on-chain demand.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_ntx_trx_count()
```

- **Tokens Transferred**: Returns the total number of XRP tokens transferred on-chain within each time window. This metric quantifies transaction volume in token units and helps evaluate liquidity flow, settlement activity, and overall utilization of the XRP Ledger.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_ntx_tokens_transferred()
```

- **Total Supply**: Returns the total circulating supply of XRP. This metric tracks the total amount of XRP available in the network at each point in time and is essential for analyzing monetary dynamics, market capitalization, and token issuance trends.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_ntx_supply()
```

#### XRP Network Indicator [:arrow_up:](#cryptoquant-sdk)
Retrieve metrics related to XRP Network Indicators.

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

- **Network Value to Transaction (NVT) Ratio**: Calculates the ratio between the network value (defined as `supply_total * price_usd`) and the total tokens transferred. This indicator is commonly used to assess whether XRP’s market price is overvalued or undervalued relative to on-chain transaction activity. A lower NVT suggests higher transactional utility, while a higher NVT may indicate speculative valuation.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_ntx_value_to_trx()
```

#### XRP Dex Data [:arrow_up:](#cryptoquant-sdk)
Retrieve metrics related to XRP Dex.

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

- **DEX Volume**: Returns the total XRP volume traded on the XRPL decentralized exchange (DEX). This metric captures the on-chain trading activity and liquidity level within the native DEX, reflecting organic market participation and decentralized trading demand.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_dex_volume()
```

- **DEX Transaction Count**: Returns the total number of XRP transactions executed on the XRPL decentralized exchange (DEX). This metric measures trading activity and user participation, serving as an indicator of adoption and network utilization within the on-chain exchange.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_dex_trx_count()
```

- **DEX Liquidity**: Returns the total USD-denominated liquidity available within the XRPL decentralized exchange (DEX). This metric reflects the overall depth and stability of the DEX’s order books, indicating how efficiently large trades can be executed without significant price impact.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_dex_liquidity()
```

- **DEX Price**: Returns the price of XRP traded on the XRPL decentralized exchange (DEX). This metric represents the on-chain market valuation of XRP within the DEX and can be compared against centralized exchange prices to identify potential arbitrage opportunities or liquidity disparities.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_dex_price()
```

#### XRP AMM Data [:arrow_up:](#cryptoquant-sdk)
Retrieve metrics related to XRP AMM Data.

Supported AMM Pairs

| Name | AMM Account | AMM | Status |
| :--- | :--- | :--- | :--- |
| MAG/XRP | `rNZ2ZVF1ZU34kFqYcNA4xkFAvdSvve5bXce` | `mag-xrp` | Validated |
| XGO/XRP | `rLeAEyRQ5RnN6Ljn2Z9Xw4pbcWFkQYut3c` | `xgo-xrp` | Validated |
| SOLO/XRP | `rMeJQ9H5XvTe17UoAJzJ8jtKkVVTRcxwngo` | `solo-xrp` | Validated |
| USDC/XRP | `rGht6LT5V9DVaEAmFzJ5ciuxuJ41ZLjLofs` | `usdc-xrp` | Validated |
| BTC/XRP | `rQBEAghWHEwWVkShryBSa5yR3VRX9oyQ5T` | `btc-xrp` | Validated |
| USD/XRP | `rHUPaqUPbwZkZdZQ8ZQCme18FrgW9pB4am` | `usd-xrp` | Validated |
| XPM/XRP | `rak2prdzwsUJ1rd2ouhYYAVP7tPbhrCbtz` | `xpm-xrp` | Validated |
| CSC/XRP | `rf7g4JWCxu9oE1MKSWtiL9whY75AphCaV` | `csc-xrp` | Validated |
| RLT/XRP | `rwzCasMZ2WisfphuMCVWDDd58HK9QtDYc` | `rlt-xrp` | Validated |
| CORE/XRP | `rBu4LXTXM9ofs3JsFCuDbPmzvGBDR66wpi` | `core-xrp` | Validated |


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

- **AMM Price**: Returns the current XRP exchange rate for supported Automated Market Maker (AMM) pairs. This metric reflects the on-chain price formation between XRP and other assets within AMM pools. Currently, only non-XRP/XRP pairs are supported.  

    - **Specific Parameters**  
        - ```amm```(str): Required — AMM pair supported by CryptoQuant.  
          Example values: `usdc-xrp`, `btc-xrp`, `solo-xrp`. See the “Supported AMM Pairs” table for all validated pools.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_amm_price(amm="usdc-xrp")
```

- **AMM Liquidity**: Returns the total USD-denominated liquidity available within supported Automated Market Maker (AMM) pools. This metric indicates the combined value of assets supplied by liquidity providers and reflects the overall market depth and stability of each AMM pair. Currently, only non-XRP/XRP pairs are supported.  

    - **Specific Parameters**  
        - ```amm```(str): Required — AMM pair supported by CryptoQuant.  
          Example values: `usdc-xrp`, `btc-xrp`, `solo-xrp`. See the “Supported AMM Pairs” table for all validated pools.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_amm_liquidity(amm="usdc-xrp")
```

- **AMM Fee**: Returns the trading fee applied within supported Automated Market Maker (AMM) pools. This metric represents the swap fee percentage charged to traders and distributed to liquidity providers, offering insight into cost structure and revenue generation across AMM markets. Currently, only non-XRP/XRP pairs are supported.  

    - **Specific Parameters**  
        - ```amm```(str): Required — AMM pair supported by CryptoQuant.  
          Example values: `usdc-xrp`, `btc-xrp`, `solo-xrp`. See the “Supported AMM Pairs” table for all validated pools.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_amm_fee(amm="usdc-xrp")
```

- **AMM Swaps**: Returns swap statistics for supported Automated Market Maker (AMM) pools. This metric includes aggregated data on swap volume, number of swaps, and liquidity movement within each AMM. It provides insights into on-chain trading activity and utilization of decentralized liquidity. Currently, only non-XRP/XRP pairs are supported.  

    - **Specific Parameters**  
        - ```amm```(str): Required — AMM pair supported by CryptoQuant.  
          Example values: `usdc-xrp`, `btc-xrp`, `solo-xrp`. See the “Supported AMM Pairs” table for all validated pools.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_xrp_amm_swaps(amm="usdc-xrp")
```

### TRX [:arrow_up:](#cryptoquant-sdk)

| Section Name | Objective | Number of Endpoints |
| :------------ | :--------- | :----------------: |
| **Market Data** | Provides TRX market performance metrics such as price OHLCV and market capitalization. Useful for analyzing market trends, valuation, and trading behavior. | 2 |
| **Network Data** | Covers on-chain metrics related to TRON’s network activity, including supply, transactions, addresses, fees, staking, and throughput. Helps assess network health, scalability, and monetary policy. | 9 |
| **DeFi Data** | Tracks decentralized finance activity within the TRON ecosystem, focusing on SunPump token creation and SunSwap trading activity to measure ecosystem growth and liquidity dynamics. | 2 |


#### TRX Market data [:arrow_up:](#cryptoquant-sdk)
Retrieve metrics related to TRX Market Data.

| Metric | Description |
| :--- | :--- |
| `open` | The opening price at the beginning of the window. |
| `close` | The USD closing price at the end of the window. |
| `high` | The highest USD price in a given window. |
| `low` | The lowest USD price in a given window. |
| `volume` | The total volume traded in a given window. |

Supported Exchanges by market

| Name | Market | Supported Exchanges |
| :--- | :--- | :--- |
| Spot | `spot` | All Exchange* |

\* Default Exchange

Supported Pairs By Exchange

| Name | Exchange | Symbol |
| :--- | :--- | :--- |
| All Exchanges | `all_exchange` | `trx_usd` * |

Supported Windows By Market

| Market | Supported Windows |
| :--- | :--- |
| Spot | `day`* |

- **Price OHLCV**: Returns TRX price metrics including open, high, low, close, and volume (OHLCV). This dataset provides the USD-denominated opening price at the start of each window, the closing price at the end, the highest and lowest prices within the interval, and the total traded token volume.  

    - **Specific Parameters**  
        - ```market```(str): Optional — Market type supported by CryptoQuant.  
        - ```exchange```(str): Optional — Exchange supported by CryptoQuant (e.g., `binance`, `bitget`, `okx`).  
        - ```symbol```(str): Optional — TRX trading pair symbol supported by CryptoQuant.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_trx_mkt_ohlcv()
```

- **Market Capitalization**: Returns metrics related to the total market capitalization of TRX. The `market_cap` value represents the overall valuation of TRX, calculated by multiplying the total circulating supply by its USD price. This metric reflects the aggregate market value of TRX and is a key indicator of its relative scale and dominance within the crypto market.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_trx_mkt_capitalization()
```

#### TRX Network Data [:arrow_up:](#cryptoquant-sdk)
Retrieve metrics related to TRX Network Data.

| Metric | Description |
| :--- | :--- |
| `supply_total` | The total amount of tokens in existence. |
| `supply_circulating` | The amount of tokens that are circulating in the market. |
| `supply_minted` | The amount of tokens minted in the given window. |
| `supply_burned` | The amount of tokens burned in the given window. |
| `supply_staked` | The amount of tokens staked in Tron Super Representative members. |

- **Supply**: Returns metrics related to the supply of TRX. This dataset includes details on total, circulating, minted, burned, and staked supply, providing a comprehensive view of TRX’s monetary dynamics and issuance activity.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_trx_ntx_supply()
```

- **Transaction Count**: Returns metrics related to the total and average number of transactions on the TRON network. This metric provides insight into overall network activity, throughput, and user engagement over time.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_trx_ntx_trx_count()
```

| Metric | Description |
| :--- | :--- |
| `transactions_count_total` | The total number of transactions. |
| `transactions_count_mean` | The mean number of transactions. |

- **Active Addresses Count**: Returns metrics related to the number of unique TRX addresses used on the network. This metric measures on-chain participation and network activity, serving as an indicator of user growth and utilization of the TRON ecosystem.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_trx_ntx_addrs_count()
```

| Metric | Description |
| :--- | :--- |
| `addresses_count_active` | The total number of unique addresses that were active (either sender or receiver) on the blockchain in a given window. |
| `addresses_count_sender` | The number of addresses that were active as a sender. |
| `addresses_count_receiver` | The number of addresses that were active as a receiver. |


- **Tokens Transferred**: Returns metrics related to the total number of TRX tokens transferred on-chain within each time window. This metric reflects the overall transaction volume in token units and helps assess liquidity flow, network usage, and transactional intensity in the TRON ecosystem.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_trx_ntx_tokens_transferred()
```

| Metric | Description |
| :--- | :--- |
| `tokens_transferred_total` | The total number of transferred tokens in that window. |
| `tokens_transferred_mean` | The mean of transferred tokens per transaction in that window. |
| `tokens_transferred_median` | The median of tokens transferred per transaction in that window. |


- **Block Count**: Returns the total number of blocks generated on the TRON network within each time window. This metric reflects the block production rate and provides insight into network stability, validator performance, and overall chain activity.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_trx_ntx_block_count()
```

- **Network Fees**: Returns statistics related to the total fees paid from executing transactions on the TRON network. This dataset includes both aggregate and average fee metrics, expressed in TRX and USD, offering insight into network demand and transaction cost dynamics.  

    **Metrics**  
    - `fees_total`: Total amount of TRX paid as transaction fees.  
    - `fees_total_usd`: Total transaction fees converted to USD.  
    - `fees_block_mean`: Average transaction fee per block.  
    - `fees_block_mean_usd`: Average transaction fee per block in USD.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_trx_ntx_fees()
```

- **Transactions Per Second (TPS)**: Returns statistics related to the number of transactions processed per second on the TRON network. This metric reflects network throughput and efficiency, serving as an indicator of scalability and system performance.  

    **Metrics**  
    - `tps`: The number of transactions per second.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_trx_ntx_tps()
```

- **Total Value Staked**: Returns the total amount of TRX locked under the TRON staking models Stake 1.0 and Stake 2.0. This metric measures the amount of TRX committed to securing the network and obtaining resources or staking rewards, reflecting validator participation and network security.  

    **Metrics**  
    - `v1_staking_amount`: The amount of TRX staked under Stake 1.0 (legacy staking model).  
    - `v2_staking_amount`: The amount of TRX staked under Stake 2.0 (current staking model).  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_trx_ntx_total_value_staked()
```

- **Energy Stake**: Returns statistics related to the amount of TRX staked for Energy. This metric provides insights into how much TRX is locked to obtain computational resources within the TRON network, reflecting user demand for Energy and staking participation.  

    **Metrics**  
    - `total_energy_weight`: The total amount of TRX staked for Energy.  
    - `energy_rate`: The percentage of TRX staked for Energy relative to total supply.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_trx_ntx_enery_stake()
```

#### TRX DEFI [:arrow_up:](#cryptoquant-sdk)
Returns metrics related to SunPump token creation on TRON.

- **SunPump Token Creation**: Returns metrics related to token creation events on the SunPump platform within the TRON network. This dataset provides insights into the growth and activity of newly created tokens in the DeFi ecosystem.  

    **Metrics**  
    - `token_create_event_count`: The total number of tokens created on the SunPump platform.  
    - `cumulative_count_create_events`: The cumulative number of token creation events on SunPump over time.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_trx_defi_sunpump_tokens()
```

- **SunSwap Activity**: Returns metrics related to trading activity on the SunSwap decentralized exchange within the TRON network. This dataset captures transaction volume, dominance, and token-specific activity, providing a view of liquidity and user engagement across the platform.  

    **Metrics**  
    - `total_transaction_count`: The total number of transactions on SunSwap.  
    - `wtrx_transaction_count`: The number of transactions involving WTRX within the given window.  
    - `other_transaction_count`: The number of transactions involving tokens other than WTRX.  
    - `wtrx_dominance`: The dominance of WTRX in total transaction volume within the given window.  
    - `wtrx_amount`: The total amount of WTRX traded within the window.  
    - `wtrx_amount_usd`: The total amount of WTRX traded in USD within the window.  

    - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_trx_defi_sunswap_activity()
```

### StableCoins [:arrow_up:](#cryptoquant-sdk)

| Section Name | Objective | Number of Endpoints |
| :------------ | :--------- | :----------------: |
| **Entity List** | Provides a list of entities (exchanges, custodians, and issuers) associated with each stablecoin. Serves as a reference point for entity-based metrics and market structure analysis. | 1 |
| **Exchange Flows** | Tracks the flow of stablecoins between exchange wallets and external addresses, including reserves, inflows, outflows, transaction count, and address activity. Useful for identifying liquidity shifts and exchange-level demand. | 6 |
| **Flow Indicator** | Measures liquidity concentration and market positioning by comparing exchange reserves to total circulating supply (Exchange Supply Ratio). | 1 |
| **Market Data** | Provides aggregated market performance metrics such as OHLCV price data and market capitalization, based on VWAP of global exchange data. | 2 |
| **Network Data** | Captures on-chain metrics including supply, mint/burn/issue/redeem events, tokens transferred, and active addresses, allowing for comprehensive monitoring of issuance and network activity. | 4 |


#### StableCoin Entity List [:arrow_up:](#cryptoquant-sdk)
Stablecoin API with Status.

- **Entity List**: Returns the list of entities available for a specific stablecoin. This includes exchanges, custodians, and other related entities.  
  *Note:* The parameter `all_token` is **not supported** for this endpoint — a specific stablecoin symbol (e.g., `usdt`, `usdc`, `dai`) must be provided.  
  For exchange entities, the `market_type` field indicates whether the exchange operates in the spot or derivatives market. Entities without a market type (e.g., banks, custodians) will return `0`.  

    **Exchange Market Type**  
    | Value | Description |  
    | :----: | :----------- |  
    | `0` | Undefined |  
    | `1` | Spot Exchange |  
    | `2` | Derivative Exchange |  

    - **Specific Parameters**  
        - ```token```(str): Required — Stablecoin symbol supported by CryptoQuant (e.g., `usdt`, `usdc`, `dai`, `tusd`).  
        - ```format_```(str): Optional — Default: `json`. Defines the response format. Supported formats: `json`, `csv`.  
        - Authorization via access token is required.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_stable_entity_list(token="usdt")
```

#### StableCoin Exchange Flows [:arrow_up:](#cryptoquant-sdk)

Returns the historical amount of stablecoin tokens held in exchange wallets for as far back as available. This metric reflects the balance of reserves across supported exchanges, helping to assess liquidity concentration and potential market pressure.  
  *Note:* Transfers to exchange wallets may occur some time after the contract creation event. Exchange wallet data is periodically updated every **Tuesday at 00:00 UTC**, which may lead to minor adjustments in recent data points.  

**Supported Aggregated Exchanges**

| Name | Exchange | Supported Stablecoins |  
| :---- | :-------- | :------------------- |  
| All Exchanges | `all_exchange` | All Tokens |  
| Spot Exchanges | `spot_exchange` | All Tokens |  
| Derivative Exchanges | `derivative_exchange` | All Tokens |  

*This endpoint does not support Point-In-Time (PIT) accuracy* due to periodic updates in exchange wallet clustering. Historical data may change as new wallets are discovered, validated, and added.  


- **Exchange Reserve**: Returns the full historical on-chain balance of Stablecoin exchanges. 

    - **Specific Parameters**  
        - ```token```(str): Required — Stablecoin symbol supported by CryptoQuant (e.g., `usdt`, `usdc`, `dai`, `tusd`).  
        - ```exchange```(str): Optional — Specific or aggregated exchange identifier (see table above).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_stable_exch_reserve(token="usdt_eth", exchange="binance")
```

- **Exchange Netflow**: Represents the difference between stablecoin inflows and outflows from exchanges. This metric helps identify whether more coins are being deposited (positive netflow) or withdrawn (negative netflow) over a given time frame. A positive netflow often signals an increase in idle coins potentially waiting to be traded, while a negative netflow can indicate accumulation or withdrawal to custody.  

    - **Specific Parameters**  
        - ```token```(str): Required — Stablecoin symbol supported by CryptoQuant (e.g., `usdt`, `usdc`, `dai`, `tusd`).  
        - ```exchange```(str): Optional — Exchange or aggregated exchange identifier (e.g., `all_exchange`, `spot_exchange`, `derivative_exchange`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_stable_exch_netflow(token="usdt_eth", exchange="binance")
```

- **Exchange Inflow**: Returns the total inflow of stablecoins into exchange wallets for as far back as available. This metric measures the amount of tokens deposited into exchange wallets, indicating potential selling pressure or increased liquidity supply. The average inflow represents the average transaction value for deposits on a given day.  

    - **Specific Parameters**  
        - ```token```(str): Required — Stablecoin symbol supported by CryptoQuant (e.g., `usdt_eth`, `usdc_eth`, `dai_eth`).  
        - ```exchange```(str): Required — Exchange supported by CryptoQuant (e.g., `binance`, `kraken`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_stable_exch_inflow(token="usdt_eth", exchange="binance")
```

- **Exchange Outflow**: Returns the total outflow of stablecoins from exchange wallets for as far back as available. This metric measures the amount of tokens withdrawn from exchange wallets, indicating accumulation, self-custody movements, or reduced liquidity on trading platforms. The average outflow represents the average transaction value for withdrawals on a given day.  

    - **Specific Parameters**  
        - ```token```(str): Required — Stablecoin symbol supported by CryptoQuant (e.g., `usdt_eth`, `usdc_eth`, `dai_eth`).  
        - ```exchange```(str): Required — Exchange supported by CryptoQuant (e.g., `binance`, `kraken`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_stable_exch_outflow(token="usdt_eth", exchange="binance")
```

- **Exchange Transaction Count**: Returns the total number of transactions flowing into and out of stablecoin exchange wallets. This metric measures on-chain transactional activity between exchanges and users, helping identify shifts in market participation, liquidity movements, and trading intensity.  

    - **Specific Parameters**  
        - ```token```(str): Required — Stablecoin symbol supported by CryptoQuant (e.g., `usdt_eth`, `usdc_eth`, `dai_eth`).  
        - ```exchange```(str): Required — Exchange supported by CryptoQuant (e.g., `binance`, `kraken`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_stable_exch_trx_count(token="usdt_eth", exchange="binance")
```

- **Exchange Addresses Count**: Returns the number of unique addresses involved in inflow and outflow transactions for a given stablecoin on exchanges. This metric reflects the diversity of participants interacting with exchange wallets, helping identify changes in market activity, user engagement, or concentration of flows.  

    - **Specific Parameters**  
        - ```token```(str): Required — Stablecoin symbol supported by CryptoQuant (e.g., `usdt_eth`, `usdc_eth`, `dai_eth`).  
        - ```exchange```(str): Required — Exchange supported by CryptoQuant (e.g., `binance`, `kraken`, `okx`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_stable_exch_addrs_count(token="usdt_eth", exchange="binance")
```

#### Stablecoin Flow Indicator [:arrow_up:](#cryptoquant-sdk)
Retrieve entity flow based indicators. CQ provide certain indicators to avoid any risks, assume upside or downside potentials, and give insights on the value of bitcoin. For more detailed information, please refer to the description of each metric.

- **Exchange Supply Ratio**: Calculates the ratio between the stablecoin reserve on exchanges and the total circulating supply. This metric measures how much of the token supply is held within exchanges, providing insight into liquidity concentration and potential sell-side pressure in the market.  

    - **Specific Parameters**  
        - ```token```(str): Required — Stablecoin symbol supported by CryptoQuant (e.g., `usdt_eth`, `usdc_eth`, `dai_eth`).  
        - ```exchange```(str): Optional — Exchange or aggregated exchange identifier (e.g., `all_exchange`, `spot_exchange`, `derivative_exchange`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_stable_flow_exch_supply_ratio(token="usdt_eth")
```

#### Stablecoin Market Data [:arrow_up:](#cryptoquant-sdk)
Retrieve metrics related to the value of tokens, including price, market cap, etc.

- **Price OHLCV (Index Price)**: Returns stablecoin price metrics including open, high, low, close, and volume (OHLCV). Metrics are calculated by minute, hour, and day intervals. The Stablecoin Index Price is derived using the Volume Weighted Average Price (VWAP) of aggregated global exchange data, providing a comprehensive and reliable reference for market valuation.  

    - **Specific Parameters**  
        - ```token```(str): Required — Stablecoin symbol supported by CryptoQuant (e.g., `usdt_eth`, `usdc_eth`, `dai_eth`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_stable_mkt_ohlcv(token="usdt_eth")
```

- **Market Capitalization**: Returns metrics related to the total market capitalization of a stablecoin. The `market_cap` value represents the circulating supply multiplied by the USD closing price (`circulating_supply * price_usd_close`). This metric reflects the total market valuation of the stablecoin and is useful for tracking issuance growth and market dominance over time.  

    - **Specific Parameters**  
        - ```token```(str): Required — Stablecoin symbol supported by CryptoQuant (e.g., `usdt_eth`, `usdc_eth`, `dai_eth`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_stable_mkt_capitalization(token="usdt_eth")
```

#### Stablecoin Network Data [:arrow_up:](#cryptoquant-sdk)
See full explanation in the [following site](https://cryptoquant.com/docs#tag/Stablecoin-Network-Data)

- **Token Supply**: Returns metrics related to the total supply of stablecoins — the amount of tokens currently in existence. This dataset includes six key metrics describing both total and circulating supply, as well as minting, burning, issuing, and redemption activity.  

    **Metrics**  
    - `supply_total`: The total amount of tokens in existence.  
    - `supply_circulating`: An approximation of the amount of tokens circulating in the market (excluding treasury or issuer-controlled addresses).  
    - `supply_minted`: The number of tokens newly created and added to total supply.  
    - `supply_burned`: The number of tokens permanently removed from total supply.  
    - `supply_issued`: The number of tokens issued and added to circulating supply.  
    - `supply_redeemed`: The number of tokens redeemed and removed from circulating supply.  
    *Note:* For some stablecoins, mint and issue (or redeem and burn) may occur simultaneously, while for others they occur separately.  

    - **Specific Parameters**  
        - ```token```(str): Required — Stablecoin symbol supported by CryptoQuant (e.g., `usdt_eth`, `usdc_eth`, `dai_eth`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_stable_ntx_supply(token="usdt_eth")
```

- **Events Count**: Returns metrics related to the number of on-chain events associated with stablecoin supply changes. This dataset tracks how frequently minting, issuing, burning, and redeeming actions occur, providing insight into the operational activity of the stablecoin’s supply management.  

    **Metrics**  
    - `events_mint_count`: The number of mint events (tokens newly created).  
    - `events_issue_count`: The number of issue events (tokens added to circulating supply).  
    - `events_burn_count`: The number of burn events (tokens permanently removed from total supply).  
    - `events_redeem_count`: The number of redeem events (tokens withdrawn from circulation).  

    - **Specific Parameters**  
        - ```token```(str): Required — Stablecoin symbol supported by CryptoQuant (e.g., `usdt_eth`, `usdc_eth`, `dai_eth`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_stable_ntx_events_count(token="usdt_eth")
```

- **Tokens Transferred**: Returns metrics related to the total number of stablecoin tokens transferred on-chain, representing transaction volume. This dataset captures both the aggregate and average amounts of tokens moved, providing insight into liquidity activity and transaction scale.  

    **Metrics**  
    - `tokens_transferred_total`: The total number of tokens transferred during the specified window.  
    - `tokens_transferred_mean`: The mean number of tokens transferred per transaction.  

    - **Specific Parameters**  
        - ```token```(str): Required — Stablecoin symbol supported by CryptoQuant (e.g., `usdt_eth`, `usdc_eth`, `dai_eth`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_stable_trx_tokens_transferred(token="usdt_eth")
```

- **Active Addresses Count**: Returns metrics related to the number of unique addresses involved in stablecoin transfers. This dataset captures the total number of active participants as well as the breakdown between senders and receivers, providing insight into network activity, user engagement, and transactional distribution.  

    **Metrics**  
    - `addresses_active_count`: The total number of unique addresses that were active (either as sender or receiver) within the given time window.  
    - `addresses_active_sender_count`: The number of unique addresses that were active as senders.  
    - `addresses_active_receiver_count`: The number of unique addresses that were active as receivers.  

    - **Specific Parameters**  
        - ```token```(str): Required — Stablecoin symbol supported by CryptoQuant (e.g., `usdt_eth`, `usdc_eth`, `dai_eth`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_stable_trx_addrs_count(token="usdt_eth")
```

### ERC20 [:arrow_up:](#cryptoquant-sdk)

#### ERC20 Entity Status [:arrow_up:](#cryptoquant-sdk)
ERC20 API with Status

- **Entity List**: Returns the list of entities available for a specific ERC-20 token. This includes exchanges, custodians, and other related entities. For exchange entities, the `market_type` field indicates whether the exchange operates in the **spot** or **derivatives** market. Entities without a defined market type (e.g., custodians or smart contracts) will return `0`.  

    **Exchange Market Type**  
    | Value | Description |  
    | :----: | :----------- |  
    | `0` | Undefined |  
    | `1` | Spot Exchange |  
    | `2` | Derivative Exchange |  

    - **Specific Parameters**  
        - ```token```(str): Required — ERC-20 token symbol supported by CryptoQuant (e.g., `link_eth`, `uni_eth`, `aave_eth`, `shib_eth`).  
        - ```format_```(str): Optional — Default: `json`. Defines the response format. Supported formats: `json`, `csv`.  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_erc20_entity_list(token="link_eth")
```

#### ERC20 Exchange Flows [:arrow_up:](#cryptoquant-sdk)

- **Exchange Reserve**: Returns the full historical on-chain ERC-20 token balance of exchanges. This metric reflects the amount of tokens held within exchange wallets, providing insight into liquidity availability, accumulation trends, and potential sell-side pressure.  
  The full list of supported ERC-20 tokens can be found in the [CryptoQuant Supported ERC-20 List](https://cryptoquant.com/docs#tag/Supported-ERC20-List).  

    - **Specific Parameters**  
        - ```token```(str): Required — ERC-20 token symbol supported by CryptoQuant (e.g., `sushi`, `uni`, `aave`, `mkr`, `omg`, `uma`).  
        - ```exchange```(str): Required — Exchange or aggregated exchange identifier (e.g., `spot_exchange`, `all_exchange`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_erc20_exch_reserve(token="uni", exchange="spot_exchange")
```

- **Exchange Netflow**: Represents the difference between ERC-20 tokens flowing into and out of exchanges. A positive netflow indicates an increase in idle coins on exchanges (potential selling pressure), while a negative netflow suggests withdrawals to self-custody or accumulation. This metric helps identify liquidity movements and investor sentiment over time.  
  The full list of supported ERC-20 tokens can be found in the [CryptoQuant Supported ERC-20 List](https://cryptoquant.com/docs#tag/Supported-ERC20-List).  

    - **Specific Parameters**  
        - ```token```(str): Required — ERC-20 token symbol supported by CryptoQuant (e.g., `sushi`, `uni`, `aave`, `mkr`, `omg`, `uma`).  
        - ```exchange```(str): Required — Exchange or aggregated exchange identifier (e.g., `spot_exchange`, `all_exchange`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_erc20_exch_netflow(token="aave", exchange="all_exchange")
```

- **Exchange Inflow**: Returns the total inflow of ERC-20 tokens into exchange wallets for as far back as available. This metric measures the amount of tokens deposited into exchange wallets, indicating potential increases in liquidity supply or short-term selling pressure. The average inflow represents the mean transaction value for deposits within a given window.  
  The full list of supported ERC-20 tokens can be found in the [CryptoQuant Supported ERC-20 List](https://cryptoquant.com/docs#tag/Supported-ERC20-List).  

    - **Specific Parameters**  
        - ```token```(str): Required — ERC-20 token symbol supported by CryptoQuant (e.g., `sushi`, `uni`, `aave`, `mkr`, `omg`, `uma`).  
        - ```exchange```(str): Required — Exchange or aggregated exchange identifier (e.g., `spot_exchange`, `all_exchange`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_erc20_exch_inflow(token="sushi", exchange="spot_exchange")
```

- **Exchange Outflow**: Returns the total outflow of ERC-20 tokens from exchange wallets for as far back as available. This metric measures the amount of tokens withdrawn from exchanges, often interpreted as accumulation, reduced liquidity, or movement toward self-custody. The average outflow represents the mean transaction value for withdrawals within a given window.  
  The full list of supported ERC-20 tokens can be found in the [CryptoQuant Supported ERC-20 List](https://cryptoquant.com/docs#tag/Supported-ERC20-List).  

    - **Specific Parameters**  
        - ```token```(str): Required — ERC-20 token symbol supported by CryptoQuant (e.g., `sushi`, `uni`, `aave`, `mkr`, `omg`, `uma`).  
        - ```exchange```(str): Required — Exchange or aggregated exchange identifier (e.g., `spot_exchange`, `all_exchange`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_erc20_exch_outflow(token="mkr", exchange="all_exchange")
```

- **Exchange Transaction Count**: Returns the total number of transactions involving ERC-20 tokens flowing into and out of exchange wallets. This metric reflects transactional activity and user participation on exchanges, helping to identify changes in liquidity dynamics and market engagement.  
  The full list of supported ERC-20 tokens can be found in the [CryptoQuant Supported ERC-20 List](https://cryptoquant.com/docs#tag/Supported-ERC20-List).  

    - **Specific Parameters**  
        - ```token```(str): Required — ERC-20 token symbol supported by CryptoQuant (e.g., `sushi`, `uni`, `aave`, `mkr`, `omg`, `uma`).  
        - ```exchange```(str): Required — Exchange or aggregated exchange identifier (e.g., `spot_exchange`, `all_exchange`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_erc20_exch_trx_count(token="omg", exchange="spot_exchange")
```

- **Exchange Addresses Count**: Returns the number of unique addresses involved in ERC-20 token inflow and outflow transactions. This metric measures the diversity and distribution of on-chain participants interacting with exchange wallets, helping identify whether market activity is concentrated or broadly distributed among users.  
  The full list of supported ERC-20 tokens can be found in the [CryptoQuant Supported ERC-20 List](https://cryptoquant.com/docs#tag/Supported-ERC20-List).  

    - **Specific Parameters**  
        - ```token```(str): Required — ERC-20 token symbol supported by CryptoQuant (e.g., `sushi`, `uni`, `aave`, `mkr`, `omg`, `uma`).  
        - ```exchange```(str): Required — Exchange or aggregated exchange identifier (e.g., `spot_exchange`, `all_exchange`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_erc20_exch_addrs_count(token="uma", exchange="all_exchange")
```

#### ERC20 Flow Indicator [:arrow_up:](#cryptoquant-sdk)
Retrieve entity flow based indicators. CQ provide certain indicators to avoid any risks, assume upside or downside potentials, and give insights on the value of bitcoin. For more detailed information, please refer to the description of each metric.

- **Exchange Supply Ratio**: Calculates the ratio between the ERC-20 token reserve on exchanges and its total circulating supply. This metric measures how much of the token supply is held within exchanges, offering insight into liquidity concentration, potential sell-side pressure, and market exposure of a given token.  
  The full list of supported ERC-20 tokens can be found in the [CryptoQuant Supported ERC-20 List](https://cryptoquant.com/docs#tag/Supported-ERC20-List).  

    - **Specific Parameters**  
        - ```token```(str): Required — ERC-20 token symbol supported by CryptoQuant (e.g., `sushi`, `uni`, `aave`, `mkr`, `omg`, `uma`).  
        - ```exchange```(str): Optional — Exchange or aggregated exchange identifier (e.g., `spot_exchange`, `all_exchange`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_erc20_exch_supply_ratio(token="sushi", exchange="spot_exchange")
```

#### ERC20 Market Data [:arrow_up:](#cryptoquant-sdk)

- **Price OHLCV (Index Price)**: Returns ERC-20 token price metrics including open, high, low, close, and volume (OHLCV). Metrics are calculated by minute, hour, and day intervals. The ERC-20 Token Index Price is derived from the Volume Weighted Average Price (VWAP) of aggregated price data across global exchanges, providing a reliable and standardized reference for market valuation.  
  The full list of supported ERC-20 tokens can be found in the [CryptoQuant Supported ERC-20 List](https://cryptoquant.com/docs#tag/Supported-ERC20-List).  
  The list of supported ERC-20 exchanges is available in the [CryptoQuant ERC-20 Exchange List](https://www.notion.so/cqlive/Stablecoins-ERC20-Exchange-List-e33b9baeae094fb090983dc1e1183b05).  

    - **Specific Parameters**  
        - ```token```(str): Required — ERC-20 token symbol supported by CryptoQuant (e.g., `sushi`, `uni`, `aave`, `mkr`, `omg`, `uma`).  
        - Common parameters apply: `window`, `from_`, `to_`, `limit`, `format_`.  

    - **Usage**  
```python
resp = client.get_erc20_mkt_ohlcv(token="aave")
```



---

## Disclaimer [:arrow_up:](#cryptoquant-sdk)

The information in this document is provided for informational and educational purposes only. Nothing herein should be construed as financial, legal, or tax advice. The author is not a licensed financial advisor or registered investment consultant.

This SDK is not affiliated with or endorsed by CryptoQuant. It is an independent, open-source tool intended for research and data analysis.

This document does not constitute an offer to buy or sell any financial instrument. Always perform your own due diligence and consult a qualified professional before making investment decisions.