from datetime import datetime
from sqlalchemy import (Column, Table, Integer, String, DateTime, Float)
from database import metadata
from pydantic import BaseModel

produto_table = Table( 'produtos', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('name', String(40), index=True),
                        Column('codigo', Integer, nullable=False),
                        Column('value', Float),
                        Column('created_at', DateTime, default=datetime.now),
                        Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now))

class Produto(BaseModel):
    name: str
    codigo: int
    value: float