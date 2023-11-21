from src.models.ingrediente_model import ingredienteModel

class ingredienteController:

    @classmethod
    def cr_obtener_ingredientes(cls):
        response = ingredienteModel().md_obtener_ingredientes()
        return response