from ..models.usuario import user_table
from database import engine

conn = engine.connect()

def create_user(user, level_usuario):
    ins = user_table.insert()

    new_user = ins.values(  name = user.name,
                            age = user.age,
                            password = user.password,
                            grupo_usuario = level_usuario)
                        
    conn.execute(new_user)

# def find_users():

def find_user(id):
    return usuarios.query.get(id)


def delete_user(id):
    delete = user_table.delete().where(
        usuarios.id == id
    )

    conn.execute(delete)