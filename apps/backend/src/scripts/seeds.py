import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from dotenv import load_dotenv
load_dotenv()

from src.app import create_app
from src.database import db
from src.models import Publisher, Title, Book

PUBLISHERS = [
    {
        "id": 1,
        "nome": "Intrínseca",
        "site": "intrinseca.com.br",
        "telefone": "(11) 94292-7189",
        "email": "sac@companhidasletras.com.br",
        "ativo": True
    },
    {
       "id": 2,
        "nome": "Companiha das Letras",
        "site": "campanhidasletras.com.br",
        "telefone": "(21) 3206-7474",
        "email": "contato@intrinseca.com.br",
        "ativo": True 
    }
]

TITLES= [
    {
        "id": 1,
        "nome": "Crepúsculo",
        "genero": "Romance",
        "classificacao_indicativa": 14,
        "idioma_original": "Inglês",
        "ano_primeiro_lancamento": 2005
    },
    {
        "id": 2,
        "nome": "Orgulho e Preconceito",
        "genero": "Romance",
        "classificacao_indicativa": 16,
        "idioma_original": "Inglês",
        "ano_primeiro_lancamento": 1813
    }
]

BOOKS = [
    {
        "id": 1 ,
        "titulo": "Lendários",
        "autor": "Tracy Deonn",
        "isbn": "978655602661",
        "paginas": 400,
        "data_publicacao": "2021/07/28",
        "disponivel": True
    },
    {
       "id": 2 ,
        "titulo": "Tartaruga até lá embaixo",
        "autor": "Jonh Green",
        "isbn": "9788415594918",
        "paginas": 272,
        "data_publicacao": "2017/10/10",
        "disponivel": True  
    }
]

def seed():
    app = create_app()
    with app.app_context():
        if Publisher.query.first():
            print("Banco já populado com dados editoriais!")
            return
        print("Inserindo dados do sistema editorial...")

        for p in PUBLISHERS:
            db.session.add(Publisher(**p))
        
        for t in TITLES: 
            db.session.add(Title(**t))

        for b in BOOKS:
            db.session.add(Book(**b))

        try:
            db.session.commit()
            print("Seed editorial finalizado com sucesso!")
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao inserir os dados: {e}")

if __name__ == '__main__':
    seed()