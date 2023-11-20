from flask import Blueprint, jsonify
from flask_cors import cross_origin

receta = Blueprint('recetas_blueprint', __name__)

@receta.route('/')
@cross_origin()
def index_recetas():
    return jsonify('Bienvenido a recetas')