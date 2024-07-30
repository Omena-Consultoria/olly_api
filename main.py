from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.db import create_tables
from routes.user import routes_user
from routes.olly import routes_olly

app = FastAPI()

origins = ["https://carroideal.omenaseguros.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST, OPTIONS"],
    allow_headers=["*"],
)

app.include_router(routes_user, prefix="/user")
app.include_router(routes_olly, prefix="/olly")

create_tables()