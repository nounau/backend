from pymongo import MongoClient
from dynaconf import settings

from app.modules.user.models.data import Data

class Service:

    @staticmethod
    def get_all_data():
        return Data.get_all_data();
