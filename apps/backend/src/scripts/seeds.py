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

TITLE = [
    {
        "id": 1
        "nome": "Crepúsculo",
        "genero": "Romance",
        "classificacao_indicativa": 14
        "idioma_original": "Inglês",
        "ano_primeiro_lancamento": 2005
    },
    {
         "id": 2
        "nome": "Orgulho e Preconceito",
        "genero": "Romance",
        "classificacao_indicativa": 16
        "idioma_original": "Inglês",
        "ano_primeiro_lancamento": 1813
    }
]

