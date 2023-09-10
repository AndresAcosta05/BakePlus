from flask import Blueprint, jsonify

receta_ingrediente = Blueprint('receta_ingredientes_blueprint', __name__)

@receta_ingrediente.route('/')
def index_receta_ingredientes():
    return jsonify('Bienvenido a receta_ingredientes')