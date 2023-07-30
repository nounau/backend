from json import dumps
from src.modules.comments.service.com_service import com_service
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime, timedelta, timezone
from bson import json_util

comment_bp = Blueprint('comment_bp', __name__)

@comment_bp.route('/postcomment', methods=['POST'])
def postComment():
    _json = request.json
    _uId = _json['uId']
    _questionId = _json['questionId']
    _answerId = _json['answerId']
    _commentType = _json['commentType']
    _comment = _json['comment']
    _createdTimeStamp = datetime.utcnow()
    _updatedTimeStamp = datetime.utcnow()

    comment_info_array = [_uId, _questionId, _answerId, _commentType, _comment, _createdTimeStamp, _updatedTimeStamp]

    if _comment and request.method == "POST":

        id = com_service.postComment(comment_info_array)
        
        return jsonify({'ok': True, 'message': 'Comment posted successfully!'}), 200
    else:
        return not_found()

@comment_bp.route('/getcomment/<id>', methods=['GET'])
def getComment(id):
    comment = com_service.getCommentById(id)
    if comment:
        resp = json_util.dumps(comment)
        #json.loads(json_util.dumps(data))
        return resp
    else:
        return not_found()

@comment_bp.route('/editcomment/<id>', methods=['PUT'])
def editComment(id):
    _id = id
    _json = request.json
    _uId = _json['uId']
    _questionId = _json['questionId']
    _answerId = _json['answerId']
    _commentType = _json['commentType']
    _comment = _json['comment']
    _createdTimeStamp = datetime.utcnow()
    _updatedTimeStamp = datetime.utcnow()

    comment_info_array = [_id, _uId, _questionId, _answerId, _commentType, _comment, _createdTimeStamp, _updatedTimeStamp]

    if _comment and request.method == "POST":
        
        id = com_service.updateComment(comment_info_array)
        
        return jsonify({'ok': True, 'message': 'Comment updated successfully!'}), 200
    else:
        return not_found()

@comment_bp.route('/deletecomment/<id>', methods=['DELETE'])
def deleteComment(id):
    return com_service.deleteCommentById(id)

@comment_bp.errorhandler(404)
def not_found(error=None):
    message = {
        'status':404,
        'message':'Not Found' + request.url
    }
    resp = jsonify(message)
 
    resp.status_code = 404
 
    return resp