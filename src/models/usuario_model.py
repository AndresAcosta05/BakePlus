from src.database.database import get_connection

class ModelUsuario:

    @classmethod
    def md_login_usuario(cls, user):
        with get_connection().cursor() as cursor:
            sql = "SELECT id_usuario, nombre_usuario, apellido_usuario, email_usuario FROM usuarios WHERE email_usuario=%s AND password_usuario=%s"
            cursor.execute(sql, (user['usuario'], str(user['contraseña'])))
            response = cursor.fetchone()
            return response