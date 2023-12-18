#Users DB API
from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.client import db_client

router = APIRouter(prefix = "/usersdb", 
                   tags = ["usersdb"], 
                   responses = {status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


users_list = []

@router.get("/")
async def users():
    return users_list