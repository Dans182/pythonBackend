from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256" #Seleccion de algoritmo de encriptación
ACCESS_TOKEN_DURATION = 1
#En terminal, de esta manera genero un secret openssl rand -hex 32
SECRET = "bb8733a5834619c1b98b91ee5cc317b646a6937cee2decec006ce94d63748a55"

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl = "login")

crypt = CryptContext(schemes=["bcrypt"]) #contexto de encriptación

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool

class UserDB(User): 
    password: str

#Aca la contraseña es necesario que se encripte usando bcrypt, porque de esta manera no expones la misma en la db
#Y se compara la contraseña ingresada por el usuario con la contraseña encriptada guardada en la db
#y eso devuelve un hash, que es el token
users_db = {
    "dans182": {
        "username": "dans182",
        "full_name": "Daniel Martinez",
        "email": "dans@xmail.com",
        "disable": False,
        "password": "$2a$12$5OOZM9s2C8/PVtMdOAY54ueAPQCcDtPf08FdfFtVNvIC87ZDyDlqa"
    },
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "mourevev@xmail.com",
        "disable": True,
        "password": "$2a$12$dWJrC6JzXz5T2WpvZFgfHeMuQJ.HrRRnbkMmULBdfAC5nhm7ygz4u"
    }
}

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

async def auth_user(token: str = Depends(oauth2)):
    exception: HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas", 
        headers={"WWW-Authenticate": "Bearer"})
    try:
        username = jwt.decode(token, SECRET,algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
    except JWTError:
        raise exception
    
    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
    if user.disable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user

# #operacion de autenticacion
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()): #Esto significa que esta operación va a recibir datos, pero no depende de nadie
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El usuario no es correcto")

    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=400, detail="La contraseña no es correcto")
    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    access_token = {"sub": user.username, "exp": expire}

    return{"access_token": jwt.encode(access_token, SECRET,algorithm=ALGORITHM), "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
