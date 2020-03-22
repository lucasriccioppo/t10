from models.usuario import grupo_usuario_table
from database import engine
from sqlalchemy.sql import select
from utils import auth

conn = engine.connect()

def create(name, level):
    ins = grupo_usuario_table.insert()

    new_group = ins.values(  name = name,
                            level = level)
    
    conn.execute(new_group)
    return "grupo criado!"