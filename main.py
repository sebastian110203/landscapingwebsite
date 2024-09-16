from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the static directory to serve files from the static folder
app.mount("/", StaticFiles(directory="static",html=True),name="static")

@app.get("/")
async def read_root():
    return {"message": "Welcome to your FastAPI website!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

