from json import dumps
from src.modules.subscription.service.sb_service import sb_service
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime, timedelta, timezone
from bson import json_util
from flask_jwt_extended import get_jwt_identity, jwt_required

subscribe_bp = Blueprint('subscribe_bp', __name__)

@subscribe_bp.route('/postsubscription', methods=['POST'])
@jwt_required()
def postSubscription():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    _userId = current_user
    _purchaseDate =_json['purchaseDate'], 
    _endDate = _json['endDate'], 
    _purchaseAmount = _json['purchaseAmount'], 
    _modeOfpayment = _json['modeOfpayment']

    subscription_info_array = [_userId, _purchaseDate, _endDate, _purchaseAmount, _modeOfpayment]

    if _userId and request.method == "POST":

        id = sb_service.postSubscription(subscription_info_array)
        
        return jsonify({'success': True, 'message': 'Subscription created successfully!', 'response': ''}), 200
    else:
        return not_found()
    
@subscribe_bp.route('/getsubscription', methods=['POST'])
@jwt_required()
def getSubscription():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    subscriptionId = _json['subscriptionId']
    sub = sb_service.getSubscriptionById(subscriptionId, current_user)
    if sub:
        resp = json_util.dumps(sub)
        return jsonify({'success': True, 'message': 'Found Subscription', 'response': resp}), 200
    else:
        return not_found()
    
@subscribe_bp.route('/getallrewards', methods=['POST'])
@jwt_required()
def getAllSubscriptions():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    subs = sb_service.getAllSubscriptions()
    if subs:
        resp = json_util.dumps(subs)
        return jsonify({'success': True, 'message': 'Found all Rewards', 'response': resp}), 200
    else:
        return not_found()

@subscribe_bp.route('/updatesubscription', methods=['POST'])
@jwt_required()
def updateSubscription():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    _subscriptionId = _json['subscriptionId']
    _userId = current_user
    _purchaseDate =_json['purchaseDate'], 
    _endDate = _json['endDate'], 
    _purchaseAmount = _json['purchaseAmount'], 
    _modeOfpayment = _json['modeOfpayment']

    subscription_info_array = [_subscriptionId, _userId, _purchaseDate, _endDate, _purchaseAmount, _modeOfpayment]

    if _subscriptionId and request.method == "POST":
        
        id = sb_service.updateSubscription(subscription_info_array)
        print("Subscription Id : "+id)
        
        return jsonify({'success': True, 'message': 'Subscription updated successfully!', 'response': ''}), 200
    else:
        return not_found()

@subscribe_bp.route('/deletesubscription', methods=['POST'])
@jwt_required()
def deleteSubscription():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'success': False, 'message': 'UnAutorized Access', 'response': ''}), 401
    
    _json = request.json
    _subscriptionId = _json['subscriptionId']
    resp = sb_service.deleteSubscriptionById(_subscriptionId, current_user)
    return jsonify({'success': True, 'message': 'Deleted Subscription', 'response': resp.acknowledged}), 200

    
@subscribe_bp.errorhandler(404)
def not_found(error=None):
    message = {
        'success':False,
        'message':'Not Found' + request.url,
        'response':''
    }
    resp = jsonify(message)
 
    resp.status_code = 404
 
    return resp

