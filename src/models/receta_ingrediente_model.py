from src.database.database import get_connection

class ingrediente_recetaModel:

    @classmethod
    def md_obtener_receta_ingrediente_id(cls, id_receta):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = "SELECT id_receta_ingrediente, cantidad_ingrediente, ingredientes.nombre_ingrediente, unidades_medidas.nombre_unidad_medida FROM receta_ingrediente, ingredientes, unidades_medidas WHERE receta_ingrediente.id_receta=%s AND receta_ingrediente.id_ingrediente = ingredientes.id_ingrediente AND receta_ingrediente.id_unidad_medida = unidades_medidas.id_unidad_medida"
                cursor.execute(sql, (id_receta,))
                return cursor.fetchall()
        except Exception as ex:
            print(ex)
            return False

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
            