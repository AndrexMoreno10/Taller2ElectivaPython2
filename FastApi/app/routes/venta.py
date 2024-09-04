from fastapi import APIRouter, Body
from models.venta import Venta

ventas_route = APIRouter()

@ventas_route.get("/")
async def get_venta():
    try:
        return {"message": "Get Venta data"}
    except Exception as e:
        return {"error": str(e)}

@ventas_route.post("/")
async def post_venta(venta: Venta = Body(...)):
    try:
        return {"message": "Venta Created"}
    except Exception as e:
        return {"error": str(e)}    

@ventas_route.put("/")
async def put_venta():
    try:
        return {"message": "Venta Put"}
    except Exception as e:
        return {"error": str(e)}
    
@ventas_route.delete("/")
async def delete_venta():
    try:
        return {"message": "Venta Eliminated"}
    except Exception as e:
        return {"error": str(e)}        
