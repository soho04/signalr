from helper import get_ticker

def get_risk_score(Ticker: str) -> dict:

    ticker = get_ticker(Ticker)
    print(ticker.info["city"])
    # print(ticker.history)

    

get_risk_score("PLTR")
