from models.usuario import user_table
from database import engine
from sqlalchemy import select
from utils import auth

conn = engine.connect()

def create(usuario):
    ins = user_table.insert()

    new_user = ins.values(  name = usuario.name,
                            age = usuario.age,
                            email = usuario.email,
                            password = auth.hash_password(usuario.password),
                            grupo_usuario = usuario.grupo_usuario)
    
    conn.execute(new_user)
    return "usuario criado!"

def find_by_email(email):
    s = select([user_table]).where(
        user_table.c.email == email
    )
    query = conn.execute(s)
    result = query.fetchone
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
    result = query.fetchone
    query.close()
    return result


"""
def delete_user(id):
    delete = user_table.delete().where(
        usuarios.id == id
    )

    conn.execute(delete)"""

