from flask import Blueprint, jsonify

tipo_documento = Blueprint('tipo_documentos_blueprint', __name__)

@tipo_documento.route('/')
def index_tipo_documentos():
    return jsonify('Bienvenido a tipo_documentos')