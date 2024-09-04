from fastapi import APIRouter, Body
from models.animal import Animal

animals_route = APIRouter()

@animals_route.get("/")
async def get_animal():
    try:
        return {"message": "Get Animal data"}
    except Exception as e:
        return {"error": str(e)}

@animals_route.post("/")
async def post_animal(animal: Animal = Body(...)):
    try:
        return {"message": "Animal Created"}
    except Exception as e:
        return {"error": str(e)}    

@animals_route.put("/")
async def put_animal():
    try:
        return {"message": "Animal Put"}
    except Exception as e:
        return {"error": str(e)}
    
@animals_route.delete("/")
async def delete_animal():
    try:
        return {"message": "Animal Eliminated"}
    except Exception as e:
        return {"error": str(e)}        
