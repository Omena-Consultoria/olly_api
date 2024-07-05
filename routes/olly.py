from fastapi import APIRouter
from models.olly_data import OllyDataModel
from bucket.s3 import load_olly_data_from_s3
from scripts.predict_model import train_and_predict_model

routes_olly = APIRouter()

@routes_olly.post("/predict/", response_model=OllyDataModel)
async def prediction(answersArray: OllyDataModel):
  return {'car_predicted': train_and_predict_model(load_olly_data_from_s3(), answersArray.answersArray)}