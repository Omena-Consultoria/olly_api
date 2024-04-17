from fastapi import APIRouter
from models.user import User
from database.user import create_user

routes_user = APIRouter()

@routes_user.post("/register", response_model=User)
def register(user:User):
  return create_user(user.model_dump()) 