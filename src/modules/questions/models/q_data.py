from bson import ObjectId
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from dynaconf import settings

from src.modules.common.mongo_utils import mongo_utils

client = MongoClient(settings.MONGO_DB_URL)
db = client['Users'] # Change this!
questions = db['questions']


class q_data:

    @staticmethod
    def postQuestion(qia):
        mongo = mongo_utils.get_mongo()
        _title = qia[0]
        _uId = qia[1]
        _savedBy = qia[2]
        _noOfReposts = qia[3]
        _isRealTime = qia[4]
        _createdTimeStamp = qia[5]
        _updatedTimeStamp = qia[6]
        _tags = qia[7]
        _views = qia[8]

        return mongo.db.questions.insert_one({'title':_title, 'uId':_uId, 'savedBy':_savedBy, 'noOfReposts':_noOfReposts, 'isRealTime':_isRealTime, 
                                    'createdTimeStamp':_createdTimeStamp, 'updatedTimeStamp':_updatedTimeStamp, 'tags':_tags, 'views':_views})
    
    @staticmethod
    def getQuestionById(id):
        mongo = mongo_utils.get_mongo()
        print(mongo)
        return mongo.db.questions.find_one({'_id':ObjectId(id)})
    
    @staticmethod
    def updateQuestion(qia):
        mongo = mongo_utils.get_mongo()
        _id = qia[0]
        _title = qia[1]
        _uId = qia[2]
        _savedBy = qia[3]
        _noOfReposts = qia[4]
        _isRealTime = qia[5]
        _createdTimeStamp = qia[6]
        _updatedTimeStamp = qia[7]
        _tags = qia[8]
        _views = qia[9]

        return mongo.db.questions.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, 
                                      {'$set': {'title':_title, 'uId':_uId, 'savedBy':_savedBy, 'noOfReposts':_noOfReposts, 'isRealTime':_isRealTime, 
                                    'createdTimeStamp':_createdTimeStamp, 'updatedTimeStamp':_updatedTimeStamp, 'tags':_tags, 'views':_views}})
