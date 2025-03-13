from pydantic import BaseModel

class Atributoxusuario (BaseModel):
    id: int = None
    idusuario: int
    idatriduto: int
    valor: str
    descripcion: str
