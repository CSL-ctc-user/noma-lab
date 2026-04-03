from fastapi import FastAPI
import vertexai
from vertexai.generative_models import GenerativeModel

app = FastAPI()
vertexai.init(project="my-project-csl-486600", location="asia-northeast1")
model = GenerativeModel("gemini-2.0-flash")

@app.post("/chat")
async def chat(body: dict):
    response = model.generate_content(body["message"])
    return {"response": response.text}
