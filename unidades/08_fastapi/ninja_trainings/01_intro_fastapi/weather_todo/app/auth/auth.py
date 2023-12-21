from datetime import datetime, timedelta

from pydantic import BaseModel
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from app.db.schemas import User


# Con este código ciframos, para enviar el token cifrado.
# Crea un código seguro con el comando: openssl rand -hex 32
SECRET_KEY = "12ab2624a67ebe61b859dd6e6937d96c553f1806393d3fb024660bce875a1dcd"
# Podemos cifrar usando varios algoritmos: en este caso HS256.
ALGORITH = "HS256"

# Por seguridad vamos a usar un tiempo de expiración del token que mandamos.
# Pasado este tiempo en minutos el token lo consideraremos caducado.
ACCESS_TOKEN_EXPIRE_MIN = 60

# Usamos la librería de python passlib para cifrar la contraseña.
# Aquí creamos un objeto indicando el algoritmo criptográfico que vamos a usar: bcrypt.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Vamos a usar un Token de tipo Bearer.
# Indicamos, además, la URL desde la cual obtener el token.
oauth2_scheme =  OAuth2PasswordBearer(tokenUrl="/auth/login")


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(user: User) -> Token:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MIN)

    to_encode = {
        "sub": user.username,
        "exp": expire
    }

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITH)

    return Token(access_token=encoded_jwt, token_type="bearer")


def decode_token(token: str) -> TokenData:
    try:
        payload: dict = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return TokenData(username=payload.get("sub"))
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )