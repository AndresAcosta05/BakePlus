from flask import Blueprint, jsonify

usuario = Blueprint('usuarios_blueprint', __name__)

@usuario.route('/')
def index_usuarios():
    return jsonify('Bienvenido a usuarios')