from fastapi import HTTPException
import yfinance as yf
import pandas as pd

def get_ticker(symbol: str) -> yf.Ticker:
    try:
        return yf.Ticker(symbol)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid symbol or yfinance error: {e}")

def helper_safe_get(df: pd.DataFrame, key: str, scale: float = 1.0) -> float | None:
    try:
        value = df.loc[key].iloc[0]
        if pd.isna(value):
            return None
        return float(value) / scale
    except (KeyError, IndexError):
        return None