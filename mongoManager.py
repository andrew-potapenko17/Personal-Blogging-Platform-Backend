from models import Article, UpdatedArticle
from backendConfig import collection_name
from schemas import list_serial
from bson import ObjectId

# GET Request Methods
def get_articles():
    articles = list_serial(collection_name.find())
    return articles

def get_single_article(id : str):
    article = collection_name.find_one({"_id": ObjectId(id)})
    article["_id"] = str(article["_id"])
    return article

# POST Request Method
def post_article(article : Article):
    collection_name.insert_one(dict(article))
    return {"succes" : "Article Succesfully Created"}

# PUT Request Method
def update_article(id : str, article : UpdatedArticle):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(article)})
    return {"succes" : "Article Succesfully Updated"}

# Delete Request Method
def delete_article(id : str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"succes" : "Article Succesfully Deleted"}