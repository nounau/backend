from json import dumps
from src.modules.questions.service.q_service import q_service
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime, timedelta, timezone
from bson import json_util

question_bp = Blueprint('question_bp', __name__)

@question_bp.route('/postquestion', methods=['POST'])
def postQuestion():
    _json = request.json
    _title = _json['title']
    _uId = _json['uId']
    _savedBy = _json['savedBy']
    _noOfReposts = _json['noOfReposts']
    _isRealTime = _json['isRealTime']
    _createdTimeStamp = datetime.utcnow()
    _updatedTimeStamp = datetime.utcnow()
    _tags = _json['tags']
    _views = _json['views']

    question_info_array = [_title, _uId, _savedBy, _noOfReposts, _isRealTime, _createdTimeStamp, _updatedTimeStamp, _tags, _views]

    if _title and request.method == "POST":

        id = q_service.postQuestion(question_info_array)
        # id = mongo.db.questions.insert_one({'title':_title, 'uId':_uId, 'noOfReposts':_noOfReposts, 'isRealTime':_isRealTime, 
        #                            'createdTimeStamp':_createdTimeStamp, 'updatedTimeStamp':_updatedTimeStamp, 'tags':_tags})
        
        return jsonify({'ok': True, 'message': 'Question created successfully!'}), 200
    else:
        return not_found()
    
@question_bp.route('/getquestion/<id>', methods=['GET'])
def getQuestion(id):
    question = q_service.getQuestionById(id)
    if question:
        resp = json_util.dumps(question)
        #json.loads(json_util.dumps(data))
        return resp
    else:
        return not_found()
    
@question_bp.route('/updatequestion/<id>', methods=['PUT'])
def editQuestion(id):
    _id = id
    _json = request.json
    _title = _json['title']
    _uId = _json['uId']
    _savedBy = _json['savedBy']
    _noOfReposts = _json['noOfReposts']
    _isRealTime = _json['isRealTime']
    _createdTimeStamp = datetime.utcnow()
    _updatedTimeStamp = datetime.utcnow()
    _tags = _json['tags']
    _views = _json['views']

    question_info_array = [_id, _title, _uId, _savedBy, _noOfReposts, _isRealTime, _createdTimeStamp, _updatedTimeStamp, _tags, _views]


    if _title and request.method == "POST":
        
        id = q_service.updateQuestion(question_info_array)
        # id = mongo.db.questions.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, 
        #                               {'$set': {'title':_title, 'noOfReposts':_noOfReposts, 
        #                                     'isRealTime':_isRealTime, 'updatedTimeStamp':_updatedTimeStamp, 'tags':_tags}})
        
        return jsonify({'ok': True, 'message': 'User updated successfully!'}), 200
    else:
        return not_found()

@question_bp.errorhandler(404)
def not_found(error=None):
    message = {
        'status':404,
        'message':'Not Found' + request.url
    }
    resp = jsonify(message)
 
    resp.status_code = 404
 
    return resp