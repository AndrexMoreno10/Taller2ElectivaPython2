from pydantic import BaseModel

class Vehicle(BaseModel):
    id: int
    modelo: str
    color: str
    placa: str