from fastapi import APIRouter, Body
from models.vehicle import Vehicle

vehicles_route = APIRouter()

@vehicles_route.get("/")
async def get_vehicle():
    try:
        return {"message": "Get Vehicle data"}
    except Exception as e:
        return {"error": str(e)}

@vehicles_route.post("/")
async def post_vehicle(vehicle: Vehicle = Body(...)):
    try:
        return {"message": "Vehicle Created"}
    except Exception as e:
        return {"error": str(e)}    

@vehicles_route.put("/")
async def put_vehicle():
    try:
        return {"message": "Vehicle Put"}
    except Exception as e:
        return {"error": str(e)}
    
@vehicles_route.delete("/")
async def delete_vehicle():
    try:
        return {"message": "Vehicle Eliminated"}
    except Exception as e:
        return {"error": str(e)}        
