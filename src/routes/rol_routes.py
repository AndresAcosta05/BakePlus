from flask import Blueprint, jsonify
from flask_cors import cross_origin

rol = Blueprint('rols_blueprint', __name__)

@rol.route('/')
@cross_origin()
def index_rols():
    return jsonify('Bienvenido a rols')