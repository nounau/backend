# from src import create_app
import os
from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
load_dotenv('.flaskenv') #the path to your .env file (or any other file of environment variables you want to load)
print("test 16", os.environ.get('MONGO_DB_URL'))
app.config.from_object(Config)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!

from src.main import bp as main_bp
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run()
