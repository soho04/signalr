from fastapi import FastAPI, HTTPException
import requests
import httpx
from datetime import date, timedelta
from news.getnews import get_finnhub_news as fetch_finnhub_news, get_marketaux_news as fetch_marketaux_news, combine_news_sources
from news.newsengine import save_news_to_db, dynamic_news
from contextlib import asynccontextmanager
import asyncio

async def run_during_runtime():
   while True:
      await dynamic_news()
      await asyncio.sleep(300)  # Run every hour

@asynccontextmanager
async def lifespan(app: FastAPI):
   await save_news_to_db()
   dynamic_update = asyncio.create_task(run_during_runtime())
   app.state.task = dynamic_update
   try:
      yield

   finally:
      dynamic_update.cancel()
      try:
         await dynamic_update
      except asyncio.CancelledError:
         print("Task cancelled")

app = FastAPI(lifespan=lifespan)


@app.get("/news/marketaux")
async def get_marketaux_news():
    news = await fetch_marketaux_news()

    return news


