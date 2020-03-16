from models.usuario import user_table
from database import engine

conn = engine.connect()

ins = user_table.insert()

new_user = ins.values(name='Lucas',
                     age=22,
                     password='senha123')
                    
conn.execute(new_user)