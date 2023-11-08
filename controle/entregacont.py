from controle.controle import Controle
from persistencia.entregaper import EntregaPersistencia


class EntregaControle(Controle):
    def __init__(self):
        super().__init__(EntregaPersistencia())

    def buscaID(self, id: int):
        return super().buscaID(id)

    def buscaVal(self, valor: str):
        return super().buscaVal(valor)

