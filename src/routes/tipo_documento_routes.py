from flask import Blueprint, jsonify
from flask_cors import cross_origin

tipo_documento = Blueprint('tipo_documentos_blueprint', __name__)

@tipo_documento.route('/')
@cross_origin()
def index_tipo_documentos():
    return jsonify('Bienvenido a tipo_documentos')