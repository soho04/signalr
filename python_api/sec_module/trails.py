import numpy as np
import pandas as pd
from sec_module.sec import retrieve_filing

tags = ["Revenues", "SalesRevenueNet", "RevenueFromContractWithCustomerExcludingAssessedTax"]
eps_tags = ["EarningsPerShareDiluted", "EarningsPerShareBasic"]

def revenue_trail(Ticker: str) -> dict:
    filing = retrieve_filing(Ticker)
    data = filing["us-gaap"]
    rows = []

    for tag in tags:
        if tag not in data:
            continue

        for unit, entries in data[tag]["units"].items():
            if unit not in ["USD", "USDm"]:
                continue

            multiplier = 1_000_000 if unit == "USDm" else 1

            for e in entries:
                if e.get("form") == "10-K":
                    rows.append({
                        "year": e["fy"],
                        "revenue": e["val"] * multiplier,
                        "filed": e["filed"]
                    })

    df = pd.DataFrame(rows, columns=["year", "revenue"])

    if df.empty:
        return []

    df = (
        pd.DataFrame(rows)
        .sort_values(["year", "filed"])
        .drop_duplicates("year", keep="last")  
        .sort_values("year", ascending=False)
        .head(10)                               
        .sort_values("year")
        .reset_index(drop=True)
    )

    return df.to_dict(orient="records")


def revenue_trail_growth(Ticker: str) -> dict:
    data = revenue_trail(Ticker)

    if not data:
        return []

    df = pd.DataFrame(data).sort_values("year")

    df["revenue_growth_pct"] = (
        df["revenue"].pct_change() * 100
    ).round(2)

    df = df.where(pd.notnull(df), 0)

    return df.to_dict(orient="records")

def get_eps(Ticker: str) -> dict:
    filing = retrieve_filing(Ticker)
    
    data = filing["us-gaap"]
    rows = []

    for tag in eps_tags:
        if tag not in data:
            continue

        for _, entries in data[tag]["units"].items():
            for e in entries:
                if e.get("form") == "10-K":
                    rows.append({
                        "year": e.get("fy"),
                        "eps": e["val"],
                        "type": "diluted" if "Diluted" in tag else "basic",
                        "filed": e.get("filed")
                    })

    df = pd.DataFrame(rows)

    if df.empty:
        return []
    
    df = (
        df.sort_values(["year", "filed"])
          .drop_duplicates(["year", "type"], keep="last")
          .sort_values("year")
          .reset_index(drop=True)
    )

    df = df[df["type"] == "basic"]

    return df.to_dict(orient="records")

def eps_trail_growth(Ticker: str) -> dict:
    eps = get_eps(Ticker)

    df = pd.DataFrame(eps).sort_values("year")

    df["eps_growth_pct"] = (df["eps"].pct_change() * 100).round(2)

    df.loc[df.index[0], "eps_growth_pct"] = 0.0

    df.replace([np.inf, -np.inf], None, inplace=True)
    df = df.astype(object).where(pd.notnull(df), None)

    return df.to_dict(orient="records")
