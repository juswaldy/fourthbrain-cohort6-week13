from fastapi import FastAPI
from pydantic import BaseModel
from models import huggingface as hf


app = FastAPI()


################################################################################
# Prepare schemas.

class PredictionRequest(BaseModel):
    query_string: str

################################################################################
# Setup endpoints.

@app.get("/health")
def health():
    return "Service is online."

@app.post("/sentiment")
def sentiment(request: PredictionRequest):
      # YOUR CODE GOES HERE
      return hf.sentiment_model(request.query_string)

