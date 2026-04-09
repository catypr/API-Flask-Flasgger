from pydantic import BaseModel 

class AuthorSchema(BaseModel):
    id : int | None = None
    nome: str
    biografia: str
    nacionalidade: str 
    data_nascimento: str 
