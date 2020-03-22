from services import usuario_service
from models.usuario import Usuario, UsuarioLogin

def create_user(usuario: Usuario):
    return usuario_service.create(usuario)

def login(data: UsuarioLogin):
    user = usuario_service.find_by_email(data.email)
    return user

def find_usuarios():
    return usuario_service.find()

def find_user_by_id(id):
    return usuario_service.find_by_id(id)