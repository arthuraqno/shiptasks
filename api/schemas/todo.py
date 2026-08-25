from pydantic import BaseModel
from datetime import datetime

class TodoCreate(BaseModel):
    titulo : str

class TodoResponse(BaseModel):
    id: str
    titulo: str
    feito: bool
    criado_em: datetime
    