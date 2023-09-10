from flask import Blueprint, jsonify

receta = Blueprint('recetas_blueprint', __name__)

@receta.route('/')
def index_recetas():
    return jsonify('Bienvenido a recetas')