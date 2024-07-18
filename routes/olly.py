from fastapi import APIRouter
from models.olly_data import OllyDataModel
from bucket.s3 import load_olly_data_from_s3
from scripts.predict_model import train_and_predict_model

routes_olly = APIRouter()

@routes_olly.post("/predict/")
async def prediction(answersArray: OllyDataModel):
  transformed_array = [list(answersArray.answersArray[0][0].values())]
  return {'car_predicted': train_and_predict_model(load_olly_data_from_s3(), transformed_array)}