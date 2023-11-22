from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from src.controllers.receta_ingrediente_controller import receta_ingredienteController

receta_ingrediente = Blueprint('receta_ingredientes_blueprint', __name__)

@receta_ingrediente.route('/')
@cross_origin()
def index_receta_ingredientes():
    return jsonify('Bienvenido a receta_ingredientes')

@receta_ingrediente.route('/insert')
@cross_origin()
def insertar_receta():
    if request.method == 'POST':
        receta_ingrediente = request.json
        response = receta_ingredienteController.cr_insertar_receta_ingrediente(receta_ingrediente=receta_ingrediente)
        return response