from datetime import datetime
from sqlalchemy import (Column, Table, Integer, String, DateTime, Float)
from database import metadata

produto_table = Table( 'produtos', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('name', String(40), index=True),
                        Column('codigo', Integer, nullable=False),
                        Column('value', Float),
                        Column('created_at', DateTime, default=datetime.now),
                        Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now))