from controle.controle import Controle
from persistencia.vendaper import VendaPersistencia


class VendaControle(Controle):
    def __init__(self):
        super().__init__(VendaPersistencia())

    def buscaID(self, id: int):
        return super().buscaID(id)

    def buscaVal(self, valor: str):
        return super().buscaVal(valor)

