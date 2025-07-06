from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NewsItem(BaseModel):
    
    def __init__(self, source, title, url, published_at, summary):
        self.source = source
        self.title = title
        self.url = url
        self.published_at = published_at
        self.summary = summary
    
    def to_dict(self):
        return {
            "source": self.source,
            "title": self.title,
            "url": self.url,
            "published_at": self.published_at.isoformat() if isinstance(self.published_at, datetime) else self.published_at,
            "summary": self.summary
        }