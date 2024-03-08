# from src import create_app
from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
load_dotenv('.flaskenv') #the path to your .env file (or any other file of environment variables you want to load)

@app.route('/')
def index():
    return 'This is The Main Blueprint'

if __name__ == "__main__":
    app.run()
