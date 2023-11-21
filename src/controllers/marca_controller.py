from src.models.marca_model import marcaModel

class marcaController:

    @classmethod
    def cr_obtener_marcas(cls):
        response = marcaModel().md_obtener_marcas()
        return response