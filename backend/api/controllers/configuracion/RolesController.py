from fastapi import HTTPException
from sqlalchemy.orm import Session
from conexion import SessionLocal
from Models.Usuarios.modeloUsuarios import Rol
from Models.Usuarios.modeloUsuarios import Permiso

class RolControlador: 
    def __init__(self):
        self.db = SessionLocal()

    def crearRol(self, rol: Rol):
        db_rol = self.db.query(Rol).filter(Rol.nombre == rol.nombre).first()
        if db_rol:
            raise HTTPException(status_code=400, detail="Rol existente")
        else:
            permisos = self.db.query(Permiso).filter(Permiso.idPermiso.in_(rol.permisos)).all()
            nuevo_rol = Rol(idRol=rol.idRol, nombre=rol.nombre, permisos=permisos)
            self.db.add(nuevo_rol)
            self.db.commit()
            self.db.refresh(nuevo_rol)
        return nuevo_rol




    
    def listarRol(self, rolId: int):
        db_rol = self.db.query(Rol).filter(Rol.id == rolId)
        if not db_rol:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return db_rol
    
    def actualizarRol(self, rolId: int, rol: Rol):
        db_rol = self.db.query(Rol).filter(Rol.id == rolId).first()
        if not db_rol:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        for key, value in rol.dict().items():
            setattr(db_rol, key, value)
        
        self.db.commit()
        return db_rol

    def eliminarRol(self, rolId: int):
        rol = self.db.query(Rol).filter(Rol.id == rolId).first()
        if not rol:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        self.db.delete(rol)
        self.db.commit()
