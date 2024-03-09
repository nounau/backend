from datetime import datetime
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.modules.follow.service.f_service import f_service
from bson import json_util

follow_bp = Blueprint('follow_bp', __name__)

@follow_bp.route('/postfollow', methods=['POST'])
@jwt_required()
def postFollow():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    _userId = _json['userId'],
    _followingId = current_user

    follow_info_array = [_userId, _followingId]

    if _userId and request.method == "POST":

        id = f_service.postFollow(follow_info_array)
        
        return jsonify({'success': True, 'message': 'Follow created successfully!', 'response': ''}), 200
    else:
        return not_found()
    
@follow_bp.route('/getfollow', methods=['POST'])
@jwt_required()
def getFollow():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    id = _json['followId']
    follow = f_service.getRewardById(id, current_user)
    if follow:
        resp = json_util.dumps(follow)
        return jsonify({'success': True, 'message': 'Found Follow', 'response': resp}), 200
    else:
        return not_found()
    
@follow_bp.route('/getallfollows', methods=['POST'])
@jwt_required()
def getAllFollows():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    follows = f_service.getAllRewards()
    if follows:
        resp = json_util.dumps(follows)
        return jsonify({'success': True, 'message': 'Found all follows', 'response': resp}), 200
    else:
        return not_found()
    
@follow_bp.errorhandler(404)
def not_found(error=None):
    message = {
        'success':False,
        'message':'Not Found' + request.url,
        'response':''
    }
    resp = jsonify(message)

    resp.status_code = 404

    return resp