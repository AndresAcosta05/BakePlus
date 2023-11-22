from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from src.controllers.receta_controller import recetaController

receta = Blueprint('recetas_blueprint', __name__)

@receta.route('/getAll')
@cross_origin()
def obtener_recetas():
    recetas = recetaController().cr_obtener_recetas()
    return jsonify(recetas)

@receta.route('/getOne/<int:id>')
@cross_origin()
def obtener_receta_id(id):
    receta = recetaController().cr_obtener_receta_id(id=id)
    return jsonify(receta)

@receta.route('/insert', methods=['POST'])
@cross_origin()
def insertar_receta():
    if request.method == 'POST':
        receta = request.json
        response = recetaController().insertar_receta(receta=receta)
        return jsonify(response)