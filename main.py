from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline


app = FastAPI()


################################################################################
# Prepare schemas.

class PredictionRequest(BaseModel):
    query_string: str

################################################################################
# Load models.

sentiment_model = pipeline("sentiment-analysis")

################################################################################
# Setup endpoints.

@app.get("/health")
def health():
    return "Service is online."

@app.post("/sentiment")
def sentiment(request: PredictionRequest):
      # YOUR CODE GOES HERE
      return sentiment_model(request.query_string)

