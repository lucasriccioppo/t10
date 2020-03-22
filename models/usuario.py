from datetime import datetime
from sqlalchemy import (Column, Table, Integer, String, DateTime, ForeignKey)
from database import metadata
from .grupo_usuario import grupo_usuario_table
from pydantic import BaseModel

user_table = Table( 'usuarios', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(40), index=True),
                    Column('age', Integer, nullable=False),
                    Column('email', String(60), nullable=False),
                    Column('password', String(300)),
                   # Column('grupo_usuario', ForeignKey('grupo_usuario.id')),
                    Column('grupo_usuario', Integer),
                    Column('created_at', DateTime, default=datetime.now),
                    Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now))

class Usuario(BaseModel):
    name: str
    age: int
    email: str
    password: str
    grupo_usuario: int

class UsuarioLogin(BaseModel):
    email: str
    password: str