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
	- [Available Endpoints](#available-endpoints-arrow_up)
	- [Bitcoin](#bitcoin-arrow_up)
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
---

## Disclaimer [:arrow_up:](#cryptoquant-sdk)

The information in this document is provided for informational and educational purposes only. Nothing herein should be construed as financial, legal, or tax advice. The author is not a licensed financial advisor or registered investment consultant.

This SDK is not affiliated with or endorsed by CryptoQuant. It is an independent, open-source tool intended for research and data analysis.

This document does not constitute an offer to buy or sell any financial instrument. Always perform your own due diligence and consult a qualified professional before making investment decisions.