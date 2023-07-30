from flask_bcrypt import Bcrypt

class auth_utils:

    flask_bcrypt = None
    jwt = None

    @staticmethod
    def set_auth_objects(flask_bcrypt, jwt):
        auth_utils.flask_bcrypt =flask_bcrypt
        auth_utils.jwt = jwt
