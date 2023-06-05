from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

class Item(BaseModel):
  name: str
  price: float
  description: str | None = None

app = FastAPI()

items = []

@app.get("/")
async def index():
  return {"message": "Hello API"}

@app.get("/ping")
async def ping():
  return {"message": "pong"}

# Get Items 
@app.get("/api/v1/items")
async def get_items(item: Item):
  return {"data": items}

# Create Item
@app.post("/api/v1/items")
async def create_item(item: Item):
  items.append(item)
  return {"data": item.dict(), "status": "OK"}
