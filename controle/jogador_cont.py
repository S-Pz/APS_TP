from controle.controle import Controle
from persistencia.jogador_per import JogadorPersistencia

class JogadorControle(Controle):
    def __init__(self):
        super().__init__(JogadorPersistencia())

    def buscar(self, termo: str):
        return super().buscar(termo)
