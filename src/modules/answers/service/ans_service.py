from src.modules.answers.models.ans_data import ans_data

class ans_service:

    @staticmethod
    def postAnswer(answer_info_array):
        return ans_data.postAnswer(answer_info_array)
    
    @staticmethod
    def updatelike(answerId, isLiked):
        return ans_data.updatelike(answerId, isLiked)
    
    @staticmethod
    def getAnswerById(id):
        return ans_data.getAnswerById(id)

    @staticmethod
    def getAllAnswers():
        return ans_data.getAllAnswers()
    
    @staticmethod
    def updateAnswer(answer_info_array):
        return ans_data.updateAnswer(answer_info_array)