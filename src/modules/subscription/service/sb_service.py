from src.modules.subscription.models.sb_data import sb_data

class sb_service:

    @staticmethod
    def postSubscription(subscription_info_array):
        return sb_data.postSubscription(subscription_info_array)
    
    @staticmethod
    def getSubscriptionById(id, current_user):
        return sb_data.getSubscriptionById(id, current_user)
    
    @staticmethod
    def getAllSubscriptions():
        return sb_data.getAllSubscriptions()
    
    @staticmethod
    def updateSubscription(subscription_info_array):
        return sb_data.updateSubscription(subscription_info_array)
    
    @staticmethod
    def deleteSubscriptionById(_subscriptionId, current_user):
        return sb_data.deleteSubscriptionById(_subscriptionId, current_user)
