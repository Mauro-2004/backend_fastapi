from pydantic import BaseModel

class User(BaseModel):
    id_usuario: int = None
    nombre: str
    email: str
    telefono: str
    direccion: str
    tipo_usuario: str
    contraseña: str
    fecha_registro: str
    id_rol: int

class Login(BaseModel):
    nombre: str
    contraseña: str    