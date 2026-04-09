from flask import Blueprint, resuqest, jsonify
from ..database import db
from ..models import Book
from ..schemas.book_schema import BookSchema
from pydantic import ValidationError 

books_bp = Blueprint('books', __name__, url_prefix='/books')

@books_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista de Livros
    ---
    tags: 
        - Books
    responses:
        200:
            description: OK
    """
    livros = Book.query.all()
    result = [BookSchema(**b.to_dict()).model_dump() for b in livros]
    return jsonify(result), 200

@books_bp.route('/<init:id>', methods=['GET'])
def get_by_id(id):
    """
    Busca por um livro específico pelo ID
    ---
    tags: 
        - Books
    parameters:
        - in: path
          name: id
          type: interger
          required: true
          descriptions: ID do livro
    responses:
        200:
            descriptions: OK
    """
    livro = Book.query.get(id)

    if not livro:
        return jsonify({"error": "Livro não encontrado"}), 404
    return jsonify(livro.to_dict()), 200

@books_bp.route('/', methods=['POST'])
def create():
    """
    Cadastra um novo livro
    ---
    tags:
      - Books
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Book'
    responses:
      201:
        description: Criado com sucesso
    """
    try:
        data = BookSchema(**request.json)
        novo_livro = Book(**data.model_dump())
        
        db.session.add(novo_livro)
        db.session.commit()
        
        return jsonify(novo_livro.to_dict()), 201
    except ValidationError as err:
        return jsonify({"errors": err.errors()}), 400
    
@books_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualiza um livro existente
    ---
    tags:
      - Books
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          $ref: '#/definitions/Book'
    responses:
      200:
        description: OK
    """
    livro = Book.query.get(id)
    
    if not livro:
        return jsonify({"error": "Livro não encontrado"}), 404
        
    try:
        data = request.json
        livro.titulo = data.get('titulo', livro.titulo)
        livro.autor = data.get('autor', livro.autor)
        livro.isbn = data.get('isbn', livro.isbn)
        livro.paginas = data.get('paginas', livro.paginas)
        livro.data_publicacao = data.get('data_publicacao', livro.data_publicacao)
        livro.disponivel = data.get('disponivel', livro.disponivel)
        
        db.session.commit()
        return jsonify(livro.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@books_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Remove um livro do sistema
    ---
    tags:
      - Books
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do livro a ser removido
    responses:
      200:
        description: OK
      404:
        description: Não encontrado
    """
    livro = Book.query.get(id)
    
    if not livro:
        return jsonify({"error": "Livro não encontrado"}), 404
        
    db.session.delete(livro)
    db.session.commit()
    
    return jsonify({"message": "Livro removido com sucesso"}), 200