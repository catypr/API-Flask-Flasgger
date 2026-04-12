from flask import Flask
from flasgger import Swagger
import os
from dotenv import load_dotenv
from .database import init_db, db
from flask_migrate import Migrate

from .schemas.author_schema import AuthorSchema
from .schemas.book_schema import BookSchema
from .schemas.publisher_schema import PublisherSchema
from .schemas.title_schema import TitleSchema

from .models import Author, Book, Publisher, Title

load_dotenv()

def create_app():
    app = Flask(__name__)
    init_db(app)

    Migrate(app, db)

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "API de Livros",
            "description": "API para gestão de cadastros de Livros",
            "version": "1.0.0"
          },
        "definitions": {
            "Author": AuthorSchema.model_json_schema(),
            "Book": BookSchema.model_json_schema(),
            "Publisher": PublisherSchema.model_json_schema(),
            "Title": TitleSchema.model_json_schema(),
            "Error": {
                "type": "object",
                "properties": {"error": {"type": "string"}}
            }
        }
    }

    Swagger(app, template=swagger_template)

    from .routes.authors import authors_bp
    from .routes.books import books_bp
    from .routes.publishers import publishers_bp
    from .routes.titles import titles_bp

    app.register_blueprint(authors_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(publishers_bp)
    app.register_blueprint(titles_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)