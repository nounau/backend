from json import dumps
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime, timedelta, timezone
from src.modules.answers.service.ans_service import ans_service
from bson import json_util
from flask_jwt_extended import get_jwt_identity, jwt_required

answer_bp = Blueprint('answer_bp', __name__)

@answer_bp.route('/postanswer', methods=['POST'])
@jwt_required()
def postAnswer():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401

    _json = request.json
    _questionId = _json['questionId']
    _answer = _json['answer']
    _userId = current_user
    _likes = 0
    _comments = []
    _createdTimeStamp = datetime.utcnow()
    _updatedTimeStamp = datetime.utcnow()
    _isQualifiedRealTime = _json['isQualifiedRealTime']

    answer_info_array = [_questionId, _answer, _userId, _likes, _comments, _createdTimeStamp, _updatedTimeStamp, _isQualifiedRealTime]

    if _questionId and _answer and request.method == "POST":

        id = ans_service.postAnswer(answer_info_array)
        
        return jsonify({'success': True, 'message': 'Answer posted successfully', 'response': ''}), 200
    else:
        return not_found()
    
@answer_bp.route('/updatelike', methods=['POST'])
@jwt_required()
def updatelike():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    _answerId = _json['answerId']
    _isLiked = _json['isLiked']
    if _isLiked and request.method == "POST":
        result = ans_service.updatelike(_answerId, _isLiked)
        return jsonify({'success': True, 'message': 'Like Updated Successfully', 'response': result}), 200
    else:
        return not_found()    

@answer_bp.route('/getanswer', methods=['POST'])
@jwt_required()
def getAnswer():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    _answerId = _json['answerId']
    if _answerId and request.method == "POST":
        ans = ans_service.getAnswerById(_answerId)
        if ans:
            resp = json_util.dumps(ans)
            return jsonify({'success': True, 'message': 'Answer Found', 'response': resp}), 200
        return ans
    else:
        return not_found()
    
@answer_bp.route('/getallanswers', methods=['POST'])
@jwt_required()
def getAllAnswers():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    if request.method == "POST":
        ans = ans_service.getAllAnswers()
        if ans:
            resp = json_util.dumps(ans)
            return jsonify({'success': True, 'message': 'All answers Found', 'response': resp}), 200
    else:
        return not_found()

@answer_bp.route('/updateanswer', methods=['POST'])
@jwt_required()
def editAnswer():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    _answerId = _json['answerId']
    _answer = _json['answer']
    _userId = current_user
    _updatedTimeStamp = datetime.utcnow()
    _isQualifiedRealTime = _json['isQualifiedRealTime']

    answer_info_array = [_answerId, _answer, _userId, _updatedTimeStamp, _isQualifiedRealTime]

    if _answerId and _answer and request.method == "POST":

        id = ans_service.updateAnswer(answer_info_array)
        print(id.upserted_id)
        
        return jsonify({'ok': True, 'message': 'Answer updated successfully!', 'response': ''}), 200
    else:
        return not_found()

@answer_bp.errorhandler(404)
def not_found(error=None):
    message = {
        'status':404,
        'message':'Not Found' + request.url
    }
    resp = jsonify(message)
 
    resp.status_code = 404
 
    return resp