from flask import Flask 
from flasgger import Swagger 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.cofig['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/livros_db'

    Swagger(app)
    db.init_app(app)
    Migrate(app, db)

    from .routes.blueprint_get import bp_get 
    from .routes.blueprint_post import bp_post

    app.register_blueprint(bp_get)
    app.register_blueprint(bp_post)

    return app