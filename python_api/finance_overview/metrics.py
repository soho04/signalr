from fastapi import HTTPException
from helper import get_ticker
import yfinance as yf
import pandas as pd

def get_valuation(ticker: yf.Ticker) -> dict:
    info = ticker.info
    
    return {
        "trailing_PE": info.get("trailingPE"),
        "forward_PE": info.get("forwardPE"),
        "ebidta": info.get("ebitda"),
        "price_to_book": info.get("priceToBook")
    }

def get_profitability(ticker: yf.Ticker) -> dict:
    info = ticker.info

    return {
        "return_on_equity": info.get("returnOnEquity"),
        "return_on_assets": info.get("returnOnAssets"),
        "ebidta": info.get("ebitda"),
        "profit_margins": info.get("profitMargins"),
        "gross_margins": info.get("grossMargins"),
        "operating_margin": info.get("operatingMargins"),
        "gross_profits": info.get("grossProfits"),
    }

def get_liquidity(ticker: yf.Ticker) -> dict:
    info = ticker.info

    return {
        "current_ratio": info.get("currentRatio"),
        "debt_to_equity": info.get("debtToEquity"),
    }

def get_growth(ticker: yf.Ticker) -> dict:
    info = ticker.info

    return {
        "earnings_growth": info.get("earningsGrowth"),
        "revenue_growth": info.get("revenueGrowth"),
        "quarterly_earnings_growth": info.get("earningsQuarterlyGrowth"),
        "target_mean_price": info.get("targetMeanPrice"),
        "forward_PE": info.get("forwardPE"),
    }

