from pydantic import BaseModel

class Order(BaseModel):
    id_order: int = None
    user_nombre: str
    estado:int
