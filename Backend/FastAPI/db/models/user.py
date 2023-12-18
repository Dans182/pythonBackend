from pydantic import BaseModel
from typing import Optional

class User(BaseModel): 
    id: Optional[str] = None #Aca decimos que es opcional. Puede que el campo ID no nos llegue.
    username: str
    email: str