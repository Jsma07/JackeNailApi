from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Servicio(BaseModel):
    idServicio: int
    nombreServicio: str
    precioServicio: float
    tiempoServicio: datetime
    imagenServicio: str
    tipoNivelId: int
    estadoServicio: int


class TipoNivel(BaseModel):
    idTipoNivel: int
    servicioId: int
    numero: int
    precioNivel: float

class Insumo(BaseModel):
    idInsumo: int
    nombreInsumo:str
    imagenInsumo: str
    cantidadInsumo: int
    usosDisponibles: int
    categoriaId: int
    estadoInsumo: int

class Categoria(BaseModel):
    idCategoria: int
    nombreCategoria: int
