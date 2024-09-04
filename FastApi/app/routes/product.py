from fastapi import APIRouter, Body
from models.product import Product

products_route = APIRouter()

@products_route.get("/")
async def get_product():
    try:
        return {"message": "Get Product data"}
    except Exception as e:
        return {"error": str(e)}

@products_route.post("/")
async def post_product(product: Product = Body(...)):
    try:
        return {"message": "Product Created"}
    except Exception as e:
        return {"error": str(e)}    

@products_route.put("/")
async def put_product():
    try:
        return {"message": "Product Put"}
    except Exception as e:
        return {"error": str(e)}
    
@products_route.delete("/")
async def delete_product():
    try:
        return {"message": "Product Eliminated"}
    except Exception as e:
        return {"error": str(e)}        
