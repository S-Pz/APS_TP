from controle.controle import Controle
from modelo.pessoa import Pessoa
from persistencia.pessoa_per import PessoaPersistencia

class PessoaControle(Controle):
    def __init__(self):
        super().__init__(PessoaPersistencia())

    def buscar(self, entidade: Pessoa):
        return super().buscar(entidade)
