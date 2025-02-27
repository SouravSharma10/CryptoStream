import datetime

def transform_bitcoin_data(raw_data):
    """
    Transforms raw Bitcoin data from CoinGecko into a structured dictionary.
    """
    bitcoin_data = raw_data.get("bitcoin")
    if not bitcoin_data:
        raise Exception("Bitcoin data not found in API response")
    
    timestamp = bitcoin_data.get("last_updated_at")
    transformed_data = {
        "time_updated": datetime.datetime.fromtimestamp(timestamp) if timestamp else None,
        "usd_rate": bitcoin_data.get("usd"),
        "code": "USD"
    }
    return transformed_data
