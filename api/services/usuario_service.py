from database import db
from models.usuario import Usuario
from schemas.usuario import UsuarioResponse
from auth import gerar_hash_senha, verificar_senha, criar_token

class UsuarioService:
    def cadastrar_usuario(self, email: str, senha: str):
        senha_hash = gerar_hash_senha(senha)
        usuario = Usuario(email=email, senha_hash=senha_hash)
        resultado = db.usuarios.insert_one(usuario.to_dict())

        usuario_criado = db.usuarios.find_one({"_id": resultado.inserted_id})
        return self._to_response(usuario_criado)

    def _to_response(self, usurio_doc: dict) -> UsuarioResponse:
        return UsuarioResponse(
            id=str(usurio_doc["_id"]),
            email=usurio_doc["email"],
            criado_em=usurio_doc["criado_em"]
        )

    def login(self, email: str, senha: str):
        usuario_doc = db.usuarios.find_one({"email": email})

        if usuario_doc is None:
            return None

        if not verificar_senha(senha, usuario_doc["senha_hash"]):
            return None

        token = criar_token({"sub": str(usuario_doc["_id"])})
        return token