from fastapi import FastAPI, HTTPException
import requests
import httpx
from datetime import date, timedelta
from news.getnews import get_finnhub_news as fetch_finnhub_news, get_marketaux_news as fetch_marketaux_news, combine_news_sources
from news.newsengine import save_news_to_db, dynamic_news


app = FastAPI()

@app.get("/news/finnhub")
async def get_finnhub_news():
   await save_news_to_db()

   return {"message": "News saved to database successfully."}



@app.get("/news/marketaux")
async def get_marketaux_news():
    news = await fetch_marketaux_news()

    return news


