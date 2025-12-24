from fastapi import FastAPI, HTTPException
from sec_module.trails import *
from yfinance_module.overview import *
from yfinance_module.helper import get_ticker
from yfinance_module.holders import top5_holders
from sec_module.trails import *

app = FastAPI()

@app.get("/test/{symbol}")
def test(symbol: str):
   return top5_holders(symbol)

@app.get("/overview/{symbol}")
def overview(symbol: str):
   ticker = get_ticker(symbol)
   return get_company_overview(ticker)

@app.get("/income-statement/{symbol}")
def income(symbol: str):
   ticker = get_ticker(symbol)
   return get_income_statement(ticker)

@app.get("/growth/{symbol}")
def get_growth(symbol: str):
   ticker = get_ticker(symbol)
   return get_growth(ticker)

@app.get("/revenue_trail/{symbol}")
def get_revenue_trail(symbol: str):
   ticker = get_ticker(symbol)
   return get_revenue_trail(ticker)

