from src.models.receta_model import recetaModel
from src.controllers.receta_ingrediente_controller import receta_ingredienteController

class recetaController:

    @classmethod
    def cr_obtener_recetas(cls):
        recetas = recetaModel().md_obtener_recetas()
        return recetas
    
    @classmethod
    def cr_obtener_receta_id(cls, id):
        receta = recetaModel().md_obtener_receta_id(id=id)
        ingredientes_receta = receta_ingredienteController().cr_obtener_receta_ingrediente_id(id_receta=id)
        
        full_receta = {
            'nombre_receta': receta[0],
            'cantidad_receta': receta[1],
            'descripcion_receta': receta[2],
            'receta_ingrediente': []
        }

        for ingrediente in ingredientes_receta:
            full_receta['receta_ingrediente'].append({
                'ingrediente': ingrediente[1],
                'cantidad_ingrediente': ingrediente[2],
                'unidad_medida': ingrediente[3]
            })
        return full_receta

    @classmethod
    def insertar_receta(cls, receta):
        for value in receta.values():
            # validamos que ningun campo venga vacion
            if not value:
                return False
        # validamos que tenga valores para ingredientes de la receta y que sea al menos 1
        if 'receta_ingrediente' in receta and len(receta['receta_ingrediente'])>=1:
            id_receta = recetaModel.md_insertar_receta(receta=receta, need_id=True)
            if id_receta:
                for receta_ingrediente in receta['receta_ingrediente']:
                    response_ingrediente = receta_ingredienteController().cr_insertar_receta_ingrediente(id_receta=id_receta, receta_ingrediente=receta_ingrediente)
                    if response_ingrediente == False:
                        return False
                # al cumplir correctamente todo retornara verdadero
                return True
        # en caso de no cumplir alguna indicacion llegara a retornar falso
        return False