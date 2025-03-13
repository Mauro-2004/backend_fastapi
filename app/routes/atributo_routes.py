from fastapi import APIRouter, HTTPException
from app.models.atributo_model import Atributo
from app.controllers.atributo_controller import *

router = APIRouter()
atributo_controller = AtributoController()

@router.post("/atributos/")
def create_atributo(atributo: Atributo):
    return atributo_controller.create_atributo(atributo)

@router.get("/atributos/{atributo_id}")
def get_atributo(atributo_id: int):
    return atributo_controller.get_atributo(atributo_id)

@router.get("/atributos/")
def get_atributos():
    return atributo_controller.get_atributos()

@router.put("/atributos/{atributo_id}")
def update_atributo(atributo_id: int, atributo: Atributo):
    return atributo_controller.update_atributo(atributo_id, atributo)

@router.delete("/atributos/{atributo_id}")
def delete_atributo(atributo_id: int):
    return atributo_controller.delete_atributo(atributo_id)
