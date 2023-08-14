from flask import Blueprint, jsonify, request
from src.modules.rewards.service.rw_service import Service

rewards_bp = Blueprint('rewards_bp', __name__)

@rewards_bp.route('/api/data', methods=['GET'])
def getRewards():
    return None

@rewards_bp.route('/api/data', methods=['POST'])
def addReward():
    new_data = request.get_json()
    return jsonify({'message': 'Data added successfully!'})