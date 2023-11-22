from src.database.database import get_connection

class ingrediente_recetaModel:

    @classmethod
    def md_insertar_receta_ingrediente(cls, id_receta, receta_ingrediente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = "INSERT INTO receta_ingrediente(id_receta, id_ingrediente, id_unidad_medida, cantidad_ingrediente) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (id_receta, int(receta_ingrediente['id_ingrediente']), int(receta_ingrediente['id_unidad_medida']), int(receta_ingrediente['cantidad_ingrediente'])))
                connection.commit()
                return True
        except Exception as ex:
            return False
            