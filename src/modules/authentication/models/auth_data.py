import traceback
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from dynaconf import settings
from bson import ObjectId

from src.modules.common.mongo_utils import mongo_utils

client = MongoClient(settings.MONGO_DB_URL)
db = client['Users'] # Change this!
users = db['user']

class auth_data:

    @staticmethod
    def authenticate(email, password):
        user = users.find_one({'email' : email})
        if user and check_password_hash(user['password'], password):
            # return {'userId': str(user['_id']), 'email': user['email']}
            user['_id'] = str(user['_id'])
            return user
        else:
            return None
    
    @staticmethod
    def register(ria):

        _uType = ria[0]
        _userName = ria[1]
        _password = generate_password_hash(ria[2])
        _email = ria[3]
        _name = ria[4]
        _birthdate = ria[5]
        _currentLocation = ria[6]
        _city = ria[7]
        _degree = ria[8]
        _startDate = ria[9]
        _endDate = ria[10]
        _companyName = ria[11]
        _workExperience = ria[12]
        _interests = ria[13]
        _education = ria[14]
        _languages = ria[15]
        _photo = ria[16]
        _savedQuestions = ria[17]
        _questionsAsked = ria[18]
        _answersGiven = ria[19]
        _rewards = ria[20]
        _guestIpAddress = ria[21]
        _otpVerified = ria[22]
        _lastActiveTimeStamp = ria[23]

        m = mongo_utils.get_mongo()
        mongo = m
        return mongo.db.user.insert_one({'uType':_uType, 'userName':_userName, 'password':_password, 'email':_email, 'name':_name,
                                       'birthdate':_birthdate, 'currentLocation':_currentLocation, 'city':_city, 'degree':_degree, 'startDate':_startDate, 'endDate':_endDate,
                                       'companyName':_companyName, 'workExperience':_workExperience, 'interests':_interests, 'education':_education, 'languages':_languages,
                                        'photo':_photo, 'savedQuestions':_savedQuestions, 'questionsAsked':_questionsAsked, 'answersGiven':_answersGiven, 
                                        'rewards':_rewards, 'guestIpAddress':_guestIpAddress, 'otpVerified':_otpVerified, 'lastActiveTimeStamp':_lastActiveTimeStamp})

    @staticmethod
    def ifUserExists(email):
        try:
            if len(users.find_one({'email': email})) > 0:
                return True
            else:
                return False
        except TypeError:
            print("No user Found!")
            return False
        
    @staticmethod
    def resetPassword(email_of_OTP, _newPassword):
        try:
            user = users.find_one({'email': email_of_OTP})
            _id = str(user['_id'])
            return mongo_utils.get_mongo().db.user.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, 
                                      {'$set': {'password':_newPassword}})

        except Exception as ex:
            traceback.print_exception(type(ex), ex, ex.__traceback__)
