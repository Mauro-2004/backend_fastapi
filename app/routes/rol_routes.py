from fastapi import APIRouter, HTTPException, Depends
from app.controllers.rol_controller import *
from app.models.rol_model import Rol

router = APIRouter()

def get_rol_controller():
    return RolController()

@router.post("/create_rol")
async def create_rol(rol: Rol, rol_controller: RolController = Depends(get_rol_controller)):
    try:
        rpta = rol_controller.create_rol(rol)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_rol/{rol_id}", response_model=Rol)
async def get_rol(rol_id: int, rol_controller: RolController = Depends(get_rol_controller)):
    try:
        rpta = rol_controller.get_rol(rol_id)
        if not rpta:
            raise HTTPException(status_code=404, detail="Rol not found")
        return rpta
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_roles/")
async def get_roles(rol_controller: RolController = Depends(get_rol_controller)):
    try:
        rpta = rol_controller.get_roles()
        return rpta
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete_rol/{rol_id}")
async def delete_rol(rol_id: int, rol_controller: RolController = Depends(get_rol_controller)):
    try:
        rpta = rol_controller.delete_rol(rol_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update_rol/{rol_id}")
async def update_rol(rol_id: int, rol: Rol, rol_controller: RolController = Depends(get_rol_controller)):
    try:
        rpta = rol_controller.update_rol(rol_id, rol)
        if not rpta:
            raise HTTPException(status_code=404, detail="Rol no encontrado o no se realizaron cambios")
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))