from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from dynaconf import settings

from src.modules.common.mongo_utils import mongo_utils

client = MongoClient(settings.MONGO_DB_URL)
db = client['Users'] # Change this!
mail_templates = db['mail_templates']

class mailTemplate_data:

    @staticmethod
    def addMailTemplate(template):
        return mongo_utils.get_mongo().db.mail_templates.insert_one(template).inserted_id;
    
    @staticmethod
    def getMailTemplate(mail_type):
        return mongo_utils.get_mongo().db.mail_templates.find_one({'mailType': mail_type});

