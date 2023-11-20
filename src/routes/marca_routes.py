from flask import Blueprint, jsonify
from flask_cors import cross_origin

marca = Blueprint('marcas_blueprint', __name__)

@marca.route('/')
@cross_origin()
def index_marcas():
    return jsonify('Bienvenido a marcas')