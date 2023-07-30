from src.modules.comments.models.com_data import com_data

class com_service:

    @staticmethod
    def postComment(comment_info_array):
        return com_data.postComment(comment_info_array)
    
    @staticmethod
    def getCommentById(id):
        return com_data.getCommentById(id)
    
    @staticmethod
    def updateComment(comment_info_array):
        return com_data.updateComment(comment_info_array)
    
    @staticmethod
    def deleteCommentById(id):
        return com_data.deleteCommentById(id)