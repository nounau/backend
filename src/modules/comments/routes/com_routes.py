from json import dumps
from src.modules.comments.service.com_service import com_service
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime, timedelta, timezone
from bson import json_util
from flask_jwt_extended import get_jwt_identity, jwt_required

comment_bp = Blueprint('comment_bp', __name__)

@comment_bp.route('/postcomment', methods=['POST'])
@jwt_required()
def postComment():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    _json = request.json
    _userId = current_user
    _questionId = _json['questionId']
    _answerId = _json['answerId']
    _commentType = _json['commentType']
    _comment = _json['comment']
    _createdTimeStamp = datetime.utcnow()
    _updatedTimeStamp = datetime.utcnow()

    comment_info_array = [_userId, _questionId, _answerId, _commentType, _comment, _createdTimeStamp, _updatedTimeStamp]

    if _comment and request.method == "POST":

        id = com_service.postComment(comment_info_array)
        
        return jsonify({'success': True, 'message': 'Comment posted successfully!', 'response': ''}), 200
    else:
        return not_found()

@comment_bp.route('/getcomment', methods=['POST'])
@jwt_required()
def getComment():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    _commentId = _json['commentId']
    comment = com_service.getCommentById(_commentId, current_user)
    if comment:
        resp = json_util.dumps(comment)
        return jsonify({'success': True, 'message': 'Found comment', 'response': resp}), 200
        
    else:
        return not_found()

@comment_bp.route('/updatecomment', methods=['POST'])
@jwt_required()
def editComment():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    _commentId = _json['commentId']
    _userId = current_user
    _comment = _json['comment']
    _updatedTimeStamp = datetime.utcnow()

    comment_info_array = [_commentId, _userId, _comment, _updatedTimeStamp]

    if _comment and request.method == "POST":
        
        id = com_service.updateComment(comment_info_array)
        
        return jsonify({'ok': True, 'message': 'Comment updated successfully!', 'response': ''}), 200
    else:
        return not_found()

@comment_bp.route('/deletecomment', methods=['POST'])
@jwt_required()
def deleteComment():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    _commentId = _json['commentId']
    resp = com_service.deleteCommentById(_commentId, current_user)
    return jsonify({'success': True, 'message': 'Deleted comment', 'response': resp.acknowledged}), 200

@comment_bp.errorhandler(404)
def not_found(error=None):
    message = {
        'status':404,
        'message':'Not Found' + request.url
    }
    resp = jsonify(message)
 
    resp.status_code = 404
 
    return resp