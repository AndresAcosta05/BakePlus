from src.models.unidad_medida_model import unidadModel

class unidadController:

    @classmethod
    def obtener_unidades_medida(cls):
        response = unidadModel().md_obtener_unidades_medida()
        return response