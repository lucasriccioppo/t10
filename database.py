from sqlalchemy import (create_engine, MetaData)

#engine = create_engine('sqlite:///teste.db', echo=True)
engine = create_engine('postgresql://postgres:123@localhost:5432/t10db', echo=True)

metadata = MetaData(bind=engine)