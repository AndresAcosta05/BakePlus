from flask import Blueprint, jsonify
from flask_cors import cross_origin
from src.utils.security import validate_token

venta = Blueprint('ventas_blueprint', __name__)

@venta.route('/')
@cross_origin()
@validate_token
def index_ventas():
    return jsonify('Bienvenido a ventas')