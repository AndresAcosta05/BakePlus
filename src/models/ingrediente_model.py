from src.database.database import get_connection

class ingredienteModel:

    @classmethod
    def md_obtener_ingredientes(cls):
        with get_connection().cursor() as cursor:
            sql = 'SELECT id_ingrediente, nombre_ingrediente, fecha_vencimiento_ingrediente FROM ingredientes WHERE estado_rg = 1'
            cursor.execute(sql)
            ingredientes = cursor.fetchall()
            return ingredientes