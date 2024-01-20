from src.modules.authentication.models.auth_data import auth_data

class auth_service:

    @staticmethod
    def authenticate(email, password):
        return auth_data.authenticate(email, password)
    
    @staticmethod
    def register(register_info_array):
        return auth_data.register(register_info_array)
    
    @staticmethod
    def ifUserExists(email):
        return auth_data.ifUserExists(email)
    
    @staticmethod
    def resetPassword(email_of_OTP, _newPassword):
        return auth_data.resetPassword(email_of_OTP, _newPassword)
    
    @staticmethod
    def updateOtpVerifiedFlag(email_of_OTP, otpVerified):
        auth_data.updateOtpVerifiedFlag(email_of_OTP, otpVerified)