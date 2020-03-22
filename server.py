# uvicorn main:app --reload
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
from controllers import usuario_controller, produto_controller

metadata.create_all()

app = FastAPI()

# Usuario
@app.post("/usuario/", status_code=201)
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

#Produtos
@app.post("/produto/", status_code=201)
def create_produto(produto: Produto):
    return produto_controller.create_produto(produto)

@app.get("/produto/")
def find_produtos():
    return produto_controller.find_produtos()

@app.get("/produto/{produto_id}")
def find_produto_by_id(produto_id: int):
    return produto_controller.find_produto_by_id(produto_id)

@app.get("/produto/{codigo}")
def find_produto_by_codigo(codigo: int):
    return produto_controller.find_produto_by_codigo(codigo)

@app.delete("/produto/{id}")
def delete_produto_by_id(id: int):
    return produto_controller.delete_produto_by_id(id)