from fastapi import FastAPI
from aws.dynamo import create_tables

app = FastAPI()

create_tables()