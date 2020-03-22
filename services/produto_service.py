from models.produto import produto_table
from database import engine
from sqlalchemy.sql import select
from utils import auth

conn = engine.connect()

def create(produto):
    ins = produto_table.insert()

    new_produto = ins.values(  name = produto.name,
                            codigo = produto.codigo,
                            value = produto.value)

    conn.execute(new_produto)
    return "produto criado!"

def find_by_codigo(codigo):
    s = select([produto_table]).where(
        produto_table.c.codigo == codigo
    )
    query = conn.execute(s)
    result = query.fetchone()
    query.close()
    return result

def find():
    s = produto_table.select()
    query = conn.execute(s)
    result = query.fetchall()
    query.close()
    return result

def find_by_id(id):
    s = select([produto_table]).where(
        produto_table.c.id == id
    )
    query = conn.execute(s)
    result = query.fetchone()
    query.close()
    return result

def delete_produto(id):
    delete = produto_table.delete().where(
        produto_table.c.id == id
    )

    return conn.execute(delete)