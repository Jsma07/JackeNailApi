from fastapi import HTTPException
from Models.Compras.modeloCompras import Compra

class CompraControlador: 
    def __init__(self):
        self.compras = {}

    def crearCompra(self, compra: Compra):
        if compra.id in self.compras:
            raise HTTPException(status_code=400, detail="Compra existente")
        self.compras[compra.id] = compra
        return compra
    
    def listarCompra(self, compraId: int):
        if compraId not in self.compras:
            raise HTTPException(status_code=404, detail="compra no encontrado")
        return self.compras[compraId]
    
    def actualizarCompra(self, compraId: int, compra: Compra):
        if compraId not in self.compras:
            raise HTTPException(status_code=404, detail="Compra no encontrado")
        self.compras[compraId] = compra
        return compra

    def eliminarCompra(self, compraId: int):
        if compraId not in self.compras:
            raise HTTPException(status_code=404, detail="Compra no encontrado")
        del self.compras[compraId]
