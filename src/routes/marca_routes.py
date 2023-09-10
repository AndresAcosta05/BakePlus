from flask import Blueprint, jsonify

marca = Blueprint('marcas_blueprint', __name__)

@marca.route('/')
def index_marcas():
    return jsonify('Bienvenido a marcas')