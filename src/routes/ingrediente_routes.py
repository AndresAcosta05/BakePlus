from flask import Blueprint, jsonify
from flask_cors import cross_origin

ingrediente = Blueprint('ingredientes_blueprint', __name__)

@ingrediente.route('/')
@cross_origin()
def index_ingredientes():
    return jsonify('Bienvenido a ingredientes')