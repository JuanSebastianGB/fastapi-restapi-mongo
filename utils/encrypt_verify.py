from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(hash: str, password: str) -> bool:
    return pwd_context.verify(password, hash)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
