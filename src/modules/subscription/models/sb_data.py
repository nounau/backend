from bson import ObjectId
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from dynaconf import settings

from src.modules.common.mongo_utils import mongo_utils

client = MongoClient(settings.MONGO_DB_URL)
db = client['Users'] # Change this!
subscription = db['subscription']

class sb_data:

    @staticmethod
    def postSubscription(sia):
        mongo = mongo_utils.get_mongo()
        _userId = sia[0]
        _purchaseDate = sia[1],
        _endDate = sia[2],
        _purchaseAmount = sia[3],
        _modeOfpayment = sia[4]

        return mongo.db.subscription.insert_one({'userId':_userId, 'purchaseDate':_purchaseDate, 'endDate':_endDate, 
                                            'purchaseAmount':_purchaseAmount, 'modeOfpayment':_modeOfpayment})
    
    @staticmethod
    def getSubscriptionById(id, current_user):
        mongo = mongo_utils.get_mongo()
        result = mongo.db.subscription.find_one({'_id':ObjectId(id)})
        return result
    
    @staticmethod
    def getAllSubscriptions():
        mongo = mongo_utils.get_mongo()
        results = mongo.db.subscription.find()
        return results
    
    @staticmethod
    def updateSubscription(sia):
        mongo = mongo_utils.get_mongo()
        _subscriptionId = sia[0],
        _userId = sia[1],
        _purchaseDate = sia[2],
        _endDate = sia[3],
        _purchaseAmount = sia[4],
        _modeOfpayment = sia[5]

        return mongo.db.subscription.update_one({'_id':ObjectId(_subscriptionId['$oid']) if '$oid' in _subscriptionId else ObjectId(_subscriptionId)}, 
                                      {'$set': {'purchaseDate':_purchaseDate, 'endDate':_endDate, 
                                            'purchaseAmount':_purchaseAmount, 'modeOfpayment':_modeOfpayment}})
    
    @staticmethod
    def deleteSubscriptionById(_subscriptionId, current_user):
        mongo = mongo_utils.get_mongo()
        return mongo.db.subscription.delete_one({'_id':ObjectId(_subscriptionId['$oid']) if '$oid' in _subscriptionId else ObjectId(_subscriptionId)})