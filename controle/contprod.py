from controle.controle import Controle
from persistencia.prodper import ProdutoPersistencia


class ProdutoControle(Controle):
    def __init__(self):
        super().__init__(ProdutoPersistencia())

    def buscaID(self, id: int):
        return super().buscaID(id)

    def buscaVal(self, valor: str):
        return super().buscaVal(valor)

