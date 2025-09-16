from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.venta_model import Venta
from app.models.venta_detalle_model import DetalleVenta
from app.schemas.venta_schema import VentaCreate, VentaResponse
from app.schemas.venta_detail_schema import DetalleVentaCreate

class VentasService:

    @staticmethod
    def get_ventas(db: Session) -> list[VentaResponse]:
        """
        Obtiene todas las ventas de la base de datos.
        """
        return db.query(Venta).all()

    @staticmethod
    def get_venta(db: Session, venta_id: int) -> VentaResponse:
        """
        Obtiene una venta por su ID.
        """
        venta = db.query(Venta).filter(Venta.id == venta_id).first()
        if not venta:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venta no encontrada")
        return venta

    @staticmethod
    def update_venta(db: Session, venta_id: int, venta_data: VentaCreate) -> VentaResponse:
        """
        Actualiza una venta existente y sus detalles.
        """
        venta = db.query(Venta).filter(Venta.id == venta_id).first()
        if not venta:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venta no encontrada")

        venta.cliente_id = venta_data.cliente_id
        venta.total = venta_data.total

        # Actualizar detalles de ventas
        db.query(DetalleVenta).filter(DetalleVenta.venta_id == venta_id).delete()
        for detalle_data in venta_data.detalles:
            detalle = DetalleVenta(
                venta_id=venta_id,
                producto_id=detalle_data.producto_id,
                cantidad=detalle_data.cantidad,
                precio_unitario=detalle_data.precio_unitario
            )
            db.add(detalle)

        db.commit()
        db.refresh(venta)
        return venta

    @staticmethod
    def delete_venta(db: Session, venta_id: int) -> None:
        """
        Elimina una venta y sus detalles asociados.
        """
        venta = db.query(Venta).filter(Venta.id == venta_id).first()
        if not venta:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venta no encontrada")

        db.delete(venta)
        db.commit()
        return  true
