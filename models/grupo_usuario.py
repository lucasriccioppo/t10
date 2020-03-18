from datetime import datetime
from sqlalchemy import (Column, Table, Integer, String, DateTime)
from database import metadata

grupo_usuario_table = Table( 'grupo_usuario', metadata,
                             Column('id', Integer, primary_key=True),
                             Column('name', String(40), index=True),
                             Column('level', Integer, nullable=False),
                             Column('created_at', DateTime, default=datetime.now),
                             Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now))
