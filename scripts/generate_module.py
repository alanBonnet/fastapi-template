import os
import sys


def generate_module(module_name: str):
    """
    ## Genera un modulo para el sistema:
    ### -> usando el comando:
    --> `python script/generate_module.py nombre_modulo`

    si estas en la terminal en la carpeta raiz del proyecto

    - ### app/api/endpoints/`module`.py

    - ### app/services/`module`.py

    - ### app/schemas/`module`.py

    - ### app/models/`module`.

    -

    #### Donde `module` como nombre es reemplazado por el parametro dado

    -  Como detalle:  Este modulo como tal debe ser agregado en `app/api/routers.py`
    """
    # * Capitalizado del nombre del modulo
    c_module_name = module_name.capitalize()
    # * Genera el archivo con su contenido en app/api/endpoints
    module_dir = os.path.join("app", "api", "endpoints")
    os.makedirs(module_dir, exist_ok=True)
    with open(os.path.join(module_dir, f"{module_name}.py"), "w") as f:
        f.write(
            f"""
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from app.schemas.{module_name} import {c_module_name},Show{c_module_name}, Update{c_module_name}
from app.services import {module_name}_service
# from app.db.database import get_db_
router = APIRouter()


@router.get("/", response_model= Show{c_module_name})
def obtener_{module_name}_listado(response: Response, db : Session = Depends(get_db_local)):
    {module_name}_list = {module_name}.list(db= db)
    return {module_name}_list


@router.get("/{{{module_name}_id}}", response_model= Show{c_module_name})
def obtener_un_{module_name}(response: Response, {module_name}_id: int, db : Session = Depends(get_db_local)):
    {module_name}_one = {module_name}.one(id={module_name}_id, db= db)
    return {module_name}_one


@router.post("/", response_model= Show{c_module_name})
def registrar_{module_name}(response: Response, {module_name}:{c_module_name}, db : Session = Depends(get_db_local)):
    {module_name}_create = {module_name}.create(body={module_name}, db= db)
    return {module_name}_create


@router.patch("/{{{module_name}_id}}", response_model= Show{c_module_name})
def editar_{module_name}(response: Response, {module_name}_id: int,{module_name}:{c_module_name}, db : Session = Depends(get_db_local)):
    {module_name}_update = {module_name}.update(body={module_name},id={module_name}_id, db= db)
    return {module_name}_update


@router.delete("/{{{module_name}_id}}", response_model= Show{c_module_name})
def eliminar_{module_name}(response: Response, {module_name}_id: int, db : Session = Depends(get_db_local)):
    {module_name}_delete = {module_name}.delete(id={module_name}_id, db= db)
    return {module_name}_delete
"""
        )

    # * Genera el archivo con su contenido en app/services
    service_dir = os.path.join("app", "services")
    os.makedirs(service_dir, exist_ok=True)
    with open(os.path.join(service_dir, f"{module_name}_service.py"), "w") as f:
        f.write(
            f"""
from app.models.{module_name} import {c_module_name} as {c_module_name}_DB
from fastapi import HTTPException, status
from app.schemas.{module_name} import {c_module_name}, Update{c_module_name}
from sqlalchemy.orm import Session
import sqlalchemy as sa

def list(db: Session):
    pass


def one(id:int, db: Session):
    pass


def create(body:{c_module_name}, db: Session):
    pass


def update(id:int,body:Update{c_module_name}, db: Session):
    pass


def delete(id:int, db: Session):
    pass
"""
        )

    # * Genera el archivo con su contenido en app/schemas
    schemas_dir = os.path.join("app", "schemas")
    os.makedirs(schemas_dir, exist_ok=True)
    with open(os.path.join(schemas_dir, f"{module_name}.py"), "w") as f:
        f.write(
            f"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class {c_module_name}(BaseModel):
    pass


class Update{c_module_name}(BaseModel):
    pass


class Show{c_module_name}(BaseModel):
    pass

    class Config:
        from_attributes = True

"""
        )
    # * Genera el archivo con su contenido en app/models
    models_dir = os.path.join("app", "models")
    os.makedirs(models_dir, exist_ok=True)
    with open(os.path.join(models_dir, f"{module_name}.py"), "w") as f:
        f.write(
            f"""
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from app.db.database import get_db, Base
from sqlalchemy.schema import ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship


class {c_module_name}(Base):
    __tablename__ = "{c_module_name}"
    id = Column(Integer, primary_key=True, autoincrement=True)
    isActive = Column(Boolean, default=True)
    createdAt = Column(DateTime, default=datetime.now())
    updatedAt = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

"""
        )

    print(f"Modulo {module_name} creado.")


if __name__ == "__main__":
    module_name = sys.argv[1]
    generate_module(module_name)
