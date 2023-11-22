from flask import Blueprint, jsonify
from flask_cors import cross_origin
from src.controllers.unidad_medida_controller import unidadController

unidad_medida = Blueprint('unidad_medidas_blueprint', __name__)

@unidad_medida.route('/')
@cross_origin()
def index_unidad_medidas():
    return jsonify('Bienvenido a unidad_medidas')

@unidad_medida.route('/getAll')
@cross_origin()
def obtener_unidades_medidas():
    unidades = unidadController().obtener_unidades_medida()
    return jsonify(unidades)