from bson import ObjectId
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from dynaconf import settings

from src.modules.common.mongo_utils import mongo_utils

client = MongoClient(settings.MONGO_DB_URL)
# client = MongoClient("mongodb://localhost:27017")
db = client['Users'] # Change this!
questions = db['questions']


class q_data:

    @staticmethod
    def postQuestion(qia):
        mongo = mongo_utils.get_mongo()
        _title = qia[0]
        _description = qia[1]
        _userId = qia[2]
        _savedBy = qia[3]
        _noOfReposts = qia[4]
        _isRealTime = qia[5]
        _createdTimeStamp = qia[6]
        _updatedTimeStamp = qia[7]
        _tags = qia[8]
        _views = qia[9]

        return mongo.db.questions.insert_one({'title':_title, 'description':_description, 'userId':_userId, 'savedBy':_savedBy, 'noOfReposts':_noOfReposts, 'isRealTime':_isRealTime, 
                                    'createdTimeStamp':_createdTimeStamp, 'updatedTimeStamp':_updatedTimeStamp, 'tags':_tags, 'views':_views})
    
    @staticmethod
    def getQuestionById(id, current_user):
        mongo = mongo_utils.get_mongo()
        newViews = []
        result = mongo.db.questions.find_one({'_id':ObjectId(id)})
        if result:
            if current_user not in result['views']:
                newViews = result['views']
                newViews.append(current_user)
                mongo.db.questions.update_one({'_id':ObjectId(id['$oid']) if '$oid' in id else ObjectId(id)}, 
                                      {'$set': {'views':newViews}})
        result['_id'] = str(result['_id'])
        return result
    
    @staticmethod
    def updateQuestion(qia):
        mongo = mongo_utils.get_mongo()
        _id = qia[0]
        _title = qia[1]
        _description = qia[2]
        _userId = qia[3]
        _savedBy = qia[4]
        _noOfReposts = qia[5]
        _isRealTime = qia[6]
        _updatedTimeStamp = qia[7]
        _tags = qia[8]
        _views = qia[9]

        return mongo.db.questions.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, 
                                      {'$set': {'title':_title, 'description':_description, 'userId':_userId, 'savedBy':_savedBy, 'noOfReposts':_noOfReposts, 'isRealTime':_isRealTime, 
                                     'updatedTimeStamp':_updatedTimeStamp, 'tags':_tags, 'views':_views}})
    
    @staticmethod
    def savedBy(current_user, questionId):
        mongo = mongo_utils.get_mongo()
        result = mongo.db.questions.find_one({'_id':ObjectId(questionId)})
        if result:
            if current_user not in result['savedBy']:
                result['savedBy'].append(current_user)
                print(result['savedBy'])
                mongo.db.questions.update_one({'_id':ObjectId(questionId['$oid']) if '$oid' in questionId else ObjectId(questionId)}, 
                                      {'$set': {'savedBy':result['savedBy']}})
                return "User added to Question!"
            else:
                return "User already added to Question"
        return result