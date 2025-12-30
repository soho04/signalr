from fastapi import FastAPI, HTTPException
from overview import *
from helper import get_ticker
from holders import top5_holders

app = FastAPI()

@app.get("/")
def root():
    return {"message": "finance Lambda is running"}

@app.get("/holders/{symbol}")
def holders(symbol: str):
   ticker = get_ticker(symbol)
   return top5_holders(ticker)

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
