from flask import Blueprint, jsonify
from flask_cors import cross_origin

producto = Blueprint('productos_blueprint', __name__)

@producto.route('/')
@cross_origin()
def index_productos():
    return jsonify('Bienvenido a productos')