from fastapi import APIRouter
from Schema.Usuarios.SchemaUsuarios import Rol, Permiso
from controllers.configuracion.RolesController import RolControlador



rolControlador = RolControlador()

router = APIRouter()

@router.post("/Rol/crearRol", response_model=Rol)
def crearRol(rol: Rol):
    return rolControlador.crearRol(rol)

@router.get("/Rol/{IdRol}")
def listarRol(rolId: int):
    return rolControlador.listarRol(rolId)

@router.put("/Rol/actualizarRol/{IdRol}")
def actualizarRol(rolId: int, rol: Rol):
    return rolControlador.actualizarRol(rolId, rol)

@router.delete("/Rol/eliminarRol/{IdRol}")
def eliminarRol(rolId: int):
    return rolControlador.eliminarRol(rolId)



