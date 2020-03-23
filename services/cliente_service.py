from models.cliente import cliente_table
from database import engine
from sqlalchemy.sql import select
from utils import auth

conn = engine.connect()

def create(cliente):
    ins = cliente_table.insert()

    new_cliente = ins.values(  name = cliente.name,
                            cnpj = cliente.cnpj)

    conn.execute(new_cliente)
    return "cliente criado!"

def find_by_cnpj(cnpj):
    s = select([cliente_table]).where(
        cliente_table.c.cnpj == cnpj
    )
    query = conn.execute(s)
    result = query.fetchone()
    query.close()
    return result

def find():
    s = cliente_table.select()
    query = conn.execute(s)
    result = query.fetchall()
    query.close()
    return result

def find_by_id(id):
    s = select([cliente_table]).where(
        cliente_table.c.id == id
    )
    query = conn.execute(s)
    result = query.fetchone()
    query.close()
    return result

def delete_cliente(id):
    delete = cliente_table.delete().where(
        cliente_table.c.id == id
    )

    return conn.execute(delete)