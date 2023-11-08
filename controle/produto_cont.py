from controle.controle import Controle
from modelo.produto import Produto
from persistencia.produto_per import ProdutoPersistencia

class ProdutoControle(Controle):
    def __init__(self):
        super().__init__(ProdutoPersistencia())

    def buscar(self, entidade: Produto):
        return super().buscar(entidade)
