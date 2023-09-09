from bson import ObjectId
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from dynaconf import settings

from src.modules.common.mongo_utils import mongo_utils

client = MongoClient(settings.MONGO_DB_URL)
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
    def updatelike(answerId, isLiked):
        mongo = mongo_utils.get_mongo()
        result = mongo.db.answers.find_one({'_id':ObjectId(answerId)})
        if result:
            if isLiked == "yes":
                result['likes'] += 1
                mongo.db.answers.update_one({'_id':ObjectId(answerId['$oid']) if '$oid' in answerId else ObjectId(answerId)}, 
                                      {'$set': {'likes':result['likes']}})
                return "Liked!"
            elif isLiked == "no":
                result['likes'] -= 1
                mongo.db.answers.update_one({'_id':ObjectId(answerId['$oid']) if '$oid' in answerId else ObjectId(answerId)}, 
                                      {'$set': {'likes':result['likes']}})
                return "Disliked"
        return result    

    @staticmethod
    def getAnswerById(id):
        mongo = mongo_utils.get_mongo()
        return mongo.db.answers.find_one({'_id':ObjectId(id)})
    
    @staticmethod
    def getAllAnswers():
        mongo = mongo_utils.get_mongo()
        return mongo.db.answers.find()

    @staticmethod
    def updateAnswer(aia):
        mongo = mongo_utils.get_mongo()
        _answerId = aia[0]
        _answer = aia[1]
        _userId = aia[2]
        _updatedTimeStamp = aia[3]
        _isQualifiedRealTime = aia[4]
        
        return mongo.db.answers.update_one({'_id':ObjectId(_answerId['$oid']) if '$oid' in _answerId else ObjectId(_answerId)}, 
                                      {'$set': {'answer':_answer, 'userId':_userId, 'updatedTimeStamp':_updatedTimeStamp, 'isQualifiedRealTime':_isQualifiedRealTime}})