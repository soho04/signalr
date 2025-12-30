import yfinance as yf
from helper import helper_safe_get
    
def get_company_overview(ticker: yf.Ticker) -> dict:
    profile = ticker.info
    executives = profile.get("companyOfficers", []) or []
    ceo = next((e.get("name") for e in executives if "ceo" in e.get("title", "").lower()), None)

    return {
        "name": profile.get("longName"),
        "ceo": ceo,
        "sector": profile.get("sector"),
        "industry": profile.get("industry"),
        "country": profile.get("country"),
        "employeecount": profile.get("fullTimeEmployees"),
        "exchange": profile.get("exchange"),
        "market_cap": profile.get("marketCap"),
        "pe_ratio": profile.get("trailingPE"),
        "eps": profile.get("trailingEps"),
        "52_week_high": profile.get("fiftyTwoWeekHigh"),
        "52_week_low": profile.get("fiftyTwoWeekLow")
    }

def get_income_statement(ticker: yf.Ticker) -> dict:
    fs = ticker.financials
    scale = 1e6

    return {
        "revenue": helper_safe_get(fs, "Total Revenue", scale),
        "net_income": helper_safe_get(fs, "Net Income", scale),
        "EPS": helper_safe_get(fs, "Basic EPS", scale),
        "operating_income": helper_safe_get(fs, "Operating Income", scale),
        "gross_profit": helper_safe_get(fs, "Gross Profit", scale)
    }