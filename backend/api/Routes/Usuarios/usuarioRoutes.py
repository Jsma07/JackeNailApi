from fastapi import APIRouter
from Schema.Usuarios.SchemaUsuarios import Usuario
from controllers.UsuariosControlador import UsuarioControlador

usuarioControlador = UsuarioControlador()

router = APIRouter()

@router.post("/Usuarios/crearUsuario", response_model=Usuario)
def crearUsuario(usuario: Usuario):
    return usuarioControlador.crearUsuario(usuario)

@router.get("/Usuario/{usuarioId}")
def listarUsuario(usuarioId: int):
    return usuarioControlador.listarUsuario(usuarioId)

@router.put("/Usuarios/actualizarUsuario/{usuarioId}")
def actualizarUsuario(usuarioId: int, usuario: Usuario):
    return usuarioControlador.actualizarUsuario(usuarioId, usuario)

@router.delete("/Usuarios/eliminarUsuario/{usuarioId}")
def eliminarUsuario(usuarioId: int):
    return usuarioControlador.eliminarUsuario(usuarioId)