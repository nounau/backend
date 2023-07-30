from src.modules.questions.models.q_data import q_data

class q_service:

    @staticmethod
    def postQuestion(question_info_array):
        return q_data.postQuestion(question_info_array)
    
    @staticmethod
    def getQuestionById(id):
        return q_data.getQuestionById(id)
    
    @staticmethod
    def updateQuestion(question_info_array):
        return q_data.updateQuestion(question_info_array)