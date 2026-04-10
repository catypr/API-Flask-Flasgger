# API-Flask-Flasgger

API para listagem de Livros.

Tecnologias Utilizadas
- Flask
- Flasgger
- PostgreSQL
- Doker 
- Pydantic
- Alembic (migrations)

## Repositório
https://github.com/Catypr/API-Flask-Flasgger

## Como rodar o projeto
1. Clone o repositório:

git clone https://github.com/Catypr/API-Flask-Flasgger.git 
cd API-Flask-Flasgger

2. Suba o banco de dados com o Docker:
docker compose up -d

3. Acesse o backend:
cd apps/backend

4. Instale/atualize as dependências:
uv sync

5. Execute as migtations:
uv run alembic upgrade head

6. Inicie a aplicação Flask:
uv run flasck --app src.app run 

## Variáveis de ambiente
o backend carrega as configurações do arquivo `apps/backend/.env`.
Por padrão ele usa:
DATABASE_URL=postgresql://devuser:devpassword@localhost:5433/turismo_db

## Documentação da API
A documentação interativa (Swagger) estará disponível em:
http://localhost:5000/apidocs