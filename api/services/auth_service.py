from models.antravision_model import SignUp

def authenticate_user(username, password):
    user = SignUp.find_by_username(username)
    if user and user.verify_password(password):
        return user
    return None
