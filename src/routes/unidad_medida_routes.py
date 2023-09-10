from flask import Blueprint, jsonify

unidad_medida = Blueprint('unidad_medidas_blueprint', __name__)

@unidad_medida.route('/')
def index_unidad_medidas():
    return jsonify('Bienvenido a unidad_medidas')