# hypercorn uvicorn main:app --reload
# docker run --name t10 -e POSTGRES_PASSWORD=123 -d -p 5432:5432 postgres
# ou
# docker start t10
# docker exec -it t10 bash
# psql -U postgres
# CREATE DATABASE t10db;
# \c t10db -> connect to db
# -------------------------------------------------------

from fastapi import FastAPI
from models.models import *
from database import metadata
from controllers import usuario_controller

metadata.create_all()

app = FastAPI()

@app.post("/usuario/")
def create_item(usuario: Usuario):
    return usuario_controller.create_user(usuario)