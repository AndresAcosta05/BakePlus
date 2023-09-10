class recetaIngrediente:

    def __init__(self, id_receta_ingrediente, id_receta, id_ingrediente, id_unidad_medida, cantidad_ingrediente, estado_rg, fecha_rg, fecha_md) -> None:
        self.id_receta_ingrediente = id_receta_ingrediente
        self.id_receta = id_receta
        self.id_ingrediente = id_ingrediente
        self.id_unidad_medida = id_unidad_medida
        self.cantidad_ingrediente = cantidad_ingrediente
        self.estado_rg = estado_rg
        self.fecha_rg = fecha_rg
        self.fecha_md = fecha_md