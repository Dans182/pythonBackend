from fastapi import FastAPI
from pydantic import BaseModel
#pydantic nos ayuda a definir una entidad

app = FastAPI()

# Creamos la entidad User()
class User(BaseModel): # Este Basemodel como parámetro, nos está dando la capacidad de crear una entidad
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name = "Daniel", surname = "Moure", url = "https://www.google.ve", age = 50),
              User(name = "Euge", surname = "Bordenave", url = "https://www.google.com", age = 25),
              User(name = "Reck", surname = "Jowar", url = "https://www.google.com", age = 30)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Daniel", "surname": "Gaiteiro", "url": "https:www.google.com", "age": 20},
            {"name": "Euge", "surname": "Bordenave", "url": "https:www.google.com", "age": 25},
            {"name": "Reck", "surname": "Jowar", "url": "https:www.google.com","age": 30}]

# Los JSON es una forma de estructurar datos que todos lo entiendan. Servidores, clientes, etc

@app.get("/users")
async def users():
    return users_list