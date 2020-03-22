from models.usuario import user_table
from database import engine
from sqlalchemy.sql import select
from utils import auth
from services import grupo_usuario_service
from fastapi import status
from fastapi.responses import JSONResponse

conn = engine.connect()

def create(usuario):
    ins = user_table.insert()

    grupo = grupo_usuario_service.find_by_name(usuario.grupo_usuario)

    if not grupo:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Grupo de usuarios nao encontrado")

    new_user = ins.values(  name = usuario.name,
                            age = usuario.age,
                            email = usuario.email,
                            password = auth.hash_password(usuario.password),
                            grupo_usuario = grupo.id)
    
    conn.execute(new_user)
    return "usuario criado!"

def find_by_email(email):
    s = select([user_table]).where(
        user_table.c.email == email
    )
    query = conn.execute(s)
    result = query.fetchone()
    query.close()
    return result

def find():
    s = user_table.select()
    query = conn.execute(s)
    result = query.fetchall()
    query.close()
    return result

def find_by_id(id):
    s = select([user_table]).where(
        user_table.c.id == id
    )
    query = conn.execute(s)
    result = query.fetchone()
    query.close()
    return result

