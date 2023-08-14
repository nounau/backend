from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from src.modules.authentication.service.auth_service import auth_service
from werkzeug.security import generate_password_hash, check_password_hash
from src.modules.common.app_utils import app_utils
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime, timedelta, timezone

# app = app_utils.get_app()
auth_bp = Blueprint('auth_bp', __name__)
 
def authenticate(email, password):
    return auth_service.authenticate(email, password);

def ifUserExists(email):
    return auth_service.ifUserExists(email)
    
def create_token(user):
    # token = jwt.encode({
    #         'user_email': user['email'],
    #         'exp' : datetime.utcnow() + timedelta(minutes = 30)
    #     }, app.config['SECRET_KEY'])
    token = create_access_token(identity=user['email'])
    return token

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = authenticate(email, password)

    if not user:
        return jsonify({'ok': False, 'message': 'Invalid credentials', 'response':''}), 401

    access_token = create_token(user)
    return jsonify({'ok': True, 'message': 'Login successful!', 'response':access_token}), 200

@auth_bp.route('/register', methods=['POST'])
def register():

    _json = request.json
    _uType = _json['uType']
    _userName = _json['userName']
    _password = _json['password']
    _email = _json['email']
    _name = _json['name']
    _birthdate = _json['birthdate']
    _currentLocation = _json['currentLocation']
    _city = _json['city']
    _degree = _json['degree']
    _startDate = _json['startDate']
    _endDate = _json['endDate']
    _companyName = _json['companyName']
    _workExperience = _json['workExperience']
    _interests = _json['interests']
    _languages = _json['languages']
    _photo = _json['photo']
    _savedQuestions = _json['savedQuestions']
    _questionsAsked = _json['questionsAsked']
    _answersGiven = _json['answersGiven']
    _rewards = _json['rewards']
    _guestIpAddress = _json['guestIpAddress']
    _lastActiveTimeStamp = datetime.utcnow()

    register_info_array = [_uType, _userName, _password, _email, _name, _birthdate, _currentLocation, _city, _degree, 
                           _startDate, _endDate, _companyName, _workExperience, _interests, _languages, _photo, 
                           _savedQuestions, _questionsAsked, _answersGiven, _rewards, _guestIpAddress, _lastActiveTimeStamp]

    if ifUserExists(_email):
        return jsonify({'ok': False, 'message': 'User Already Exists', 'response': ''}), 200
    
    if _userName and _email and _password and request.method == "POST":

        # _hashed_password = generate_password_hash(_password)

        id = auth_service.register(register_info_array)
        # id = mongo.db.user.insert_one({'uType':_uType, 'userName':_userName, 'password':_hashed_password, 'email':_email, 'name':_name,
        #                                'birthdate':_birthdate, 'currentLocation':_currentLocation, 'city':_city, 'degree':_degree, 'startDate':_startDate, 'endDate':_endDate,
        #                                'companyName':_companyName, 'workExperience':_workExperience, 'photo':_photo, 'guestIpAddress':_guestIpAddress, 'lastActiveTimeStamp':_lastActiveTimeStamp})

        return jsonify({'ok': True, 'message': 'User created successfully!', 'response': ''}), 200
    else:
        return not_found()

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({'message': f'Hello, {current_user}!'}), 200

@auth_bp.errorhandler(404)
def not_found(error=None):
    message = {
        'ok':False,
        'message':'Not Found' + request.url,
        'response':''
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
