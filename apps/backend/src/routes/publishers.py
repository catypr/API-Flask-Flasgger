from flask import Blueprint, request, jsonify
from ..database import db
from ..models import Publisher
from ..schemas.publisher_schema import PublisherSchema
from pydantic import ValidationError

publishers_bp = Blueprint('publishers', __name__, url_prefix='/publishers')

@publishers_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista todas as editoras do banco de dados
    ---
    tags:
      - Publishers
    responses:
      200:
        description: OK
    """
    editoras = Publisher.query.all()
    result = [PublisherSchema(**e.to_dict()).model_dump() for e in editoras]
    return jsonify(result), 200

@publishers_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Busca uma editora específica pelo seu ID
    ---
    tags:
      - Publishers
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do registro
    responses:
      200:
        description: OK
    """
    editora = Publisher.query.get(id)
    
    if not editora:
        return jsonify({"error": "Editora não encontrada"}), 404

    return jsonify(editora.to_dict()), 200

@publishers_bp.route('/', methods=['POST'])
def create():
    """
    Cadastra uma nova editora
    ---
    tags:
      - Publishers
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Publisher'
    responses:
      201:
        description: Criado com sucesso
    """
    try:
        data = PublisherSchema(**request.json)
        nova_editora = Publisher(**data.model_dump())
        
        db.session.add(nova_editora)
        db.session.commit()
        
        return jsonify(nova_editora.to_dict()), 201
    except ValidationError as err:
        return jsonify({"errors": err.errors()}), 400
    
@publishers_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualiza uma editora existente
    ---
    tags:
      - Publishers
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          $ref: '#/definitions/Publisher'
    responses:
      200:
        description: OK
    """
    editora = Publisher.query.get(id)
    
    if not editora:
        return jsonify({"error": "Editora não encontrada"}), 404
        
    try:
        data = request.json
        editora.nome_fantasia = data.get('nome_fantasia', editora.nome_fantasia)
        editora.razao_social = data.get('razao_social', editora.razao_social)
        editora.cnpj = data.get('cnpj', editora.cnpj)
        editora.email_contato = data.get('email_contato', editora.email_contato)
        editora.site = data.get('site', editora.site)
        editora.telefone = data.get('telefone', editora.telefone)
        editora.ativo = data.get('ativo', editora.ativo)

        db.session.commit()
        return jsonify(editora.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@publishers_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Remove uma editora
    ---
    tags:
      - Publishers
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do registro a ser removido
    responses:
      200:
        description: OK
      404:
        description: Não encontrado
    """
    editora = Publisher.query.get(id)
    
    if not editora:
        return jsonify({"error": "Editora não encontrada"}), 404
        
    db.session.delete(editora)
    db.session.commit()
    
    return jsonify({"message": "Editora removida com sucesso"}), 200