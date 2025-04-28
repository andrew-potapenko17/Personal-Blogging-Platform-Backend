from fastapi import FastAPI
from models import Article, UpdatedArticle
import mongoManager as db

app = FastAPI()

@app.get("/articles")
def getArticles():
    return db.get_articles()

@app.get("/getarticle/{article_id}")
def getSingleArticle(article_id : str):
    return db.get_single_article(article_id)

@app.post("/createarticle")
def createArticle(article : Article):
    return db.post_article(article)

@app.delete("/deletearticle/{article_id}")
def deleteArticle(article_id : str):
    return db.delete_article(article_id)

@app.put("/updatearticle/{article_id}")
def updateArticle(article_id: str, article: UpdatedArticle):
    return db.update_article(article_id, article)
