from services import produto_service, grupo_usuario_service
from models.produto import Produto
from utils import auth
from fastapi import status
from fastapi.responses import JSONResponse

list_permissao = ['ANALISTA_DE_PEDIDOS', 'ADMINISTRADOR']

def verifica_permissao(token, lista):
    if not token:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content="Não há acessos suficientes")

    decoded = auth.decode(token)

    grupo = grupo_usuario_service.find_by_id(decoded["usuario"]["level"])

    if grupo.name not in lista:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content="Não há acessos suficientes")
        


def create_produto(produto: Produto, token):
    verifica_permissao(token, list_permissao)

    return produto_service.create(produto)

def find_produtos(token):
    verifica_permissao(token, list_permissao)

    return produto_service.find()

def find_produto_by_codigo(codigo, token):
    verifica_permissao(token, list_permissao)
    
    return produto_service.find_by_codigo(codigo)

def find_produto_by_id(id, token):
    verifica_permissao(token, list_permissao)

    return produto_service.find_by_id(id)

def delete_produto_by_id(id, token):
    verifica_permissao(token, list_permissao)

    return produto_service.delete_produto(id)
"""
def update_poduto_by_id(id, token):
    if not verifica_permissao(produto.token, list_permissao):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content="Não há acessos suficientes")
"""
    