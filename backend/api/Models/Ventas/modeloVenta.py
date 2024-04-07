from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from typing import List, Optional
from datetime import datetime

Base = declarative_base()

class Venta(Base):
    __tablename__ = 'ventas'
    idVenta = Column(Integer, primary_key=True)
    empleadoId = Column(Integer, ForeignKey('empleados.idEmpleado'))
    clienteId = Column(Integer, ForeignKey('clientes.idCliente'))
    servicioId = Column(Integer, ForeignKey('servicios.idServicio'))
    ivaVenta = Column(Float)
    subtotalVenta = Column(Float)
    descuentoVenta = Column(Float)
    horaServicio = Column(DateTime)
    precio = Column(Float)
    adicionesId = Column(String)  # Cambia el tipo según tus necesidades
    fechaVenta = Column(DateTime)
    estadoVenta = Column(Integer)
    salidaInsumoId = Column(Integer, ForeignKey('SalidaInsumo.idSalidaInsumo'))
    
    salida_insumo = relationship("SalidaInsumo", back_populates="venta")

class DetalleVenta(Base):
    __tablename__ = 'DetalleVenta'
    idDetalleVenta = Column(Integer, primary_key=True)
    ventaId = Column(Integer, ForeignKey('ventas.idVenta'))
    insumoId = Column(String)  # Cambia el tipo según tus necesidades
    precioUnitario = Column(Float)
    cantidadInsumo = Column(Integer)

    venta = relationship("Venta", back_populates="detalles")

class SalidaInsumo(Base):
    __tablename__ = 'SalidasInsumos'
    idSalidaInsumo = Column(Integer, primary_key=True)
    ventaId = Column(Integer, ForeignKey('ventas.idVenta'))
    insumoId = Column(String)  # Cambia el tipo según tus necesidades
    cantidadUtilizada = Column(Integer)
    fechaSalida = Column(DateTime)
    estadoSalida = Column(Integer)

    venta = relationship("Venta", uselist=False, back_populates="SalidaInsumo")

engine = create_engine('mysql+pymysql://root:@localhost/JackeNail1')
# Crear todas las tablas en la base de datos
Base.metadata.create_all(engine)
