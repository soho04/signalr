from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NewsItem(BaseModel):
    source: str
    title: str
    url: str
    published_at: datetime
    ticker: Optional[str]
    summary: Optional[str]
    category: Optional[str]