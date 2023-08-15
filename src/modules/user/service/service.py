from pymongo import MongoClient
from dynaconf import settings

from src.modules.user.models.data import Data

class Service:

    @staticmethod
    def get_all_data():
        return Data.get_all_data()
    
    @staticmethod
    def questionsSaved(current_user, questionId):
        return Data.questionsSaved(current_user, questionId)
