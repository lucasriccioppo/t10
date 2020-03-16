from datetime import datetime
from sqlalchemy import (Column, Table, Integer, String, DateTime)
from database import metadata

cliente_table = Table( 'clientes', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('name', String(40), index=True),
                        Column('cnpj', String, nullable=False),
                        Column('created_at', DateTime, default=datetime.now),
                        Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now))