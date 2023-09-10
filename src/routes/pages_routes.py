from flask import Blueprint, jsonify

page = Blueprint('pages', __name__)

@page.route('/')
def index_pages():
    return jsonify('Bienvenido a pages')