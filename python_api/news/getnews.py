# Retrieve news articles from different sources and merge

from fastapi import FastAPI, HTTPException
import httpx
from news.newsclass import NewsItem
from datetime import datetime, date, timedelta
from typing import List
import asyncio

FINNHUB_API_KEY = "d1kht4hr01qt8foomrh0d1kht4hr01qt8foomrhg"
MARKETAUX_API_KEY = "6WtkONH8y6LUJwdwEeUrsp062EKn3j4G0WUJz66H"

async def get_finnhub_news():
    url = f"https://finnhub.io/api/v1/company-news"
    params = {
        "symbol": "PLTR",
        "from": date.today() - timedelta(days=1),
        "to": date.today().isoformat(),
        "token": FINNHUB_API_KEY
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()

    articles = response.json()

    news_items = [convert_finnhub_to_newsitem(article) for article in articles]
    
    return news_items

async def get_marketaux_news():
    url = f"https://api.marketaux.com/v1/news/all"
    params = {
        "published_after": date.today() - timedelta(days=1),
        "api_token": MARKETAUX_API_KEY,
        "language": "en",
        "symbols": "PLTR"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()

    data = response.json()
    articles = data.get("data", [])

    if not isinstance(articles, list):
        return []

    news_items = [convert_marketaux_to_newsitem(article) for article in articles]

    return news_items

def convert_finnhub_to_newsitem(article: dict) -> dict:
    return {
        "source":"Finnhub",
        "title":article["headline"],
        "url":article["url"],
        "published_at":datetime.fromtimestamp(article["datetime"]),
        "summary":article.get("summary"),
    }

def convert_marketaux_to_newsitem(article) -> dict:
    return {
        "source": "MarketAux",
        "title": article["title"],
        "url": article["url"],
        "published_at": article["published_at"],
        "summary": article.get("snippet"),
    }

async def combine_news_sources():
    fetch_finnhub_news, fetch_marketaux_news = await asyncio.gather(
        get_finnhub_news(),
        get_marketaux_news()
    )

    all_articles = fetch_finnhub_news + fetch_marketaux_news
    sorted_articles = sorted(all_articles, key=lambda x: x['published_at'], reverse=True)

    return sorted_articles