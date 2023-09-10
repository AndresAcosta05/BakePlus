from flask import Blueprint, jsonify

ingrediente = Blueprint('ingredientes_blueprint', __name__)

@ingrediente.route('/')
def index_ingredientes():
    return jsonify('Bienvenido a ingredientes')