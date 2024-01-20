import traceback
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from dynaconf import settings

from src.modules.common.mongo_utils import mongo_utils

client = MongoClient(settings.MONGO_DB_URL)
db = client['Users'] # Change this!
otpColl = db['otp']

class otp:

    @staticmethod
    def save_otp(email, OTP, exp_Time, status):
        # otpObj = otp.find_one({'email': email})

        return otpColl.update_one({'email':email}, {'$set': {'otp': OTP, 'expTime': exp_Time, 'status': status}})
        # return otpColl.insert_one({'email': email, 'otp': OTP, 'expTime': exp_Time, 'status': status});


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
        
    @staticmethod
    def updateFlag(email, status):
        try:
            return otpColl.update_one({'email':email}, {'$set': {'status': status}})
        except Exception as ex:
            traceback.print_exception(type(ex), ex, ex.__traceback__)
