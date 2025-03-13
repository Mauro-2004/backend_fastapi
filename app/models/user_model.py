from pydantic import BaseModel

class User(BaseModel):
    id: int = None
    nombre: str
    apellido: str
    documento: str
    telefono: str
    email: str
    password: str
    id_rol: int
    id_producto: int
    estado:int

class Login(BaseModel):
    nombre: str
    password: str    