from flask import Flask

app = Flask(__name__)

def init_app(config):
    # PASAMOS LA CONFIGURACION
    app.config.from_object(config)
    # ESPACIO PARA RUTAS

    return app