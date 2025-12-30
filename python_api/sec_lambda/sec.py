import requests

identification = {"User-Agent": "Ash Rana ashimsr@hotmail.com"}


def retrieve_company_cik(Ticker: str):
    url = "https://www.sec.gov/files/company_tickers.json"
    keys = requests.get(url, headers=identification).json()
    
    for _, v in keys.items():
        if v["ticker"].upper() == Ticker.upper():
            return str(v["cik_str"]).zfill(10)

    raise ValueError(f"{Ticker} not found")

def retrieve_filing(Ticker: str):
    cik = retrieve_company_cik(Ticker)
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    response = requests.get(url, headers=identification)
    response.raise_for_status
    return response.json()["facts"]


