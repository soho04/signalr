from fastapi import FastAPI, HTTPException
import requests
import httpx
from datetime import date, timedelta
from news.news import get_finnhub_news as fetch_finnhub_news

app = FastAPI()

@app.get("/news/finnhub")
async def get_finnhub_news():
    news = await fetch_finnhub_news()

    return news 

