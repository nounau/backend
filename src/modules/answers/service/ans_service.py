from src.modules.answers.models.ans_data import ans_data

class ans_service:

    @staticmethod
    def postAnswer(answer_info_array):
        return ans_data.postAnswer(answer_info_array)
    
    @staticmethod
    def getAnswerById(id):
        return ans_data.getAnswerById(id)
    
    @staticmethod
    def updateAnswer(answer_info_array):
        return ans_data.updateAnswer(answer_info_array)