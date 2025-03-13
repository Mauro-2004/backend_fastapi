from fastapi import APIRouter, HTTPException, Depends
from app.controllers.productos_controller import *
from app.models.productos_model import Productos

router = APIRouter()

def get_productos_controller():
    return ProductosController()


@router.post("/create_productos")
async def create_productos(productos: Productos, productos_controller: ProductosController = Depends(get_productos_controller)):
    try:
        return productos_controller.create_productos(productos)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_productos/{productos_id}")
async def get_productos(productos_id: int, productos_controller: ProductosController = Depends(get_productos_controller)):
    try:
        return ProductosController.get_productos(productos_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_productos")
async def get_productos(productos_controller: ProductosController = Depends(get_productos_controller)):
    try:
        return productos_controller.get_productos()
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete_productos/{productos_id}")
async def delete_productos(productos_id: int, productos_controller: ProductosController = Depends(get_productos_controller)):
    try:
        return productos_controller.delete_productos(productos_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update_productos/{productos_id}")
async def update_productos(productos_id: int, productos: Productos, productos_controller: ProductosController = Depends(get_productos_controller)):
    try:
        return productos_controller.update_productos(productos_id, productos)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
