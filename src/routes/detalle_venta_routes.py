from flask import Blueprint, jsonify

detalle_venta = Blueprint('detalle_ventas_blueprint', __name__)

@detalle_venta.route('/')
def index_detalle_ventas():
    return jsonify('Bienvenido a detalle_ventas')