from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

#El primero se encarga de gestionar la autenticacion
#El segundo, es la forma en que se envia a nuestro Backend los criterios de autenticacion. 

app = FastAPI()

#Creamos una instancia de nuestro sistema de autenticación
oath2 = OAuth2PasswordBearer(tokenUrl = "login")
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool

class UserDB(User): #El usuario de la DB tiene todo lo del User, por eso lo pasamos como parámetro, mas el password
    password: str


users_db = { #a falta de una base de dato, la crearemos acá como variable.
    #Al usar dbc relacional, el formato es JSON
    "dans182": {
        "username": "dans182",
        "full_name": "Daniel Martinez",
        "email": "dans@xmail.com",
        "disable": False,
        "password": "123456"
    },
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "mourevev@xmail.com",
        "disable": True,
        "password": "654321"
    }
}

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username]) #Aca estoy creando un UserDB y le paso de nuestra DB el usuario que coincide con la clave

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

async def current_user(token: str = Depends(oath2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas", 
            headers={"WWW-Authenticate": "Bearer"})
    
    if user.disable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return user

#operacion de autenticacion
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()): #Esto significa que esta operación va a recibir datos, pero no depende de nadie
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El usuario no es correcto")

    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="La contraseña no es correcto")
    
    return{"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
