from decouple import config
from flask import session, jsonify
# UTILITIES
import datetime
import jwt
import pytz

class Security:

    secret = config('JWT_KEY')
    tz = pytz.timezone('America/Bogota')

    @classmethod
    def generateToken(cls, authenticated_user):
        try:
            payload = {
                'iat': datetime.datetime.now(tz= cls.tz),
                'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=6),
                'user_name': authenticated_user['nombre_usuario'],
                'user': authenticated_user['usuario']
            }

            return jwt.encode(payload, cls.secret, algorithm='HS256')
        
        except Exception as ex:
            print(ex)
            return False
    

    @classmethod
    def verify_token(cls, token):
        try:
            if token:
                try:
                    payload = jwt.decode(token, cls.secret, algorithms=['HS256'])
                    return True
                
                except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                    return False
        
        except Exception as ex:
            print(ex)
    
def validate_token(funcion):
    def funcion_decorada(*args, **kwargs):
        if 'token' in session:
            token = session['token']
            # validamos que el token sirva y sea valido
            if Security().verify_token(token=token):
                # si funciona detendremos la ejecucion de codigo
                return funcion(*args, **kwargs)

        return jsonify({'status': 401})
    return funcion_decorada
