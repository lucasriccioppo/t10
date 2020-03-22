from models.usuario import user_table
from database import engine

conn = engine.connect()

def create_user(usuario):
    ins = user_table.insert()

    new_user = ins.values(  name = usuario.name,
                            age = usuario.age,
                            password = usuario.password,
                            grupo_usuario = usuario.grupo_usuario)
    
    conn.execute(new_user)
    return "usuario criado!"

# def find_users():

def find_user(id):
    return usuarios.query.get(id)


def delete_user(id):
    delete = user_table.delete().where(
        usuarios.id == id
    )

    conn.execute(delete)