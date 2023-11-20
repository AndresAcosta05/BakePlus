from flask import Blueprint, jsonify
from flask_cors import cross_origin

page = Blueprint('pages', __name__)

@page.route('/')
@cross_origin()
def index_pages():
    return jsonify('Bienvenido a pages')