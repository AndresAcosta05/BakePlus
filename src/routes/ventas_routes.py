from flask import Blueprint, jsonify

venta = Blueprint('ventas_blueprint', __name__)

@venta.route('/')
def index_ventas():
    return jsonify('Bienvenido a ventas')