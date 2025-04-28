from fastapi import FastAPI
from models import Article, UpdatedArticle
import mongoManager

app = FastAPI()

articles = {
    1 : {
        "title" : "My First Post",
        "description" : "I hope that I would be able to end this project",
        "date" : "April 28",
    },
}

mongoManager.ping()

@app.get("/")
async def root():
    return {"message" : "Personal Blog Platform"}

@app.get("/articles")
def getArticles():
    return articles

@app.get("/getarticle/{article_id}")
def getSingleArticle(article_id : int):
    if article_id not in articles:
        return {"error" : "Article Not Found"}

    return articles[article_id]

@app.post("/createarticle/{article_id}")
def createArticle(article_id : int, article : Article):
    if article_id in articles:
        return {"error" : "Article ID already taken"}

    articles[article_id] = article
    return {"succes" : "Article Succesfully Added"}

@app.delete("/deletearticle/{article_id}")
def deleteArticle(article_id : int):
    if article_id not in articles:
        return {"error" : "Article Not Found"}

    del articles[article_id]
    return {"succes" : "Article Succesfully Deleted"}

@app.put("/updatearticle/{article_id}")
def updateArticle(article_id: int, article: UpdatedArticle):
    if article_id not in articles:
        return {"error": "Article Not Found"}
    
    if article.title is not None:
        articles[article_id]["title"] = article.title
    
    if article.description is not None:
        articles[article_id]["description"] = article.description
    
    return {"success": "Article Successfully Updated"}
