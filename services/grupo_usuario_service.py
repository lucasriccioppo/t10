from models.grupo_usuario import grupo_usuario_table
from database import engine
from sqlalchemy.sql import select
from utils import auth

conn = engine.connect()

def create(name):
    ins = grupo_usuario_table.insert()

    new_group = ins.values( name = name)
    
    conn.execute(new_group)
    return "grupo criado!"

def find_by_name(name):
    s = select([grupo_usuario_table]).where(
        grupo_usuario_table.c.name == name
    )
    query = conn.execute(s)
    result = query.fetchone()
    query.close()
    return result

def find_by_id(id):
    s = select([grupo_usuario_table]).where(
        grupo_usuario_table.c.id == id
    )
    query = conn.execute(s)
    result = query.fetchone()
    query.close()
    return result