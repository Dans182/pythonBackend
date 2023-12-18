from fastapi import APIRouter, HTTPException, status
from .users import users_list, User

router = APIRouter(prefix = "/userdb", 
                   tags = ["userdb"], 
                   responses = {status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list) #Tiene primero un objeto user. Dentro de ese objeto, queremos que compare el campo id de esa clase user, con el ID que se para como parametro. A mayores le pasamos para que itere en la lista, por eso el users_list
    try:
        return list(users)[0] #El filter puede devolvernos varios objetos, es por esa razón que creamos una lista. En esa lista, le pasamos la variable users que nace a razón del filter
    except:
        return {"error": "No se ha encontrado el usuario"}

#POST
#Crear nuevo usuario
@router.post("/", status_code=status.HTTP_201_CREATED) 
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")
        #return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)
        return user

#GET
#Por medio de un Path
@router.get("/{id}")
async def user(id: int):
    return search_user(id)

# Por medio de un Query 
@router.get("/query")
async def user(id: int):
    return search_user(id)

# Otro Query que la url es la misma que el del path
@router.get("/")
async def user(id: int):
    return search_user(id)

#PUT
#Actualizar datos
@router.put("/")
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

#DELETE
#Eliminar datos
@router.delete("/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario"}
