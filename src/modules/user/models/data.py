from bson import ObjectId
from pymongo import MongoClient
from dynaconf import settings
from src.modules.common.mongo_utils import mongo_utils

# client = MongoClient(settings.MONGO_DB_URL)
client = MongoClient(settings.MONGO_DB_URL)
db = client['Users'] # Change this!
users = db['user']

class Data:
    @staticmethod
    def get_all_data():
        return users.find()
        # return settings.MONGO_DB_URL

    @staticmethod
    def add_data(data):
        # collection.insert_one(data)
        return None
    
    @staticmethod
    def questionsSaved(current_user, questionId):
        mongo = mongo_utils.get_mongo()
        result = mongo.db.user.find_one({'_id':ObjectId(current_user)})
        if result:
            if questionId not in result['savedQuestions']:
                result['savedQuestions'].append(questionId)
                print(result['savedQuestions'])
                mongo.db.user.update_one({'_id':ObjectId(current_user['$oid']) if '$oid' in current_user else ObjectId(current_user)}, 
                                      {'$set': {'savedQuestions':result['savedQuestions']}})
                return "Saved Question!"
            else:
                return "Already Saved!"
        return result
    

