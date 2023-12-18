from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema
from bson import ObjectId

router = APIRouter(prefix = "/userdb", 
                   tags = ["userdb"], 
                   responses = {status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

def search_user(field: str, key):
    try:
        user = db_client.local.users.find_one({field: key}) #Aca lo busco en DB
        return User(**user_schema(user))
    except:
        return {"error": "No se ha encontrado el usuario"} #aca creamos la transformacion a diccionario y creamos el objeto user

#POST
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED) 
async def user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="El usuario ya existe")
    user_dict = dict(user)
    del user_dict["id"] #Al dejarlo opcional en el schema, si no le pasamos ID lo crea como un null. Es por eso que mandamos a borrar el id, para que mongo me autogenere el ID
    id = db_client.local.users.insert_one(user_dict).inserted_id
    
    new_user = user_schema(db_client.local.users.find_one({"_id": id}))

    return User(**new_user)

#GET
#Por medio de un Path
@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))

# Por medio de un Query 
@router.get("/query")
async def user(id: str):
    return search_user("_id", ObjectId(id))

# Otro Query que la url es la misma que el del path
@router.get("/")
async def user(id: str):
    return search_user("_id", ObjectId(id))

#PUT
@router.put("/", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    found = db_client.local.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return user

#DELETE
@router.delete("/{id}")
async def user(id: str):
    found = db_client.local.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return user
