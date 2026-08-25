from datetime import datetime

class Todo:
    def __init__(self, titulo: str, feito: bool = False, criado_em: datetime = None, _id=None):
        self.id = _id
        self.titulo = titulo
        self.feito = feito
        self.criado_em = criado_em or datetime.utcnow()

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "feito": self.feito,
            "criado_em": self.criado_em
        }