from flask import Blueprint, jsonify
from flask_cors import cross_origin

receta_ingrediente = Blueprint('receta_ingredientes_blueprint', __name__)

@receta_ingrediente.route('/')
@cross_origin()
def index_receta_ingredientes():
    return jsonify('Bienvenido a receta_ingredientes')