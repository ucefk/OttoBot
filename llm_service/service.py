from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present) curl -X POST http://localhost:11434/api/generate -H "Content-Type: application/json" -d '{"model": "qwen2:0.5b","prompt": "Give me an introduction to computer science."}'
dotenv_file = ".env"
load_dotenv(dotenv_file)

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
MODEL_SERVICE = os.getenv("MODEL_SERVICE")
MODEL_PORT = os.getenv("MODEL_PORT")

# Define a class for the input data
class InputData(BaseModel):
    question: str

# Initialize the model and the prompt
template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model=OLLAMA_MODEL)
chain = prompt | model

app = FastAPI()

@app.post("/predict")
async def predict(data: InputData):
    # Generate the response
    response = chain.invoke({"question": data.question})

    # Return the response
    return {"response": response}

@app.get("/status")
async def status():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host=MODEL_SERVICE, port=MODEL_PORT, reload=True)
