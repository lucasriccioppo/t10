# hypercorn uvicorn main:app --reload
# docker run --name t10 -e POSTGRES_PASSWORD=123 -d -p 5432:5432 postgres
# ou
# docker start t10
# docker exec -it t10 bash
# psql -U postgres
# CREATE DATABASE t10db;
# \c t10db -> connect to db
# -------------------------------------------------------

from fastapi import FastAPI
from models.models import *
from database import metadata
from controllers import usuario_controller

metadata.create_all()

app = FastAPI()

# Usuario
@app.post("/usuario/")
def create_usuario(usuario: Usuario):
    return usuario_controller.create_user(usuario)

@app.get("/usuario/")
def find_usuarios():
    return usuario_controller.find_usuarios()
    
@app.get("/usuario/{usuario_id}")
def find_usuario_by_id(usuario_id: int):
    return usuario_controller.find_user_by_id(usuario_id)

@app.post("/usuario/login/")
def login(data: UsuarioLogin):
    return usuario_controller.login(data)
