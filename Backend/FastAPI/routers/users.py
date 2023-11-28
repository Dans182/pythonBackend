from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
#pydantic nos ayuda a definir una entidad

router = APIRouter(prefix = "/users", tags = ["users"], responses = {404: {"message": "No encontrado"}})

# Creamos la entidad User()
class User(BaseModel): # Este Basemodel como parámetro, nos está dando la capacidad de crear una entidad
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id = 1, name = "Daniel", surname = "Moure", url = "https://www.google.ve", age = 50),
              User(id = 2, name = "Euge", surname = "Bordenave", url = "https://www.google.com", age = 25),
              User(id = 3, name = "Reck", surname = "Jowar", url = "https://www.google.com", age = 30)]

@router.get("/json")
async def usersjson():
    return [{"name": "Daniel", "surname": "Gaiteiro", "url": "https:www.google.com", "age": 20},
            {"name": "Euge", "surname": "Bordenave", "url": "https:www.google.com", "age": 25},
            {"name": "Reck", "surname": "Jowar", "url": "https:www.google.com","age": 30}]

# Los JSON es una forma de estructurar datos que todos lo entiendan. Servidores, clientes, etc

@router.get("/")
async def users():
    return users_list