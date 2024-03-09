from datetime import datetime
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.modules.rewards.service.rw_service import rw_service
from bson import json_util

rewards_bp = Blueprint('rewards_bp', __name__)

@rewards_bp.route('/postreward', methods=['POST'])
@jwt_required()
def postReward():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    _userId = current_user
    _couponName = _json['couponName']
    _amount = _json['amount']
    _pointsRedeemed = _json['pointsRedeemed']
    _rewardTimeStamp = datetime.utcnow()
    _expiryTimeStamp = _json['expiryTimeStamp']

    reward_info_array = [_userId, _couponName, _amount, _pointsRedeemed, _rewardTimeStamp, _expiryTimeStamp]

    if _userId and request.method == "POST":

        id = rw_service.postReward(reward_info_array)
        
        return jsonify({'success': True, 'message': 'Reward created successfully!', 'response': ''}), 200
    else:
        return not_found()

@rewards_bp.route('/getreward', methods=['POST'])
@jwt_required()
def getReward():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    id = _json['rewardId']
    reward = rw_service.getRewardById(id, current_user)
    if reward:
        resp = json_util.dumps(reward)
        return jsonify({'success': True, 'message': 'Found Reward', 'response': resp}), 200
    else:
        return not_found()
    
@rewards_bp.route('/getallrewards', methods=['POST'])
@jwt_required()
def getAllRewards():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    rewards = rw_service.getAllRewards()
    if rewards:
        resp = json_util.dumps(rewards)
        return jsonify({'success': True, 'message': 'Found all Rewards', 'response': resp}), 200
    else:
        return not_found()

@rewards_bp.route('/updatereward', methods=['POST'])
@jwt_required()
def updateReward():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    _rewardId = _json['rewardId']
    _userId = current_user
    _couponName = _json['couponName']
    _amount = _json['amount']
    _pointsRedeemed = _json['pointsRedeemed']
    _rewardTimeStamp = datetime.utcnow()
    _expiryTimeStamp = _json['expiryTimeStamp']

    reward_info_array = [_rewardId, _userId, _couponName, _amount, _pointsRedeemed, _rewardTimeStamp, _expiryTimeStamp]

    if _userId and request.method == "POST":
        
        id = rw_service.updateReward(reward_info_array)
        print("Reward Id : "+id)
        
        return jsonify({'success': True, 'message': 'Reward updated successfully!', 'response': ''}), 200
    else:
        return not_found()

@rewards_bp.route('/deletereward', methods=['POST'])
@jwt_required()
def deleteReward():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    _rewardId = _json['rewardId']
    resp = rw_service.deleteRewardById(_rewardId, current_user)
    return jsonify({'success': True, 'message': 'Deleted comment', 'response': resp.acknowledged}), 200

@rewards_bp.errorhandler(404)
def not_found(error=None):
    message = {
        'success':False,
        'message':'Not Found' + request.url,
        'response':''
    }
    resp = jsonify(message)
 
    resp.status_code = 404
 
    return resp