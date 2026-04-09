from pydantic import BaseModel

class Book(BaseModel):
    id: int | None = None
    titulo: str
    autor: str
    isbn: str
    paginas: int
    data_publicacao: date | str
    disponivel: bool = True
