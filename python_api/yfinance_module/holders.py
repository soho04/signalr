from yfinance_module.helper import get_ticker

def top5_holders(Ticker: str) -> dict:
    ticker = get_ticker("PLTR")
    df = ticker.institutional_holders.head(5)

    if df is None or df.empty:
        return {}
    
    return (
        df.set_index("Holder").to_dict(orient="index")
    )