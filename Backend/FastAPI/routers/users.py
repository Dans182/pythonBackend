from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
#pydantic nos ayuda a definir una entidad

router = APIRouter()

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

@router.get("/usersjson")
async def usersjson():
    return [{"name": "Daniel", "surname": "Gaiteiro", "url": "https:www.google.com", "age": 20},
            {"name": "Euge", "surname": "Bordenave", "url": "https:www.google.com", "age": 25},
            {"name": "Reck", "surname": "Jowar", "url": "https:www.google.com","age": 30}]

# Los JSON es una forma de estructurar datos que todos lo entiendan. Servidores, clientes, etc

@router.get("/users")
async def users():
    return users_list

#Podemos llamar a un usuario por un Path o por un Query
#Por medio de un Path
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)
    # users = filter(lambda user: user.id == id, users_list) #Tiene primero un objeto user. Dentro de ese objeto, queremos que compare el campo id de esa clase user, con el ID que se para como parametro. A mayores le pasamos para que itere en la lista, por eso el users_list
    # try:
    #     return list(users)[0] #El filter puede devolvernos varios objetos, es por esa razón que creamos una lista. En esa lista, le pasamos la variable users que nace a razón del filter
    # except:
    #     return {"error": "No se ha encontrado el usuario"}

#El resultado que devuelve en la API es un listado, pero en nuestra operación nos interesa solo la primer concordancia
#Lo hacemos con el list(users)[0]
#Y nos devuelve algo asi 
"""
{
  "id": 3,
  "name": "Reck",
  "surname": "Jowar",
  "url": "https://www.google.com",
  "age": 30
}
"""

#Si no lo tuvieramos con el [0], nos devolvería
"""
[{
  "id": 3,
  "name": "Reck",
  "surname": "Jowar",
  "url": "https://www.google.com",
  "age": 30
}]
"""

# Por medio de un Query 
@router.get("/userquery/")
async def user(id: int):
    return search_user(id)
# Otro Query que la url es la misma que el del path
@router.get("/user/")
async def user(id: int):
    return search_user(id)

# @router.get("/userquery/")
# async def user(id: int):
#     users = filter(lambda user: user.id == id, users_list) #Tiene primero un objeto user. Dentro de ese objeto, queremos que compare el campo id de esa clase user, con el ID que se para como parametro. A mayores le pasamos para que itere en la lista, por eso el users_list
#     try:
#         return list(users)[0] #El filter puede devolvernos varios objetos, es por esa razón que creamos una lista. En esa lista, le pasamos la variable users que nace a razón del filter
#     except:
#         return {"error": "No se ha encontrado el usuario"}
    
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list) #Tiene primero un objeto user. Dentro de ese objeto, queremos que compare el campo id de esa clase user, con el ID que se para como parametro. A mayores le pasamos para que itere en la lista, por eso el users_list
    try:
        return list(users)[0] #El filter puede devolvernos varios objetos, es por esa razón que creamos una lista. En esa lista, le pasamos la variable users que nace a razón del filter
    except:
        return {"error": "No se ha encontrado el usuario"}
    
# El Path se suele utilizar cuando se considera que es un parámetro obligatorio. Una url que es fija.
# Los queries para los parametros que pueden NO ser necesarios para realizar la petición. Parámetros que pueden ir o no

#Crear nuevo usuario
@router.post("/user/", status_code=201) #codigo de respuesta por defecto
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code = 204, detail="El usuario ya existe")
        #return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)
        return user

#Actualizar datos
@router.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return user
    
#Eliminar datos
@router.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario"}
