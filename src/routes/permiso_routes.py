from flask import Blueprint, jsonify
from flask_cors import cross_origin

permiso = Blueprint('permisos_blueprint', __name__)

@permiso.route('/')
@cross_origin()
def index_permisos():
    return jsonify('Bienvenido a permisos')