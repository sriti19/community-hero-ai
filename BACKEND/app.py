from fastapi import FastAPI
from pydantic import BaseModel
from ai_classifier import classify_issue

app = FastAPI()


class IssueRequest(BaseModel):
    description: str


@app.get("/")
def home():
    return {
        "message": "Community Hero API is running successfully!"
    }


@app.post("/classify")
def classify(request: IssueRequest):

    result = classify_issue(request.description)

    return result