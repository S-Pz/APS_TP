from controle.controle import Controle
from persistencia.cliper import ClientePersistencia


class ClienteControle(Controle):
    def __init__(self):
        super().__init__(ClientePersistencia())

    def buscaID(self, id: int):
        return super().buscaID(id)

    def buscaVal(self, valor: str):
        return super().buscaVal(valor)

