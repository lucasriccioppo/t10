from datetime import datetime
from sqlalchemy import (Column, Table, Integer, String, DateTime)
from database import metadata

user_table = Table( 'usuarios', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(40), index=True),
                    Column('age', Integer, nullable=False),
                    Column('password', String),
                    Column('created_at', DateTime, default=datetime.now),
                    Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now))

metadata.create_all()
