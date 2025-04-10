from fastapi import FastAPI
from app.routes.v1.auth import router as router_auth


app = FastAPI()

app.include_router(router_auth, tags=["Authentication"])

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

