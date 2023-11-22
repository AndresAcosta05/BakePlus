from flask import Blueprint, jsonify
from flask_cors import cross_origin
from src.controllers.marca_controller import marcaController

marca = Blueprint('marcas_blueprint', __name__)

@marca.route('/')
@cross_origin()
def index_marcas():
    return jsonify('Bienvenido a marcas')

@marca.route('/getAll')
@cross_origin()
def obtener_marcas():
    response = marcaController().cr_obtener_marcas()
    return jsonify(response)