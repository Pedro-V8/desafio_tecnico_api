from flask import Blueprint, request, jsonify

from src.db.repositories.pessoas_repository import PessoaRepository

routes_bp = Blueprint("routes", __name__)


@routes_bp.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"


@routes_bp.route("/list_pessoas", methods=["GET"])
def return_pessoas():
    pessoas = PessoaRepository.select_pessoas()
    response = [x.toDict() for x in pessoas]

    return jsonify(response)

@routes_bp.route("/create_pessoa", methods=["POST"])
def create_pessoa():
    request_form = request.json
    
    response = PessoaRepository.create_pessoa(request_form)

    return jsonify(response.toDict())

@routes_bp.route("/update_pessoa/<id>", methods=["PUT"])
def update_pessoa(id):
    request_form = request.json
    
    response = PessoaRepository.update_pessoa(id, request_form)

    return jsonify(response.toDict())

@routes_bp.route("/delete_pessoa/<id>", methods=["DELETE"])
def delete_pessoa(id):
    response = PessoaRepository.delete_pessoa(id)

    return jsonify(response)
