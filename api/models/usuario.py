from datetime import datetime

class Usuario:
    def __init__(self, email: str, senha_hash: str, criado_em: datetime = None, _id=None):
        self.id=_id
        self.email=email
        self.senha_hash=senha_hash
        self.criado_em = criado_em or datetime.utcnow()

    def to_dict(self):
        return{
            "email" : self.email,
            "senha_hash" : self.senha_hash,
            "criado_em" : self.criado_em
        }
