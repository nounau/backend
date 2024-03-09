from bson import ObjectId
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from dynaconf import settings

from src.modules.common.mongo_utils import mongo_utils

client = MongoClient(settings.MONGO_DB_URL)
# client = MongoClient("mongodb://localhost:27017")
db = client['Users'] # Change this!
follow = db['follow']

class f_data:

    @staticmethod
    def postFollow(fia):
        mongo = mongo_utils.get_mongo()
        _userId = fia[0]
        _followingId = fia[1]

        return mongo.db.follow.insert_one({'userId':_userId, 'followingId':_followingId})
    
    