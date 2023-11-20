from flask import Blueprint, jsonify
from flask_cors import cross_origin

detalle_venta = Blueprint('detalle_ventas_blueprint', __name__)

@detalle_venta.route('/')
@cross_origin()
def index_detalle_ventas():
    return jsonify('Bienvenido a detalle_ventas')