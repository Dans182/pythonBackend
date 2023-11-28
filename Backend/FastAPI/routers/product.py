from fastapi import APIRouter
from .products import products_list

router = APIRouter(prefix = "/product", tags = ["product"], responses = {404: {"message": "No encontrado"}})

@router.get("/{id}")
async def products(id: int):
    return products_list[id]
