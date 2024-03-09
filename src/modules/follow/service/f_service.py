from src.modules.follow.models.f_data import f_data

class f_service:

    @staticmethod
    def postFollow(follow_info_array):
        return f_data.postFollow(follow_info_array)
    
    @staticmethod
    def getFollow(id, current_user):
        return f_data.getFollow(id, current_user)
    
    @staticmethod
    def getAllFollows():
        return f_data.getAllFollows()
      
    
