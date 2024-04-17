from .db import dynamodb
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse

table = dynamodb.Table("olly-database")

def create_user(user: dict):
  try:
    table.put_item(Item=user)
  except ClientError as e:
    return JSONResponse(content=e.response["Error"], status_code=500)