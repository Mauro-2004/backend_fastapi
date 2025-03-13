from pydantic import BaseModel

class Productos(BaseModel):
    id_productos: int = None
    nombre: str
    fecha:int
    descripcion: str
    estado_alquiler: int
    estado:int
    fecha_creacion:int
   
  
