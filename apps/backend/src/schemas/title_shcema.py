from pydantic import BaseModel 

class Title(BaseModel):
    id: str
    nome: str
    descricao: str | None = None
    genero: str | None = None
    classificacao_indicativa: str 
    idioma_origem: str 
    ano_primeira_publicacao: int 