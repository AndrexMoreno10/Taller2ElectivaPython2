from pydantic import BaseModel
from database import database

class User(BaseModel):
    id: int
    name: str
    age: str
    email: str
    adress: str
    document: str
    
    class Meta:
        database = database  # Conectar con la base de datos
        table_name = "users"