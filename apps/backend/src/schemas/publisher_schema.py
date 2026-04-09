from pydantic import BaseModel, EmailStr

class Publisher(BaseModel):
    id: int | None = None
    nome: str
    site: str | None = None
    telefone: str
    email_contato: EmailStr | str 
