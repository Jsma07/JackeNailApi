from fastapi import HTTPException
from sqlalchemy.orm import Session
from conexion import SessionLocal
from Models.Usuarios.modeloUsuarios import Permiso

class PermisoControlador: 
    def __init__(self):
        self.db = SessionLocal()

    def crearPermiso(self, permiso: Permiso):
        db_permiso = self.db.query(Permiso).filter(Permiso.nombre == permiso.nombre).first()
        if db_permiso:
            raise HTTPException(status_code=400, detail="Permiso existente")
        else:
            nuevo_permiso = Permiso(idPermiso=permiso.idPermiso, nombre=permiso.nombre)
            self.db.add(nuevo_permiso)
            self.db.commit()
            self.db.refresh(nuevo_permiso)
            return nuevo_permiso



    
    def listarPermiso(self, permisoId: int):
        db_permiso = self.db.query(Permiso).filter(Permiso.id == permisoId)
        if not db_permiso:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return db_permiso
    
    def actualizarPermiso(self, permisoId: int, permiso: Permiso):
        db_permiso = self.db.query(Permiso).filter(Permiso.id == permisoId).first()
        if not db_permiso:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        for key, value in permiso.dict().items():
            setattr(db_permiso, key, value)
        
        self.db.commit()
        return db_permiso

    def eliminarPermiso(self, permisoId: int):
        permiso = self.db.query(Permiso).filter(Permiso.id == permisoId).first()
        if not permiso:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        self.db.delete(permiso)
        self.db.commit()
