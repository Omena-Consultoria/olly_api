from pydantic import BaseModel
from typing import Dict

class OllyDataModel(BaseModel):
  answersArray: Dict