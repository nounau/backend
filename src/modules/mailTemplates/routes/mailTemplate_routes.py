from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from src.modules.authentication.service.auth_service import auth_service
from src.modules.mailTemplates.models.mailTemplate_data import mailTemplate_data
from werkzeug.security import generate_password_hash, check_password_hash
from src.modules.common.app_utils import app_utils
from bson import json_util
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime, timedelta, timezone

# app = app_utils.get_app()
mt_bp = Blueprint('mt_bp', __name__)

def getMailTemplate(mail_type, replacements):
    try:
        template = mailTemplate_data.getMailTemplate(mail_type);
        print(type(template))
        print(template)

        # replacements = request.args.getlist('replacements[]')
        for replacement in replacements:
            print(replacement)
            template['description'] = template['description'].replace("{{" + replacement['target'] + "}}", replacement['value'])

        template['_id'] = str(template['_id'])
        return template;
        # return jsonify({'template': template}), 200
        # return jsonify({'template': template}), 200, {'Content-Type': 'application/json', 'indent': 2}

    except Exception as e:
        print(e)
        return jsonify({'message': 'Something went wrong', 'success': False}), 500

@mt_bp.route('/addMailTemplate', methods=['POST'])
def addMailTemplate():
    try:
        data = request.json
        template = {
            'mailType': data.get('mailType'),
            'subject': data.get('subject'),
            'description': data.get('description'),
        }

        template_id = mailTemplate_data.addMailTemplate(template);
        template['_id'] = str(template_id)

        return jsonify({'message': 'Template created successfully.', 'success': True, 'response': template}), 200

    except Exception as e:
        print(e)
        return jsonify({'message': 'Something went wrong', 'success': False}), 500

@mt_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    print(current_user)
    return jsonify({'message': f'Hello, {current_user}!'}), 200

@mt_bp.errorhandler(404)
def not_found(error=None):
    message = {
        'success':False,
        'message':'Not Found' + request.url,
        'response':''
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
