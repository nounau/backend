from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from dynaconf import settings

from src.modules.common.mongo_utils import mongo_utils

client = MongoClient(settings.MONGO_DB_URL)
db = client['Users'] # Change this!
otpColl = db['otp']

class otp:

    @staticmethod
    def save_otp(email, OTP, exp_Time):
        # otpObj = otp.find_one({'email': email})

        # return mongo_utils.get_mongo().otp.update({'email': email}, {'otp': OTP}, upsert=True);
        return otpColl.insert_one({'email': email, 'otp': OTP, 'expTime': exp_Time});


    @staticmethod
    def get_otp(email):
        try:
            otpObj = otpColl.find_one({'email': email})
            if otpObj:
                return otpObj.get('otp')
            else:
                return None
        except TypeError:
            print("No OTP Found!")
            return False
