from bson import ObjectId
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from dynaconf import settings

from src.modules.common.mongo_utils import mongo_utils

client = MongoClient(settings.MONGO_DB_URL)
db = client['Users'] # Change this!
comments = db['comments']
mongo = mongo_utils.get_mongo()

class com_data:

    @staticmethod
    def postComment(cia):
        mongo = mongo_utils.get_mongo()
        _uId = cia['uId']
        _questionId = cia['questionId']
        _answerId = cia['answerId']
        _commentType = cia['commentType']
        _comment = cia['comment']
        _createdTimeStamp = cia['createdTimeStamp']
        _updatedTimeStamp = cia['updatedTimeStamp']

        return mongo.db.comments.insert_one({'uId':_uId, 'questionId':_questionId, 'answerId':_answerId, 'commentType':_commentType, 'comment':_comment,
                                    'createdTimeStamp':_createdTimeStamp, 'updatedTimeStamp':_updatedTimeStamp})
    
    @staticmethod
    def getCommentById(id):
        mongo = mongo_utils.get_mongo()
        print(mongo)
        return mongo.db.comments.find_one({'_id':ObjectId(id)})
    
    @staticmethod
    def updateComment(cia):
        mongo = mongo_utils.get_mongo()
        _id = cia[0]
        _uId = cia[1]
        _questionId = cia[2]
        _answerId = cia[3]
        _commentType = cia[4]
        _comment = cia[5]
        _createdTimeStamp = cia[6]
        _updatedTimeStamp =cia[7]

        return mongo.db.comments.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, 
                                      {'$set': {'uId':_uId, 'questionId':_questionId, 'answerId':_answerId, 'commentType':_commentType, 'comment':_comment,
                                    'createdTimeStamp':_createdTimeStamp, 'updatedTimeStamp':_updatedTimeStamp}})
    
    @staticmethod
    def deleteCommentById(id):
        _id = id
        return mongo.db.comments.filter_by(id=_id).delete() 
