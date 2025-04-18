from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}

# Simple GET endpoint
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}

# POST endpoint example
class User(BaseModel):
    name: str
    age: int

@app.post("/user")
def create_user(user: User):
    return {"message": f"User {user.name} added!", "data": user.dict()}
