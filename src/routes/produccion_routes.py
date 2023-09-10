from flask import Blueprint, jsonify

produccion = Blueprint('produccions_blueprint', __name__)

@produccion.route('/')
def index_produccions():
    return jsonify('Bienvenido a produccions')