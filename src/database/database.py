import psycopg2
from decouple import config

def get_connection():
    try:
        return psycopg2.connect(
            host = config('HOST'),
            user = config('USER'),
            password = config('PASSWORD'),
            database = config('DATABASE')
        )
    except Exception as e:
        print(e)