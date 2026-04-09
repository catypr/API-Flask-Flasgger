from flask import Blueprint, request, jsonify
from ..database import db
from ..models import Author
from ..schemas.author_schema import AuthorSchema
from pydantic import ValidationError

authors_bp = Blueprint('authors', __name__, url_prefix='/authors')

@authors_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista de Autores
    ---
    tags:
        - Authors
    responses:
        200:
            description: OK
    """
    authors = Author.query.all()
    result = [AuthorSchema(**a.to_dict()).model_dump() for a in authors]
    return jsonify(result), 200

@authors_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Busca um Autor específico pelo ID
    ---
    tags:
        - Authors
    parameters:
        - in: path
          name: id
          type: interger
          required: true
          description: ID do registro 
    responses:
        200:
            description: OK
    """
    autor = Author.query.get(id)

    if not autor:
        return jsonify({"error": "Autor não encotrado"}), 404
    return jsonify(autor.to_dict()), 200

@authors_bp.route('/', methods=['POST'])
def create():
    """
    Cadastrar um novo Autor
    ---
    tags:
        - Authors
    parameters:
        - in: body
          name: body
          required: true
          schema:
            $ref: '#/definitions/Authors'
    reaponses:
        200:
            description: Autor cadastrado com sucesso
            schema:
                $ref: '#/definitions/Authors'
    """
    try:
        data = AuthorSchema(**request.json)
        novo_autor = Author(**data.model_dump())
        db.session.add(novo_autor)
        db.session.commit()

        return jsonify(novo_autor.to_dict()), 201
    except ValidationError as err:
        return jsonify({"errors": err.errors()}), 400

@authors_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualizar um Autor existente 
    ---
    tags:
        - Authors:
    parameters:
        - in: path
          name: id
          tupe: interger
          required: true
        - in: body
          name: body
          schema:
            $ref: '#/definitions/Authors'
    responses:
        200:
            description: OK
    """
    autor = Author.query.get(id)

    if not autor:
        return jsonify ({"error": "Autor não encontrado"}), 404
    try:
        data = request.json
        autor.nome = data.get('nome', autor.nome)
        autor.biografia = data.get('biografia', autor.biografia)
        autor.nacionalidade = data.get('nacionalidade', autor.nacionalidade)
        autor.data_nascimento = data.get('data_nascimento', autor.data_nascimento)

        db.session.commit()
        return jsonify(autor.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@authors_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Exclui um Autor
    ---
    tags:
        - Authors
    parameters:
        - in: path
          name: id
          type: interger
          required: true
          description: ID do autor a ser removido
    responses: 
        200:
            description: OK
        404:
            description: Não encontrado
    """
    autor =  Author.query.get(id)

    if not autor:
        return jsonify({"error": "Autor removido com sucesso"}), 404
    
    db.session.delete(autor)
    db.session.commit()

    return jsonify({"mensagem": "Autor removido com sucesso"}), 200