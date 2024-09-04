from fastapi import APIRouter, Body
from models.user import User

users_route = APIRouter()

@users_route.get("/")
async def get_user():
    try:
        return {"message": "Get User data"}
    except Exception as e:
        return {"error": str(e)}

@users_route.post("/")
async def post_user(user: User = Body(...)):
    try:
        return {"message": "User Created"}
    except Exception as e:
        return {"error": str(e)}    

@users_route.put("/")
async def put_user():
    try:
        return {"message": "User Put"}
    except Exception as e:
        return {"error": str(e)}
    
@users_route.delete("/")
async def delete_user():
    try:
        return {"message": "User Eliminated"}
    except Exception as e:
        return {"error": str(e)}        
