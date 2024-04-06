from fastapi import HTTPException
from sqlalchemy.orm import Session
from conexion import SessionLocal
from Models.Usuarios.modeloUsuarios import Usuario

class UsuarioControlador: 
    def __init__(self):
        self.db = SessionLocal()

    def crearUsuario(self, usuario: Usuario):
        if usuario is None:
            raise ValueError("El usuario no puede ser None")
        db_usuario = self.db.query(Usuario).filter(Usuario.correo == usuario.correo).first()
        if db_usuario:
            raise HTTPException(status_code=400, detail="Usuario existente")
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario


    
    def listarUsuario(self, usuarioId: int):
        db_usuario = self.db.query(Usuario).filter(Usuario.id == usuarioId)
        if not db_usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return db_usuario
    
    def actualizarUsuario(self, usuarioId: int, usuario: Usuario):
        db_usuario = self.db.query(Usuario).filter(Usuario.id == usuarioId).first()
        if not db_usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        for key, value in usuario.dict().items():
            setattr(db_usuario, key, value)
        
        self.db.commit()
        return db_usuario

    def eliminarUsuario(self, usuarioId: int):
        usuario = self.db.query(Usuario).filter(Usuario.id == usuarioId).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        self.db.delete(usuario)
        self.db.commit()
