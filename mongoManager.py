from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import backendConfig

client = MongoClient(backendConfig.MONGO_URL, server_api=ServerApi('1'))

db = client.articles_db

collection_name = db["articles_collection"]