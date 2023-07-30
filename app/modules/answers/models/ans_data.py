from bson import ObjectId
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

from app.modules.common.mongo_utils import mongo_utils

client = MongoClient('mongodb://localhost:27017/')
db = client['Users'] # Change this!
answers = db['answers']

class ans_data:
    @staticmethod
    def postAnswer(aia):
        mongo = mongo_utils.get_mongo()
        _questionId = aia[0]
        _answer = aia[1]
        _userId = aia[2]
        _likes = aia[3]
        _comments = aia[4]
        _createdTimeStamp = aia[5]
        _updatedTimeStamp = aia[6]
        _isQualifiedRealTime = aia[7]

        return mongo.db.answers.insert_one({'questionId':_questionId, 'answer':_answer, 'userId':_userId, 'likes':_likes, 'comments':_comments, 
                                    'createdTimeStamp':_createdTimeStamp, 'updatedTimeStamp':_updatedTimeStamp, 'isQualifiedRealTime':_isQualifiedRealTime})
    
    @staticmethod
    def getAnswerById(aia):
        mongo = mongo_utils.get_mongo()
        print(mongo)
        return mongo.db.answers.find_one({'_id':ObjectId(id)})

    @staticmethod
    def updateAnswer(aia):
        mongo = mongo_utils.get_mongo()
        _id = aia[0]
        _questionId = aia[1]
        _answer = aia[2]
        _userId = aia[3]
        _likes = aia[4]
        _comments = aia[5]
        _createdTimeStamp = aia[6]
        _updatedTimeStamp = aia[7]
        _isQualifiedRealTime = aia[8]
        
        return mongo.db.answers.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, 
                                      {'$set': {'questionId':_questionId, 'answer':_answer, 'userId':_userId, 'likes':_likes, 'comments':_comments, 
                                    'createdTimeStamp':_createdTimeStamp, 'updatedTimeStamp':_updatedTimeStamp, 'isQualifiedRealTime':_isQualifiedRealTime}})