from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items")
async def read_item():
    return {"items": ["Learn Docker", "Learn FastAPI"]}