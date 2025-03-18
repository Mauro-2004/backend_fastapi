from pydantic import BaseModel

class User(BaseModel):
    id_usuario: int = None
    nombre: str
    email: str
    telefono: str
    direccion: str
    tipo_usuario: str
    contraseña: str
    id_rol: int
    estado: int

class Login(BaseModel):
    email: str
    contraseña: str    
    id_rol: int
    estado: bool