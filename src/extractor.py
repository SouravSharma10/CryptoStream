import requests

def fetch_bitcoin_data():
    """
    Extracts current Bitcoin price data from the CoinGecko API.
    Returns the JSON data if the request is successful.
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
        "include_last_updated_at": "true"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")
