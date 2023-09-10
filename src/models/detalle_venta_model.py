class detalleVenta:

    def __init__(self, id_detalle, id_venta, id_producto, precio_unitario, precio_total, estado_rg, fecha_rg, fecha_md) -> None:
        self.id_detalle = id_detalle
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.precio_unitario = precio_unitario
        self.precio_total = precio_total
        self.estado_rg = estado_rg
        self.fecha_rg = fecha_rg
        self.fecha_md = fecha_md