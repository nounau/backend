import traceback
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from src.modules.authentication.service.auth_service import auth_service
from src.modules.mailTemplates.routes.mailTemplate_routes import getMailTemplate
from src.modules.authentication.models.otp import otp
from src.modules.common.mailUtility import mailUtility
from werkzeug.security import generate_password_hash, check_password_hash
from src.modules.common.app_utils import app_utils
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime, timedelta, timezone
import random

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
    token = create_access_token(identity=user['_id'])
    return token

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = authenticate(email, password)
    print(user)
    if not user:
        return jsonify({'success': False, 'message': 'Invalid credentials', 'response':''}), 401
    if (user['otpVerified'] == False):
        return jsonify({'success': False, 'message': 'OTP verification required.', 'response':'', 'otpVerified': False}), 401

    access_token = create_token(user)
    return jsonify({'success': True, 'message': 'Login successful!', 'response':access_token}), 200

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
    _education = _json['education']
    _languages = _json['languages']
    _photo = _json['photo']
    _savedQuestions = _json['savedQuestions']
    _questionsAsked = _json['questionsAsked']
    _answersGiven = _json['answersGiven']
    _rewards = _json['rewards']
    _guestIpAddress = _json['guestIpAddress']
    _otpVerified = False
    _lastActiveTimeStamp = datetime.utcnow()

    register_info_array = [_uType, _userName, _password, _email, _name, _birthdate, _currentLocation, _city, _degree, 
                           _startDate, _endDate, _companyName, _workExperience, _interests, _education, _languages, _photo, 
                           _savedQuestions, _questionsAsked, _answersGiven, _rewards, _guestIpAddress, _otpVerified, _lastActiveTimeStamp]

    # try:
    if ifUserExists(_email):
        return jsonify({'success': False, 'message': 'User Already Exists', 'response': ''}), 200
    
    
    if _userName and _email and _password and request.method == "POST":

        # _hashed_password = generate_password_hash(_password)

        id = auth_service.register(register_info_array)
    
        OTP = random.randint(100000,999999);

        replacements = [];
        replacements.append({"target": "OTP", "value": str(OTP)})
        mailObj = getMailTemplate("NEW_USER", replacements)

        # mailObj.to = _email
        mailUtility.sendMail(mailObj, _email)

        #temp
        exp_Time = None
        # if(otp.get_otp(_email)):
        #     otp.updateStatus(_email, "INACTIVE")
        # else:
        otp.save_otp(_email, OTP, exp_Time, "ACTIVE")
        

        return jsonify({'success': True, 'message': 'User created successfully!', 'response': ''}), 200
    else:
        return not_found()
    
@auth_bp.route('/SendOTP', methods=['POST'])
def SendOTP():
    try:
        _email = request.json.get('email',None)
        OTP = random.randint(100000,999999);

        replacements = [];
        replacements.append({"target": "OTP", "value": str(OTP)})
        mailObj = getMailTemplate("RESET_PASSWORD", replacements)

        # mailObj.to = _email
        mailUtility.sendMail(mailObj, _email)

        #temp
        exp_Time = None
        # if(otp.get_otp(_email)):
        #     otp.updateStatus(_email, "INACTIVE")
        # else:
        otp.save_otp(_email, OTP, exp_Time, "ACTIVE")
        return jsonify({'success': True, 'message': 'Check the mail, OTP has been sent for paswword reset.', 'response': ''}), 200

    except Exception as ex:
        print(traceback.print_exception(type(ex), ex, ex.__traceback__))

@auth_bp.route('/resetPassword', methods=['POST'])
def resetPassword():
    try:
        email_of_OTP = request.json.get('email',None)
        _otp = request.json.get('otp',None)
        _newPassword = request.json.get('newPassword',None)
        
        if(otp.get_otp(email_of_OTP) == _otp):
            auth_service.resetPassword(email_of_OTP, _newPassword)
            # auth_service.updateOtpVerifiedFlag(email_of_OTP, True)
            return jsonify({'success': True, 'message': 'Password reset successful.', 'response': ''}), 200
        else:
            return jsonify({'success': False, 'message': 'OTP verification failed for reset password.', 'response': ''}), 401

    except Exception as ex:
        print(traceback.print_exception(type(ex), ex, ex.__traceback__))

@auth_bp.route('/verifyOTP', methods=['GET'])
def verifyOTP():
    email_of_OTP = request.json.get('email', None)
    if(otp.get_otp(email_of_OTP) == request.json.get('otp', None)):
        # otp.updateStatus(email_of_OTP, "INACTIVE")
        auth_service.updateOtpVerifiedFlag(email_of_OTP, True)
        return jsonify({'success': True, 'message': 'OTP verified!', 'response': ''}), 200
    else:
        return jsonify({'success': False, 'message': 'OTP verification failed!!', 'response': ''}), 401


@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    print(current_user)
    return jsonify({'message': f'Hello, {current_user}!'}), 200

@auth_bp.errorhandler(404)
def not_found(error=None):
    message = {
        'success':False,
        'message':'Not Found' + request.url,
        'response':''
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
