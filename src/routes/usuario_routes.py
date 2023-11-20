from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from src.controllers.usuario_controller import ControladorUsuario


usuario = Blueprint('usuarios_blueprint', __name__)

@usuario.route('/')
@cross_origin()
def index_usuarios():
    return jsonify('Bienvenido a usuarios')

@usuario.route('/login', methods=['POST'])
@cross_origin()
def usuario_login():
    if request.method == 'POST':
        user = request.json
        if 'usuario' and 'contraseña' in user:
            response = ControladorUsuario.login(user=user)
            return jsonify({'response': response})
        else:
            return jsonify({'response': False})
        