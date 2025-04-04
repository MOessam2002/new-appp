from fastapi import FastAPI
from .routes import users

app = FastAPI()

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Welcome to DevOps Practice App!"}
