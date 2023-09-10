import pymysql
from decouple import config

def get_connection():
    try:
        return pymysql.connect(
            host= config('MYSQL_HOST'),
            user= config('MYSQL_USER'),
            password= config('MYSQL_PASSWORD'),
            db= config('MYSQL_DATABASE')
        )
    except Exception as e:
        print(e)