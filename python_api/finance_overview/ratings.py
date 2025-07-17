import httpx
from datetime import datetime, date, timedelta
import requests

FINNHUB_API_KEY = "d1kht4hr01qt8foomrh0d1kht4hr01qt8foomrhg"

def get_ratings(symbol: str):
    url = f"https://finnhub.io/api/v1/stock/recommendation"

    params = {
        "symbol": symbol,
        "token": FINNHUB_API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"API error: {response.status_code}")
    
    data = response.json()

    ratings = data[0]
    
    return {
        "symbol": symbol,
        "period": ratings.get("period"),
        "strong_buy": ratings.get("strongBuy"),
        "buy": ratings.get("buy"),
        "hold": ratings.get("hold"),
        "sell": ratings.get("sell"),
        "strong_sell": ratings.get("strongSell")
    }