from services import produto_service
from models.produto import Produto
from utils import auth
from fastapi import status
from fastapi.responses import JSONResponse


def create_produto(produto: Produto):
    return produto_service.create(produto)

def find_produtos():
    return produto_service.find()

def find_produto_by_codigo(codigo):
    return produto_service.find_by_codigo(codigo)

def find_produto_by_id(id):
    return produto_service.find_by_id(id)

def delete_produto_by_id(id):
    return produto_service.delete_produto(id)