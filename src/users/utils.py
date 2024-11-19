from passlib.context import CryptContext
from datetime import timedelta
from jwt import encode
from src.config import Config

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_password_hash(password):
    return password_context.hash(password)


def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)


def create_access_token(userdata, expires_in=3600):
    token = encode(
        payload=userdata,
        key=Config.JWT_SECRET_KEY,
        algorithm=Config.JWT_ALGORITHM,
        expires_in=expires_in
    )
    return token
