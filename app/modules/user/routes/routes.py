from flask import Blueprint, jsonify, request
from app.modules.user.service.service import Service
from app.modules.user.models.data import Data

data_bp = Blueprint('data_bp', __name__)

@data_bp.route('/api/data', methods=['GET'])
def get_data():
    data = Service.get_all_data()
    return jsonify(data)

@data_bp.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.get_json()
    Data.add_data(new_data)
    return jsonify({'message': 'Data added successfully!'})
