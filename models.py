from pydantic import BaseModel
from typing import Optional

class Article(BaseModel):
    title : str
    description : str
    date : str

class UpdatedArticle(BaseModel):
    title : Optional[str] = None
    description : Optional[str] = None
    date : Optional[str] = None