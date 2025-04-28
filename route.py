from fastapi import APIRouter
from models import Article, UpdatedArticle
from mongoManager import collection_name
from schemas import list_serial
from bson import ObjectId

router = APIRouter()

# GET Request Method
@router.get("/")
async def get_article():
    articles = list_serial(collection_name.find())
    return articles

# POST Request Method
@router.post("/")
async def post_article(article : Article):
    collection_name.insert_one(dict(article))

# PUT Request Method
@router.put("/{id}")
async def put_article(id : str, article : UpdatedArticle):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(article)})

@router.delete("/{id}")
async def delete_article(id : str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})



