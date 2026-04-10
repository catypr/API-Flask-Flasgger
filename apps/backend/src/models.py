from .database import db

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    biografia = db.Column(db.Text)
    nacionalidade = db.Column(db.String)
    data_nascimento = db.Column(db.String)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
class Publisher(db.Model):
    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    site = db.Column(db.String)
    telefone = db.Column(db.String)
    email = db.Column(db.String)
    ativo = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Title(db.Model):
    __tablename__ = 'titles'
    id = db.Column(db.Interger, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    descricao = db.Column(db.Text)
    genero = db.Column(db.String)
    classificacoa_indicativa = db.Column(db.String)
    idioma_otiginal = db.Column(db.String)
    ano_primeiro_lancamento = db.Column(db.Interger)

    def to_dict(selg):
        return {c.name: getattr(self, c.name) for c in self.__table__.column}
    
class Book(db.Model):
    __tablename__ = 'books'
    id = db.column(db.Interger, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    autor = db.Column(db.String, nullable=False)
    isbn = db.Column(db.String, unique=True, nullable=False)
    paginas = db.Column(db.Interger)
    data_publicacao = db.Column(db.String)
    disponivel = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}