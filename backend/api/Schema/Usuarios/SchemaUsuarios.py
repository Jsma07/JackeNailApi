# schemas.py
from pydantic import BaseModel, Field
from typing import List


class Usuario(BaseModel):
    id: int
    nombre: str
    apellido: str
    correo: str
    telefono: str
    contrasena: str
    rolId: int
    estado: int

class Permiso(BaseModel):
    idPermiso: int 
    nombre: str


class Rol(BaseModel):
    idRol: int 
    nombre: str
    permisos: List[int]





class Cliente(Usuario):
    pass

class Empleado(Usuario):
    pass

class Administrador(Usuario):
    pass
