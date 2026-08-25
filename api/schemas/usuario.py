from pydantic import BaseModel, EmailStr
from datetime import datetime

class UsuarioCreate(BaseModel):
    email: EmailStr
    senha: str

class UsuarioResponse(BaseModel):
    id: str
    email: str
    criado_em: datetime  

class LoginRequest(BaseModel):
    email: EmailStr
    senha: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"