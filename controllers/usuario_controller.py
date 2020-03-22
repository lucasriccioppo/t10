from services import usuario_service
from models.usuario import Usuario, UsuarioLogin
from utils import auth
from fastapi import status
from fastapi.responses import JSONResponse


def create_user(usuario: Usuario):
    return usuario_service.create(usuario)

def login(data: UsuarioLogin):
    user = usuario_service.find_by_email(data.email)

    if user and auth.check_password(data.password, user.password):
        return auth.get_token({'id': user.id, 'email': user.email, 'nome': user.name, 'level': user.grupo_usuario})
    else:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content="Email ou senha incorretos")

def find_usuarios():
    return usuario_service.find()

def find_user_by_id(id):
    return usuario_service.find_by_id(id)