from passlib.context import CryptContext

def hash(password):
    pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
    return pwd_context.hash(password)