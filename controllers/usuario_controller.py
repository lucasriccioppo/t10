from services import usuario_service
from models.usuario import Usuario

def create_user(usuario: Usuario):
    return usuario_service.create_user(usuario)