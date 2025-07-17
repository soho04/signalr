from fastapi import HTTPException
from helper import helper_safe_get, get_ticker
import yfinance as yf
import pandas as pd

def valuation(ticker: yf.Ticker) -> dict:
    info = ticker.info
    
    return {
        "trailing_PE": helper_safe_get(info, "trailingPE"),
        "forward_PE": helper_safe_get(info, "forwardPE"),
        "ebidta": helper_safe_get(info, "ebitda"),
        "price_to_book": helper_safe_get(info, "priceToBook")
    }

def profitability(ticker: yf.Ticker) -> dict:
    info = ticker.info

    return {
        "return_on_equity": helper_safe_get(info, "returnOnEquity"),
        "return_on_assets": helper_safe_get(info, "returnOnAssets"),
        "ebidta": helper_safe_get(info, "ebitda"),
        "profit_margins": helper_safe_get(info, "profitMargins"),
        "gross_margins": helper_safe_get(info, "grossMargins"),
        "operating_margin": helper_safe_get(info, "operatingMargins"),
        "gross_profits": helper_safe_get(info, "grossProfits"),
    }

def liquidity(ticker: yf.Ticker) -> dict:
    info = ticker.info

    return {
        
    }

def growth(ticker: yf.Ticker) -> dict:
    info = ticker.info

