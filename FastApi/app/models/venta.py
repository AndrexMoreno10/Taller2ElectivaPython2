from pydantic import BaseModel
from models.user import User

class Venta(BaseModel):
    id: int
    cantidad: int
    precio: str
    user: User
    descripcion: str