#Users DB API
from fastapi import APIRouter, HTTPException
from db.models.user import User

router = APIRouter(prefix = "/usersdb", 
                   tags = ["usersdb"], 
                   responses = {404: {"message": "No encontrado"}})


users_list = []

@router.get("/")
async def users():
    return users_list