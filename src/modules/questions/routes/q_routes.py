from json import dumps
from src.modules.questions.service.q_service import q_service
from src.modules.user.service.service import Service
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime, timedelta, timezone
from bson import json_util
from flask_jwt_extended import get_jwt_identity, jwt_required

question_bp = Blueprint('question_bp', __name__)

@question_bp.route('/postquestion', methods=['POST'])
@jwt_required()
def postQuestion():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    print(current_user)
    
    _json = request.json
    _title = _json['title']
    _description = _json['description']
    _userId = current_user
    _savedBy = _json['savedBy']
    _noOfReposts = _json['noOfReposts']
    _isRealTime = _json['isRealTime']
    _createdTimeStamp = datetime.utcnow()
    _updatedTimeStamp = datetime.utcnow()
    _tags = _json['tags']
    _views = _json['views']

    question_info_array = [_title, _description, _userId, _savedBy, _noOfReposts, _isRealTime, _createdTimeStamp, _updatedTimeStamp, _tags, _views]

    if _title and request.method == "POST":

        id = q_service.postQuestion(question_info_array)
        
        return jsonify({'success': True, 'message': 'Question created successfully!', 'response': ''}), 200
    else:
        return not_found()
    
@question_bp.route('/getquestion', methods=['POST'])
@jwt_required()
def getQuestion():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    id = _json['questionId']
    question = q_service.getQuestionById(id, current_user)
    if question:
        resp = json_util.dumps(question)
        parsed_resp = json_util.loads(resp)
        return jsonify({'success': True, 'message': 'Found Question', 'response': parsed_resp}), 200, {'Content-Type': 'application/json', 'indent': 2}

    else:
        return not_found()
    
@question_bp.route('/updatequestion', methods=['POST'])
@jwt_required()
def editQuestion():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    _json = request.json
    _id = _json['questionId']
    _title = _json['title']
    _description = _json['description']
    _userId = current_user
    _savedBy = _json['savedBy']
    _noOfReposts = _json['noOfReposts']
    _isRealTime = _json['isRealTime']
    _updatedTimeStamp = datetime.utcnow()
    _tags = _json['tags']
    _views = _json['views']

    question_info_array = [_id, _title, _description, _userId, _savedBy, _noOfReposts, _isRealTime, _updatedTimeStamp, _tags, _views]


    if _title and request.method == "POST":
        
        id = q_service.updateQuestion(question_info_array)
        print("Question Id : "+id)
        
        return jsonify({'success': True, 'message': 'Question updated successfully!', 'response': ''}), 200
    else:
        return not_found()
    
@question_bp.route('/savedby', methods=['POST'])
@jwt_required()
def savedBy():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    _json = request.json
    questionId = _json['questionId']

    if current_user and questionId and request.method == "POST":
        questionSavedBy = q_service.savedBy(current_user, questionId)
        userQuestionsSaved = Service.questionsSaved(current_user, questionId)
        # result = questionSavedBy + userQuestionsSaved
        return jsonify({'success': True, 'message': userQuestionsSaved, 'response': ''}), 200
    else:
        return not_found()
    

@question_bp.errorhandler(404)
def not_found(error=None):
    message = {
        'success':False,
        'message':'Not Found' + request.url,
        'response':''
    }
    resp = jsonify(message)
 
    resp.status_code = 404
 
    return resp