from dataclasses import dataclass
from database.prezzo_DAO import PrezzoDAO


@dataclass()
class Distributore:
    id: int
    nome: str
    indirizzo: str

    lista_prezzi: list = None

    def get_prezzi(self):
        self.lista_prezzi = PrezzoDAO.get_prezzi(self.id)
        return self.lista_prezzi

    def __eq__(self, other):
        return isinstance(other, Distributore) and self.id == other.id

    def __str__(self):
        return f"{self.id} | {self.nome} | Indirizzo: {self.indirizzo}"

    def __repr__(self):
        return f"{self.id} | {self.nome} | Indirizzo: {self.indirizzo}"