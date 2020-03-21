# hypercorn uvicorn main:app --reload
# docker run --name t10 -e POSTGRES_PASSWORD=123 -d -p 5432:5432 postgres
# ou
# docker start t10
# docker exec -it t10 bash
# psql -U postgres
# CREATE DATABASE t10db;

# -------------------------------------------------------

from fastapi import FastAPI
from models.models import *
from database import metadata

metadata.create_all()

app = FastAPI()

@app.get("/user/create")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}