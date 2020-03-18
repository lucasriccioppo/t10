from datetime import datetime
from sqlalchemy import (Column, Table, Integer, String, DateTime, ForeignKey)
from database import metadata
from .grupo_usuario import grupo_usuario_table

user_table = Table( 'usuarios', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(40), index=True),
                    Column('age', Integer, nullable=False),
                    Column('password', String),
                    Column('grupo_usuario', ForeignKey('grupo_usuario.id')),
                    Column('created_at', DateTime, default=datetime.now),
                    Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now))