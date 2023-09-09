from bson import ObjectId
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from dynaconf import settings

from src.modules.common.mongo_utils import mongo_utils

client = MongoClient(settings.MONGO_DB_URL)
# client = MongoClient("mongodb://localhost:27017")
db = client['Users'] # Change this!
rewards = db['rewards']

class rw_data:

    @staticmethod
    def postReward(ria):
        mongo = mongo_utils.get_mongo()
        _userId = ria[0]
        _couponName = ria[1]
        _amount = ria[2]
        _pointsRedeemed = ria[3]
        _rewardTimeStamp = ria[4]
        _expiryTimeStamp = ria[5]

        return mongo.db.rewards.insert_one({'userId':_userId, 'couponName':_couponName, 'amount':_amount, 'pointsRedeemed':_pointsRedeemed, 
                                            'rewardTimeStamp':_rewardTimeStamp, 'expiryTimeStamp':_expiryTimeStamp})
    
    @staticmethod
    def getRewardById(id, current_user):
        mongo = mongo_utils.get_mongo()
        result = mongo.db.rewards.find_one({'_id':ObjectId(id)})
        return result
    
    @staticmethod
    def getAllRewards():
        mongo = mongo_utils.get_mongo()
        results = mongo.db.rewards.find()
        return results
    
    @staticmethod
    def updateReward(ria):
        mongo = mongo_utils.get_mongo()
        _rewardId = ria[0]
        _userId = ria[1]
        _couponName = ria[2]
        _amount = ria[3]
        _pointsRedeemed = ria[4]
        _rewardTimeStamp = ria[5]
        _expiryTimeStamp = ria[6]

        return mongo.db.rewards.update_one({'_id':ObjectId(_rewardId['$oid']) if '$oid' in _rewardId else ObjectId(_rewardId)}, 
                                      {'$set': {'couponName':_couponName, 'amount':_amount, 'pointsRedeemed':_pointsRedeemed, 
                                                'rewardTimeStamp':_rewardTimeStamp, 'expiryTimeStamp':_expiryTimeStamp}})
    
    @staticmethod
    def deleteRewardById(_rewardId, current_user):
        mongo = mongo_utils.get_mongo()
        return mongo.db.comments.delete_one({'_id':ObjectId(_rewardId['$oid']) if '$oid' in _rewardId else ObjectId(_rewardId)})
    