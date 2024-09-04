from pydantic import BaseModel

class Animal(BaseModel):
    id: int
    name: str
    edad: str
    raza: str