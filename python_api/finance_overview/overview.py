import yfinance as yf
import pandas as pd
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

def get_balance_sheet(ticker: yf.Ticker) -> dict:
    bs = ticker.balance_sheet
    scale = 1e6

    return {
        "cash": helper_safe_get(bs, "Cash And Cash Equivalents", scale),
        "net_receivables": helper_safe_get(bs, "Receivables", scale),
        "inventory": helper_safe_get(bs, "Inventory", scale) or helper_safe_get(bs, "Prepaid Assets", scale),
        "total_current_assets": helper_safe_get(bs, "Total Current Assets", scale) or helper_safe_get(bs, "Total Assets", scale),
        "accounts_payable": helper_safe_get(bs, "Accounts Payable", scale),
        "total_debt": helper_safe_get(bs, "Total Debt", scale),
        "long_term_debt": helper_safe_get(bs, "Long Term Debt", scale),
        "total_liabilities": helper_safe_get(bs, "Current Liabilities", scale),
        "common_stock": helper_safe_get(bs, "Common Stock", scale),
        "retained_earnings": helper_safe_get(bs, "Retained Earnings", scale),
        "treasury_stock": helper_safe_get(bs, "Treasury Stock", scale),
        "total_stockholder_equity": helper_safe_get(bs, "Stockholders Equity", scale)
    }

def get_cashflow(Ticker: yf.Ticker) -> dict:
    cf = Ticker.cashflow
    scale = 1e6

    return {
        "operating_cash_flow": helper_safe_get(cf, "Operating Cash Flow", scale),
        "capital_expenditures": helper_safe_get(cf, "Capital Expenditures", scale) or helper_safe_get(cf, "Capital Expenditure", scale),
        "free_cash_flow": helper_safe_get(cf, "Free Cash Flow", scale),
        "investing_cash_flow": helper_safe_get(cf, "Investing Cash Flow", scale),
        "financing_cash_flow": helper_safe_get(cf, "Financing Cash Flow", scale),
        "net_change_in_cash": helper_safe_get(cf, "Change In Cash", scale)
    }