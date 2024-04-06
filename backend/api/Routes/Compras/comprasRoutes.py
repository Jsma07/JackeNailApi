from fastapi import APIRouter
from Models.Compras.modeloCompras import Compra
from controllers.Compras.comprasControllers import CompraControlador

compraControlador = CompraControlador()

router = APIRouter()

@router.post("/Compras/crearCompra", response_model=Compra)
def crearCompra(compra: Compra):
    return compraControlador.crearCompra(compra)

@router.get("/Compra/{compraId}")
def listarCompra(compraId: int):
    return compraControlador.listarCompra(compraId)

@router.put("/Compras/actualizarCompra/{compraId}")
def actualizarCompra(compraId: int, compra: Compra):
    return compraControlador.actualizarCompra(compraId, compra)

@router.delete("/Compras/eliminarCompra/{compraId}")
def eliminarCompra(compraId: int):
    return compraControlador.eliminarCompra(compraId)