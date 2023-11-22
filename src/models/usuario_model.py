from src.database.database import get_connection

class ModelUsuario:

    @classmethod
    def md_login_usuario(cls, user):
        with get_connection().cursor() as cursor:
            sql = "SELECT id_usuario, nombre_usuario, apellido_usuario, email_usuario FROM usuarios WHERE email_usuario=%s AND password_usuario=%s"
            cursor.execute(sql, (user['usuario'], str(user['contraseña'])))
            usuario = cursor.fetchone()
            return usuario
    
    @classmethod
    def md_obtener_usuario(cls, user):
        with get_connection().cursor() as cursor:
            sql = "SELECT id_usuario, nombre_usuario, apellido_usuario, email_usuario FROM usuarios WHERE email_usuario=%s"
            cursor.execute(sql)
            usuario = cursor.fetchone()
            return usuario
    
    @classmethod
    def md_insertar_usuario(cls, user):
        connection = get_connection()
        with connection.cursor() as cursor:
            try:
                sql = "INSERT INTO usuarios(id_rol, id_tipo_documento, doc_usuario, password_usuario, nombre_usuario, apellido_usuario, telefono_usuario, email_usuario) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (int(user['id_rol']), int(user['id_tipo_documento']), user['doc_usuario'], user['password_usuario'], user['nombre_usuario'], user['apellido_usuario'], user['telefono_usuario'], user['email_usuario']))
                connection.commit()
                return True
            
            except Exception as ex:
                print(ex)
                return False
                
        