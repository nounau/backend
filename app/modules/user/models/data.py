from pymongo import MongoClient
from dynaconf import settings
from app.modules.common.mongo_utils import mongo_utils

# client = MongoClient(settings.MONGO_DB_URL)
client = MongoClient('mongodb://localhost:27017/')
db = client['Users'] # Change this!
users = db['user']

class Data:
    @staticmethod
    def get_all_data():
        #return users.find({})
        return settings.MONGO_DB_URL

    @staticmethod
    def add_data(data):
        # collection.insert_one(data)
        return None
