from sqlalchemy import (create_engine, MetaData)

engine = create_engine('sqlite:///teste.db', echo=True)

metadata = MetaData(bind=engine)