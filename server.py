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
from controllers import usuario_controller, produto_controller, cliente_controller

metadata.create_all()

from utils import create_grupos_usuario

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
@app.post("/produto/{token}", status_code=201)
def create_produto(produto: Produto, token):
    return produto_controller.create_produto(produto, token)

@app.get("/produto/{token}")
def find_produtos(token):
    return produto_controller.find_produtos(token)

@app.get("/produto/{produto_id}/{token}")
def find_produto_by_id(produto_id: int, token):
    return produto_controller.find_produto_by_id(produto_id, token)

@app.get("/produto/codigo/{codigo}/{token}")
def find_produto_by_codigo(codigo: int, token):
    return produto_controller.find_produto_by_codigo(codigo, token)

@app.delete("/produto/{id}/{token}")
def delete_produto_by_id(id: int, token):
    return produto_controller.delete_produto_by_id(id, token)

#Cliente
@app.post("/cliente/{token}", status_code=201)
def create_cliente(cliente: Cliente, token):
    return cliente_controller.create_cliente(cliente, token)

@app.get("/cliente/{token}")
def find_clientes(token):
    return cliente_controller.find_clientes(token)

@app.get("/cliente/{cliente_id}/{token}")
def find_cliente_by_id(cliente_id: int, token):
    return cliente_controller.find_cliente_by_id(cliente_id, token)

@app.get("/cliente/cnpj/{cnpj}/{token}")
def find_cliente_by_cnpj(cnpj: str, token):
    return cliente_controller.find_cliente_by_cnpj(cnpj, token)

@app.delete("/cliente/{id}/{token}")
def delete_cliente_by_id(id: int, token):
    return cliente_controller.delete_cliente_by_id(id, token)