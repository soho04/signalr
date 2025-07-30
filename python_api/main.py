from fastapi import FastAPI, HTTPException
from news.newsengine import save_news_to_db, dynamic_news
from contextlib import asynccontextmanager
import asyncio
from finance_overview.metrics import *
from finance_overview.overview import *
from finance_overview.ratings import *
from finance_overview.helper import get_ticker


async def run_during_runtime():
   while True:
      await dynamic_news()
      await asyncio.sleep(300) 

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

# @app.get("/news/marketaux")
# async def get_marketaux_news():
#     news = await fetch_marketaux_news("PLTR")

#     return news

@app.get("/overview/{symbol}")
def overview(symbol: str):
   ticker = get_ticker(symbol)
   return get_company_overview(ticker)

@app.get("/income-statement/{symbol}")
def income(symbol: str):
   ticker = get_ticker(symbol)
   return get_income_statement(ticker)

@app.get("/balance-sheet/{symbol}")
def balance(symbol: str):
   ticker = get_ticker(symbol)
   return get_balance_sheet(ticker)

@app.get("/cashflow/{symbol}")
def cashflow(symbol: str):
   ticker = get_ticker(symbol)
   return get_cashflow(ticker)

@app.get("/profitability/{symbol}")
def profitability(symbol: str):
   ticker = get_ticker(symbol)
   return get_profitability(ticker)

@app.get("/valuation/{symbol}")
def valuation(symbol: str):
   ticker = get_ticker(symbol)
   return get_valuation(ticker)

@app.get("/liquidity/{symbol}")
async def liquidity(symbol: str):
   ticker = get_ticker(symbol)
   return get_liquidity(ticker)

@app.get("/growth/{symbol}")
async def get_growth(symbol: str):
   ticker = get_ticker(symbol)
   return get_growth(ticker)

@app.get("/ratings/{symbol}")
async def ratings(symbol: str):
    try:
        return get_ratings(symbol.upper())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

