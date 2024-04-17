from fastapi import FastAPI
from db.dynamo import create_tables

app = FastAPI()

create_tables()