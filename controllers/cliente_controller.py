from services import cliente_service, grupo_usuario_service
from models.cliente import Cliente
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
        


def create_cliente(cliente: Cliente, token):
    verifica_permissao(token, list_permissao)

    return cliente_service.create(cliente)

def find_clientes(token):
    verifica_permissao(token, list_permissao)

    return cliente_service.find()

def find_cliente_by_cnpj(cnpj, token):
    verifica_permissao(token, list_permissao)
    
    return cliente_service.find_by_cnpj(cnpj)

def find_cliente_by_id(id, token):
    verifica_permissao(token, list_permissao)

    return cliente_service.find_by_id(id)

def delete_cliente_by_id(id, token):
    verifica_permissao(token, list_permissao)

    return cliente_service.delete_cliente(id)