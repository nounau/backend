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
        _userId = cia[0]
        _questionId = cia[1]
        _answerId = cia[2]
        _commentType = cia[3]
        _comment = cia[4]
        _createdTimeStamp = cia[5]
        _updatedTimeStamp = cia[6]

        return mongo.db.comments.insert_one({'userId':_userId, 'questionId':_questionId, 'answerId':_answerId, 'commentType':_commentType, 'comment':_comment,
                                    'createdTimeStamp':_createdTimeStamp, 'updatedTimeStamp':_updatedTimeStamp})
    
    @staticmethod
    def getCommentById(commentId, current_user):
        mongo = mongo_utils.get_mongo()
        print(mongo)
        return mongo.db.comments.find_one({'_id':ObjectId(commentId)})
    
    @staticmethod
    def updateComment(cia):
        mongo = mongo_utils.get_mongo()
        _commentId = cia[0]
        _userId = cia[1]
        _comment = cia[2]
        _updatedTimeStamp =cia[3]

        return mongo.db.comments.update_one({'_id':ObjectId(_commentId['$oid']) if '$oid' in _commentId else ObjectId(_commentId)}, 
                                      {'$set': {'comment':_comment, 'updatedTimeStamp':_updatedTimeStamp}})
    
    @staticmethod
    def deleteCommentById(commentId, current_user):
        mongo = mongo_utils.get_mongo()
        return mongo.db.comments.delete_one({'_id':ObjectId(commentId['$oid']) if '$oid' in commentId else ObjectId(commentId)})
