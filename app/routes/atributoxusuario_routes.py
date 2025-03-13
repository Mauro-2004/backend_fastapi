from fastapi import APIRouter, HTTPException
from app.models.atributoxusuario_model import Atributoxusuario
from app.controllers.atributoxusuario_controller import AtributoxusuarioController

router = APIRouter()
atributoxusuario_controller = AtributoxusuarioController()

@router.post("/atributoxusuarios/")
def create_atributoxusuario(atributoxusuario: Atributoxusuario):
    return atributoxusuario_controller.create_atributoxusuario(atributoxusuario)

@router.get("/atributoxusuarios/{atributoxusuario_id}")
def get_atributoxusuario(atributoxusuario_id: int):
    return atributoxusuario_controller.get_atributoxusuario(atributoxusuario_id)

@router.get("/atributoxusuarios/")
def get_atributoxusuarios():
    return atributoxusuario_controller.get_atributoxusuarios()

@router.put("/atributoxusuarios/{atributoxusuario_id}")
def update_atributoxusuario(atributoxusuario_id: int, atributoxusuario: Atributoxusuario):
    return atributoxusuario_controller.update_atributoxusuario(atributoxusuario_id, atributoxusuario)

@router.delete("/atributoxusuarios/{atributoxusuario_id}")
def delete_atributoxusuario(atributoxusuario_id: int):
    return atributoxusuario_controller.delete_atributoxusuario(atributoxusuario_id)
