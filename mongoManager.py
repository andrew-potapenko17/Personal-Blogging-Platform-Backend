from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import backendConfig

client = MongoClient(backendConfig.MONGO_URL, server_api=ServerApi('1'))
def ping():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
