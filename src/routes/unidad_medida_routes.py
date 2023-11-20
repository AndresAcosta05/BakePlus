from flask import Blueprint, jsonify
from flask_cors import cross_origin

unidad_medida = Blueprint('unidad_medidas_blueprint', __name__)

@unidad_medida.route('/')
@cross_origin()
def index_unidad_medidas():
    return jsonify('Bienvenido a unidad_medidas')