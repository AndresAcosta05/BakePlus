from decouple import config
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
                'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(hours=1),
                'user_name': authenticated_user.name,
                'user': authenticated_user.user
            }

            return jwt.encode(payload, cls.secret, algorithm='HS256')
        
        except Exception as ex:
            print(ex)
    

    @classmethod
    def verify_token(cls, headers):
        try:
            if 'Authorization' in headers.keys():
                authorization = headers['Authorization']
                encoded_token = authorization.split(" ")[1]

                try:
                    payload = jwt.decode(encoded_token, cls.secret, algorithms=['HS256'])
                    return True
                
                except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                    return False
        
        except Exception as ex:
            print(ex)