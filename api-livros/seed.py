from app import create_app, db
from app.models import Livro

app = create_app()
with app.app_context():
    l1 = Livro(titulo="Dom Casmurro", autor="Machado de Assis")]
    db.session.add(l1)
    db.session.commit()
    print("Banco de dados populado1")