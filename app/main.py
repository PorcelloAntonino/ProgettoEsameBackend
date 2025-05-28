from fastapi import FastAPI,Request,Response
from fastapi.middleware.cors import CORSMiddleware
from app.routes.v1.auth import router as router_auth
from app.routes.v1.dipendente.dipendente import router as router_dipendenti
from app.routes.v1.macchine import router as router_macchine
from app.routes.v1.controlli import router as router_controlli
from app.routes.v1.vendite import router as router_vendite
from app.routes.v1.magazzino import router as router_magazino
from app.routes.v1.macchineControlli import router as router_macchineControlli

app = FastAPI() 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router_auth, tags=["Authentication"])
app.include_router(router_dipendenti)
app.include_router(router_macchine)

app.include_router(router_controlli)

app.include_router(router_vendite)

app.include_router(router_magazino)

app.include_router(router_macchineControlli)
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