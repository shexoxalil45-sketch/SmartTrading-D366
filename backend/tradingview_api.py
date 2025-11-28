import requests

def get_tradingview_data(symbol="BTCUSDT", interval="1h"):
    url = f"https://api.tradingview.com/crypto/{symbol}/{interval}"
    response = requests.get(url)
    return response.json()
