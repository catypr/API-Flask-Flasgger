# API-Flask-Flasgger

Esta é uma API desenvolvida em Python utilizando o framework Flask. O sistema permite gerenciar um catálogo completo de livros, incluindo informações sobre autores, editoras, títulos e disponibilidade de estoque.

🚀 Tecnologias Utilizadas
- Python 3.x
- Flask
- Flasgger
- PostgreSQL
- Docker 
- Pydantic
- Alembic (migrations)

## Repositório
https://github.com/Catypr/API-Flask-Flasgger

## 🔧 Como rodar o projeto
1. Clone o repositório:

git clone https://github.com/Catypr/API-Flask-Flasgger.git 
cd API-Flask-Flasgger

2. Criar e ativar o ambiente virtual:
python -m venv venv 
venv\Scripts\activate

3. Instalar as dependências:
pip install -r requirements.txt

4. Configurar as variáveis de ambiente:
Crie um arquivo .env na raiz do projeto e adicione as configurações necessárias (exemplo):
FLASK_APP=src/app.py
FLASK_ENV=development
DATABASE_URL=sqlite:///database.db

5. Executar as migrações e o Seed:
flask db upgrade
python src/scripts/seed.py

6. Rodar a aplicação:
flask run 

## 📖 Documentação (Swagger)
Após iniciar o servidor, você pode acessar a documentação interativa da API através do navegador no endereço:
http://localhost:5000/apidocs