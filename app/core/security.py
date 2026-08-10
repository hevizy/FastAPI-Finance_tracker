import bcrypt

def get_password_hash(password: str):
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    hashed_string = hashed.decode('utf-8')
    return hashed_string

def check_password(password: str, hashed_password: str):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())
