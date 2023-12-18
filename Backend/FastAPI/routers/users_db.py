#Users DB API
from fastapi import APIRouter, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import users_schema

router = APIRouter(prefix = "/usersdb", 
                   tags = ["usersdb"], 
                   responses = {status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

users_list = []

@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.local.users.find())