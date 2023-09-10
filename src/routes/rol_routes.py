from flask import Blueprint, jsonify

rol = Blueprint('rols_blueprint', __name__)

@rol.route('/')
def index_rols():
    return jsonify('Bienvenido a rols')