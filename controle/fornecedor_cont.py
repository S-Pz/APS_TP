from controle.controle import Controle
from modelo.fornecedor import Fornecedor
from persistencia.fornecedor_per import FornecedorPersistencia

class FornecedorControle(Controle):
    def __init__(self):
        super().__init__(FornecedorPersistencia())

    def buscar(self, entidade: Fornecedor):
        return super().buscar(entidade)
