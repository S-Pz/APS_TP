from controle.controle import Controle
from persistencia.pessoa_per import PessoaPersistencia

class PessoaControle(Controle):
    def __init__(self):
        super().__init__(PessoaPersistencia())

    def buscar(self, termo: str):
        return super().buscar(termo)
