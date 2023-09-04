from controle.controle import Controle
from modelo.patrocinador import Patrocinador
from persistencia.patrocinador_per import PatrocinadorPersistencia

class PatrocinadorControle(Controle):
    def __init__(self):
        super().__init__(PatrocinadorPersistencia())

    def buscar(self, entidade: Patrocinador):
        return super().buscar(entidade)
