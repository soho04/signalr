from fastapi import FastAPI, HTTPException
from overview import *
from helper import get_ticker, cached
from holders import top5_holders
from mangum import Mangum
import requests

app = FastAPI(root_path="/finance")

handler = Mangum(app)

@app.get("/")
def root():
    return {"message": "finance Lambda is running"}

@app.get("/holders/{symbol}")
def holders(symbol: str):
   ticker = get_ticker(symbol)
   return cached(
      key=f"holders:{symbol}",
      fetch_fn=lambda: yahoo_handler(lambda: top5_holders(ticker)),
      ttl=300
   )

@app.get("/overview/{symbol}")
def overview(symbol: str):
   ticker = get_ticker(symbol)
   return cached(
      key=f"overview:{symbol}",
      fetch_fn=lambda: yahoo_handler(lambda: get_company_overview(ticker)),
      ttl=300
   )

@app.get("/income-statement/{symbol}")
def income(symbol: str):
   ticker = get_ticker(symbol)
   return cached(
      key=f"income-statement:{symbol}",
      fetch_fn=lambda: yahoo_handler(lambda: get_income_statement(ticker)),
      ttl=300
   )

def yahoo_handler(fetch_fn):
    try:
        return fetch_fn()

    except requests.HTTPError as e:
        if e.response is not None and e.response.status_code == 429:
            raise HTTPException(
                status_code=429,
                detail="Yahoo Finance rate limit exceeded. Please try again shortly."
            )
        raise HTTPException(
            status_code=502,
            detail="Upstream Yahoo Finance error."
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal server error while fetching market data."
        )


