from flask import Blueprint, jsonify, request
from src.modules.user.service.service import Service
from src.modules.user.models.data import Data

data_bp = Blueprint('data_bp', __name__)

@data_bp.route('/users', methods=['GET'])
def get_data():
    data = Service.get_all_data()
    print(data)
    # return jsonify(data)

@data_bp.route('/addusers', methods=['POST'])
def add_data():
    new_data = request.get_json()
    Data.add_data(new_data)
    return jsonify({'message': 'Data added successfully!'})
