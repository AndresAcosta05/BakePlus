from src.models.usuario_model import ModelUsuario
from src.utils.security import Security

class ControladorUsuario:

    @classmethod
    def login(cls, user):
        response = ModelUsuario.md_login_usuario(user=user)
        # modificamos la respuesta para enviar el token
        if response:
            authenticated_user = {
                'nombre_usuario': f'{response[1]} {response[2]}',
                'usuario': response[3]
            }
            token = Security.generateToken(authenticated_user= authenticated_user)
            # modificamos la respuesta
            response = authenticated_user
            response['token'] = token
        return response