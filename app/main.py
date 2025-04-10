from fastapi import FastAPI,Request,Response
from app.routes.v1.auth import router as router_auth


app = FastAPI()

app.include_router(router_auth, tags=["Authentication"])

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.middleware("http")
async def cors_handler(request: Request, call_next):
    # Gestione preflight OPTIONS
    if request.method == "OPTIONS":
        response = Response()
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
        return response

    # Continuare con la richiesta normale
    response: Response = await call_next(request)
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
    return response