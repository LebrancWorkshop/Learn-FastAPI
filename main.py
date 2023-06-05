from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
async def index():
  return {"message": "Hello, API"}

@app.get("/ping")
async def ping():
  return {"message": "pong"}

# Path Parameter
@app.get("/tutorial/path/{tutorial_name}")
async def get_podcast(tutorial_name):
  return {"tutorial_name": tutorial_name}

# Path Parameter with Type
@app.get("/tutorial/path/type/{tutorial_id}")
async def get_podcast(tutorial_id: int): # Must use async
  return {"tutorial_id": tutorial_id}
