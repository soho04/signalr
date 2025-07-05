# Retrieve news articles from different sources and merge

from fastapi import FastAPI, HTTPException
import httpx
from .newsc import NewsItem
from datetime import datetime, date

FINNHUB_API_KEY = "d1kht4hr01qt8foomrh0d1kht4hr01qt8foomrhg"
MARKETAUX_API_KEY = "6WtkONH8y6LUJwdwEeUrsp062EKn3j4G0WUJz66H"
NEWSDATA_API_KEY = "pub_3e93e78f17ef4cf6833aa515e8f274bb"

async def get_finnhub_news():
    url = f"https://finnhub.io/api/v1/company-news"
    params = {
        "symbol": "PLTR",
        "from": date.today().isoformat(),
        "to": date.today().isoformat(),
        "token": FINNHUB_API_KEY
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()

    articles = response.json()
    print(articles)

    news_items = [convert_finnhub_to_newsitem(article) for article in articles]
    print(news_items)
    
    return news_items

async def get_marketaux_news():
    url = f"https://api.marketaux.com/v1/news/all"
    published_after = date.today().isoformat()
    params = {
        "published_after": published_after,
        "api_token": MARKETAUX_API_KEY,
        "language": "en",
        "symbols": "PLTR"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()

    return [convert_marketaux_to_newsitem(article) for article in response.json()]

async def get_newsdata_news():
    url = f"https://newsdata.io/api/1/news"
    params = {
        "apikey": NEWSDATA_API_KEY,
        "q": "PLTR",
        "language": "en",
        "published_at": date.today().isoformat(),
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
    return [convert_newsdata_to_newsitem(article) for article in response.json()]

def convert_finnhub_to_newsitem(article: dict) -> NewsItem:
    return NewsItem(
        source="Finnhub",
        title=article["headline"],
        url=article["url"],
        published_at=datetime.fromtimestamp(article["datetime"]),
        ticker=article.get("ticker"),
        summary=article.get("summary"),
        category=article.get("category")
    )

def convert_marketaux_to_newsitem(article: dict) -> NewsItem:
    return NewsItem(
        source="MarketAux",
        title=article["title"],
        url=article["url"],
        published_at=datetime.fromisoformat(article["published_at"]),
        ticker=article.get("ticker"),
        summary=article.get("summary"),
        category=article.get("category")
    )

def convert_newsdata_to_newsitem(article: dict) -> NewsItem:
    return NewsItem(
        source="NewsData",
        title=article["title"],
        url=article["url"],
        published_at=datetime.fromisoformat(article["published_at"]),
        ticker=article.get("ticker"),
        summary=article.get("summary"),
        category=article.get("category")
    )