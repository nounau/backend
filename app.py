from flask import Flask
from src.modules.common.app_utils import app_utils
from src.modules.common.mongo_utils import mongo_utils
from src.modules.common.jwt_utils import auth_utils
from src.modules.user.routes.routes import data_bp
from src.modules.authentication.routes.auth_routes import auth_bp
from src.modules.questions.routes.q_routes import question_bp
from src.modules.answers.routes.ans_routes import answer_bp
from src.modules.comments.routes.com_routes import comment_bp
from src.modules.rewards.routes.rw_routes import rewards_bp
from src.modules.subscription.routes.sb_routes import subscribe_bp
from src.modules.follow.routes.f_routes import follow_bp
from dynaconf import Dynaconf, settings
import json
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from flask_bcrypt import Bcrypt
from pymongo import MongoClient

app = Flask(__name__)
app.register_blueprint(data_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(question_bp)
app.register_blueprint(answer_bp)
app.register_blueprint(comment_bp)
app.register_blueprint(rewards_bp)
app.register_blueprint(subscribe_bp)
app.register_blueprint(follow_bp)
app.secret_key = "secretkey"


app.config['MONGO_URI'] = settings.MONGO_DB_URL
app.config["JWT_SECRET_KEY"] = "rohannitiket"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)

app_utils.set_app(app)
auth_utils.set_auth_objects(Bcrypt(app), JWTManager(app))
mongo_utils.set_mongo(PyMongo(app))

settings = Dynaconf(
    settings_files=["settings.toml"],  # List of configuration files to load
)
if __name__ == '__main__':
    app.run(debug=True)
