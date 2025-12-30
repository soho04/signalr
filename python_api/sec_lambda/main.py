from fastapi import FastAPI
from trails import *

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SEC Lambda is running"}

@app.get("/revenue_trail/{symbol}")
def get_revenue_trail(symbol: str):
   return revenue_trail(symbol)

@app.get("/revenue_trail_growth/{symbol}")
def get_revenue_trail(symbol: str):
   return revenue_trail_growth(symbol)

@app.get("/eps_trail/{symbol}")
def get_eps_trail(symbol: str):
   return get_eps(symbol)

@app.get("/eps_trail_growth/{symbol}")
def get_eps_trail_growth(symbol: str):
   return eps_trail_growth(symbol)
