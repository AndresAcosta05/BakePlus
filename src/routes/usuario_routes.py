from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from src.controllers.usuario_controller import ControladorUsuario


usuario = Blueprint('usuarios_blueprint', __name__)

# RUTA PARA LOGIN
@usuario.route('/login', methods=['POST'])
@cross_origin()
def usuario_login():
    if request.method == 'POST':
        user = request.json
        if 'usuario' and 'contraseña' in user:
            response = ControladorUsuario.login(user=user)
            return jsonify(response)
        else:
            return jsonify(False)

# RUTA PARA INSERTAR NUEVO
@usuario.route('/insertar', methods=['POST'])
@cross_origin()
def insertar_usuario():
    if request.method == 'POST':
        usuario = request.json
        if usuario:
            response = ControladorUsuario.cr_insertar_usuario(usuario=usuario)
            return jsonify(response)
        else:
            return jsonify(False)
        