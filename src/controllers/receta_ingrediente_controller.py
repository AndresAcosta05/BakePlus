from src.models.receta_ingrediente_model import ingrediente_recetaModel

class receta_ingredienteController:

    @classmethod
    def cr_insertar_receta_ingrediente(cls, id_receta, receta_ingrediente):
        for value in receta_ingrediente.values():
            # validamos que ningun campo venga vacion
            if not value:
                return False
        response = ingrediente_recetaModel().md_insertar_receta_ingrediente(id_receta= id_receta, receta_ingrediente=receta_ingrediente)
        return response