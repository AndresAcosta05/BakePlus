from flask import session
from src.models.usuario_model import ModelUsuario
from src.utils.security import Security

class ControladorUsuario:

    @classmethod
    def login(cls, user):
        
        #primero validamos si existe un token y que ademas sea valido
        if 'token' in session and Security.verify_token(token=session['token']):
            return session, 200
        
        # en caso de no tener un token y usuario procedemos a crear un token y devolver la data correspondiente
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
            session['token'] = token
        return response, 200