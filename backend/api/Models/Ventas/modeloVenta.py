from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class SalidaInsumo(BaseModel):
    idSalidaInsumo: int
    ventaId: int
    insumoId: List[int]
    cantidadUtilizada: int
    fechaSalida: datetime
    estadoSalida: int

class Venta(BaseModel):
    idVenta: int
    empleadoId:int
    clienteId:int
    servicioId: int
    ivaVenta: float
    subtotalVenta: float
    descuentoVenta: float
    horaServicio: datetime
    precio: float
    adicionesId: Optional[List[int]] = []
    fechaVenta: datetime
    salidaInsumo: Optional[SalidaInsumo] = None
    estadoVenta:int
    
class DetalleVenta(BaseModel):
    idDetalle: int
    VentaId: int
    insumoId:List[int]
    precioUnitario: float
    cantidadInsumo: int
    

