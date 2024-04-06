from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Agendamiento(BaseModel):
    idAgenda: int
    clienteId: int
    servicioId: int
    empleadoId: int
    fechaAgenda: datetime
    tipoNivelId: int
    estadoAgenda: int

class TipoNivel(BaseModel):
    idTipoNivel: int
    servicioId: int
    numero: int
    precioNivel: float
