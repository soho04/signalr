from pymongo import MongoClient
from .getnews import combine_news_sources as combine
import asyncio 
from motor.motor_asyncio import AsyncIOMotorClient

mongo_client = AsyncIOMotorClient("mongodb+srv://ashimsr:t0PVze81k8tjkvql@article-database.l9wqjqr.mongodb.net/?retryWrites=true&w=majority&appName=article-database")

db = mongo_client["articles"]
collection = db["articles-record"]

async def save_news_to_db():
    news_items = await combine()
    
    for article in news_items:
        existing = await collection.find_one({"title": article["title"]})
        if not existing:
            await collection.insert_one(article)

async def dynamic_news():
   async def polling_loop():
        while True:
            await save_news_to_db()
            await asyncio.sleep(300)
    
        asyncio.create_task(polling_loop())


