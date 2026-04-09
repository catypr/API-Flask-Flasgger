from flask import Blueprint, request, jsonify
from ..database import db
from ..models import Title
from ..schemas.title_schema import TitleSchema
from pydantic import ValidationError

titles_bp = Blueprint('titles', __name__, url_prefix='/titles')

@titles_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista todos os Títulos 
    ---
    tags:
      - Titles
    responses:
      200:
        description: OK
    """
    titulos = Title.query.all()
    result = [TitleSchema(**t.to_dict()).model_dump() for t in titulos]
    return jsonify(result), 200

@titles_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Busca um título específico pelo seu ID
    ---
    tags:
      - Titles
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do título
    responses:
      200:
        description: OK
    """
    titulo = Title.query.get(id)
    
    if not titulo:
        return jsonify({"error": "Título não encontrado"}), 404

    return jsonify(titulo.to_dict()), 200

@titles_bp.route('/', methods=['POST'])
def create():
    """
    Cadastra um novo título
    ---
    tags:
      - Titles
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Title'
    responses:
      201:
        description: Criado com sucesso
    """
    try:
        data = TitleSchema(**request.json)
        novo_titulo = Title(**data.model_dump())
        
        db.session.add(novo_titulo)
        db.session.commit()
        
        return jsonify(novo_titulo.to_dict()), 201
    except ValidationError as err:
        return jsonify({"errors": err.errors()}), 400

@titles_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualiza um título existente
    ---
    tags:
      - Titles
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          $ref: '#/definitions/Title'
    responses:
      200:
        description: OK
    """
    titulo = Title.query.get(id)
    
    if not titulo:
        return jsonify({"error": "Título não encontrado"}), 404
        
    try:
        data = request.json
        titulo.nome = data.get('nome', titulo.nome)
        titulo.subtitulo = data.get('subtitulo', titulo.subtitulo)
        titulo.descricao = data.get('descricao', titulo.descricao)
        titulo.genero = data.get('genero', titulo.genero)
        titulo.classificacao_indicativa = data.get('classificacao_indicativa', titulo.classificacao_indicativa)
        titulo.idioma_original = data.get('idioma_original', titulo.idioma_original)
        titulo.ano_primeiro_lancamento = data.get('ano_primeiro_lancamento', titulo.ano_primeiro_lancamento)
        
        db.session.commit()
        return jsonify(titulo.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@titles_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Remove um título
    ---
    tags:
      - Titles
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do título a ser removido
    responses:
      200:
        description: OK
      404:
        description: Não encontrado
    """
    titulo = Title.query.get(id)
    
    if not titulo:
        return jsonify({"error": "Título não encontrado"}), 404
        
    db.session.delete(titulo)
    db.session.commit()
    
    return jsonify({"message": "Título removido com sucesso"}), 200