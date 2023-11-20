from flask import Blueprint, jsonify
from flask_cors import cross_origin

venta = Blueprint('ventas_blueprint', __name__)

@venta.route('/')
@cross_origin()
def index_ventas():
    return jsonify('Bienvenido a ventas')