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
    print("In post Answer: "+current_user)

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

@answer_bp.route('/getanswer/<id>', methods=['GET'])
@jwt_required()
def getAnswer(id):
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    ans = ans_service.getAnswerById(id)
    if ans:
        resp = json_util.dumps(ans)
        #json.loads(json_util.dumps(data))
        return resp
    else:
        return not_found()

@answer_bp.route('/updateanswer/<id>', methods=['PUT'])
@jwt_required()
def editAnswer(id):
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _id = id
    _json = request.json
    _questionId = _json['questionId']
    _answer = _json['answer']
    _userId = current_user
    _likes = _json['likes']
    _comments = _json['comments']
    _createdTimeStamp = datetime.utcnow()
    _updatedTimeStamp = datetime.utcnow()
    _isQualifiedRealTime = _json['isQualifiedRealTime']

    answer_info_array = [_id, _questionId, _answer, _userId, _likes, _comments, _createdTimeStamp, _updatedTimeStamp, _isQualifiedRealTime]

    if _questionId and _answer and request.method == "POST":

        id = ans_service.updateAnswer(answer_info_array)
        # id = mongo.db.questions.insert_one({'title':_title, 'uId':_uId, 'noOfReposts':_noOfReposts, 'isRealTime':_isRealTime, 
        #                            'createdTimeStamp':_createdTimeStamp, 'updatedTimeStamp':_updatedTimeStamp, 'tags':_tags})
        
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