from fastapi import APIRouter
from Schema.Usuarios.SchemaUsuarios import  Permiso
from controllers.configuracion.PermisosController import PermisoControlador


permisoControlador = PermisoControlador()

router = APIRouter()

@router.post("/Permiso/crearPermiso", response_model=Permiso)
def crearRol(permiso: Permiso):
    return permisoControlador.crearPermiso(permiso)

@router.get("/Permiso/{IdPermiso}")
def listarRol(permisoId: int):
    return permisoControlador.listarPermiso(permisoId)

@router.put("/Permiso/actualizarPermiso/{IdPermiso}")
def actualizarRol(permisoId: int, permiso: Permiso):
    return permisoControlador.actualizarPermiso(permisoId, permiso)

@router.delete("/Permiso/eliminarPermiso/{IdPermiso}")
def eliminarRol(permisoId: int):
    return permisoControlador.eliminarPermiso(permisoId)
