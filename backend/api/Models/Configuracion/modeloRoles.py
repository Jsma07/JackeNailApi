from sqlalchemy import create_engine
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# Esta es tu tabla de asociación
permisos_roles = Table('permisos_roles', Base.metadata,
    Column('permisoId', Integer, ForeignKey('permisos.idPermiso')),
    Column('rolId', Integer, ForeignKey('roles.idRol'))
)

class Permiso(Base):
    __tablename__ = 'permisos'
    idPermiso= Column(Integer, primary_key= True)
    nombre= Column(String(50))

class Rol(Base):
    __tablename__ = "roles"
    idRol = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30))
    # primer parametro: clase, segundo: relacion de muchos a muchos y se pasa la tabla de asociacion, tercero: Esto crea una referencia inversa en la clase Permiso llamada roles
    # Esto significa que puedes acceder a todos los roles asociados con un permiso a través del atributo roles
    permisos = relationship('Permiso', secondary=permisos_roles, backref='roles')
    # Esta línea establece la relación inversa con la tabla 'usuarios', como primer parametro se pone la clase y como segundo la tabla
    usuarios = relationship("Usuario", back_populates="rol")

# Crear el motor de la base de datos
engine = create_engine('mysql+pymysql://root:@localhost/JackeNail1')

# Crear todas las tablas en la base de datos
Base.metadata.create_all(engine)

