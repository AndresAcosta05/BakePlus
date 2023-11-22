from src.database.database import get_connection

class recetaModel:

    @classmethod
    def md_obtener_recetas(cls):
        try:
            with get_connection().cursor() as cursor:
                sql = "SELECT id_receta, nombre_receta, cantidad_receta, descripcion_receta FROM recetas WHERE estado_rg=1"
                cursor.execute(sql)
                return cursor.fetchall()
        
        except Exception as ex:
            print(ex)
            return False
    
    @classmethod
    def md_obtener_receta_id(cls, id):
        try:
            with get_connection().cursor() as cursor:
                sql = "SELECT nombre_receta, cantidad_receta, descripcion_receta FROM recetas WHERE id_receta=%s AND estado_rg=1"
                cursor.execute(sql, (int(id),))
                return cursor.fetchone()
        
        except Exception as ex:
            print(ex)
            return False

    @classmethod
    def md_insertar_receta(cls, receta, need_id=False):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = "INSERT INTO recetas(nombre_receta, cantidad_receta, descripcion_receta) VALUES (%s, %s, %s) returning id_receta"
                cursor.execute(sql, (receta['nombre_receta'], receta['cantidad_receta'], receta['descripcion_receta']))
                connection.commit()
                id_receta = cursor.fetchone()
                return id_receta if need_id else True
        
        except Exception as ex:
            print(ex)
            return False
