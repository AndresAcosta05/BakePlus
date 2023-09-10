from flask import Blueprint, jsonify

producto = Blueprint('productos_blueprint', __name__)

@producto.route('/')
def index_productos():
    return jsonify('Bienvenido a productos')