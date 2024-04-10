import jwt
from todo.config import settings


def encode_jwt(payload: dict, private_key: str = settings.auth_jwt.private_key_path.read_text(), algorithm: str = settings.auth_jwt.algorithm):
    encoded = jwt.encode(payload, private_key, algorithm=algorithm)
    return encoded


def decode_jwt(jwt_token: str | bytes, public_key: str = settings.auth_jwt.public_key_path.read_text(), algorithm: str = settings.auth_jwt.algorithm):
    decoded = jwt.decode(jwt_token, public_key, algorithm=[algorithm])
    return decoded
