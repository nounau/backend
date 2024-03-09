# # Inside app/__init__.py

# from flask import Flask
# from flask_jwt_extended import JWTManager
# from config import Config

# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(config_class)

#     app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!

#     # Register blueprints here

#     # from src.main import bp as main_bp
#     # app.register_blueprint(main_bp)



#     return app
