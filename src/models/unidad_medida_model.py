from src.database.database import get_connection

class unidadModel:

    @classmethod
    def md_obtener_unidades_medida(cls):
        with get_connection().cursor() as cursor:
            sql = 'SELECT id_unidad_medida, abreviatura_unidad_medida, nombre_unidad_medida FROM unidades_medidas WHERE estado_rg=1'
            cursor.execute(sql)
            unidades = cursor.fetchall()
        return unidades
