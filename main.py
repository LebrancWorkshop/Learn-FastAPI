from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
def index():
  return {"message": "Hello, API"}

@app.get("/ping")
def ping():
  return {"message": "pong"}


