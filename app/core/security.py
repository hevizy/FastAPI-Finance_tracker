import bcrypt

def get_password_hash(password: str):
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed

def check_password(password: str, hashed_password: str):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())
