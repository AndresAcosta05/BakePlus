from flask import Blueprint, jsonify
from flask_cors import cross_origin

produccion = Blueprint('produccions_blueprint', __name__)

@produccion.route('/')
@cross_origin()
def index_produccions():
    return jsonify('Bienvenido a produccions')