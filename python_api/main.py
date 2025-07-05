from fastapi import FastAPI, HTTPException
import requests
import httpx
from datetime import date, timedelta

app = FastAPI()

FINNHUB_API_KEY = "d1kht4hr01qt8foomrh0d1kht4hr01qt8foomrhg"

# Get latest news from external APIs
@app.get("/news/{ticker}")
async def get_news(ticker: str):
    
    today, aweekago = date.today(), date.today() - timedelta(days=7)
    today_str, aweekago_str = today.isoformat(), aweekago.isoformat()
    
    
    url = "https://finnhub.io/api/v1/company-news"
    params = {
        "symbol": ticker.upper(),
        "from": aweekago_str,
        "to": today_str,
        "token": FINNHUB_API_KEY,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching news")
        
        news_data = response.json()

        return {"ticker": "PLTR", "news": news_data[:5]}