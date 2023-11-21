from src.database.database import get_connection

class marcaModel:

    @classmethod
    def md_obtener_marcas(cls):
        with get_connection().cursor() as cursor:
            sql = 'SELECT * FROM marcas WHERE estado_rg=1'
            cursor.execute(sql)
            marcas = cursor.fetchall()

            return marcas