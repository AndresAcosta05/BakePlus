from flask import Blueprint, jsonify

permiso = Blueprint('permisos_blueprint', __name__)

@permiso.route('/')
def index_permisos():
    return jsonify('Bienvenido a permisos')