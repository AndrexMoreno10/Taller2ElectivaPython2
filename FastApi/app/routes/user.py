from fastapi import APIRouter, Body , HTTPException
from models.user import User

users_route = APIRouter()


@users_route.get("/")
async def get_users():
    try:
        users = list(User.select().dicts())
        return {"data": users}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@users_route.post("/")
async def create_user(user: User = Body(...)):
    try:
        new_user = User.create(**user.dict())
        return {"message": "User created", "data": new_user.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@users_route.put("/{user_id}")
async def update_user(user_id: int, user: User = Body(...)):
    try:
        user_to_update = User.get(User.id == user_id)
        user_to_update.username = user.username
        user_to_update.email = user.email
        user_to_update.age = user.age
        user_to_update.save()
        return {"message": "User updated"}
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@users_route.delete("/")
async def delete_user(user_id: int):
    try:
        user_to_delete = User.get(User.id == user_id)
        user_to_delete.delete_instance()
        return {"message": "User deleted"}
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
