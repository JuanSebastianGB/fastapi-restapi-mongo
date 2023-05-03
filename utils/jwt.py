from datetime import timedelta, datetime
from jose import jwt


SECRET_KEY = "smlnfjkdskgjkdngkjdgd5sdf5dsf15s"
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data[::]
    expire = datetime.utcnow() + expires_delta if expires_delta else datetime.utcnow() + \
        timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
