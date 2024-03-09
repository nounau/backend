from src.modules.rewards.models.rw_data import rw_data

class rw_service:

    @staticmethod
    def postReward(reward_info_array):
        return rw_data.postReward(reward_info_array)
    
    @staticmethod
    def getRewardById(id, current_user):
        return rw_data.getRewardById(id, current_user)
    
    @staticmethod
    def getAllRewards():
        return rw_data.getAllRewards()
    
    @staticmethod
    def updateReward(reward_info_array):
        return rw_data.updateReward(reward_info_array)
    
    @staticmethod
    def deleteRewardById(_rewardId, current_user):
        return rw_data.deleteRewardById(_rewardId, current_user)