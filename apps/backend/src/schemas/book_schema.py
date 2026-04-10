from pydantic import BaseModel

class BookSchema(BaseModel):
    id: int | None = None
    titulo: str
    autor: str
    isbn: str
    paginas: int
    data_publicacao: date | str
    disponivel: bool = True
