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
	- [Available Endpoints](available-edpoints-arrow_up)
	- [Bitcoin](bitcoin-arrow_up)
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
		- ```format_```(str): Optional - Default: ```json```.A format type about return message type. Supported formats are ```json```, ```csv```.

	- Usage:
```python
resp = client.get_endpoints()
```

### Bitcoin [:arrow_up:](#cryptoquant-sdk)
---

## Disclaimer [:arrow_up:](#cryptoquant-sdk)
The information in this document is provided for informational and educational purposes only. Nothing herein should be construed as financial, legal, or tax advice. The author is not a licensed financial advisor or registered investment consultant.

This SDK is not affiliated with or endorsed by CryptoQuant. It is an independent, open-source tool intended for research and data analysis.

This document does not constitute an offer to buy or sell any financial instrument. Always perform your own due diligence and consult a qualified professional before making investment decisions.