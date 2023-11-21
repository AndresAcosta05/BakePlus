from flask import Blueprint, jsonify
from flask_cors import cross_origin
from src.controllers.ingrediente_controller import ingredienteController

ingrediente = Blueprint('ingredientes_blueprint', __name__)

@ingrediente.route('/')
@cross_origin()
def index_ingredientes():
    return jsonify('Bienvenido a ingredientes')

@ingrediente.route('/getAll')
def obtener_ingredientes():
    response = ingredienteController().cr_obtener_ingredientes()
    return jsonify({'ingredientes': response})