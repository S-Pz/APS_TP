from abc import ABC
from persistencia.persistencia import Persistencia

class Controle(ABC): 
    def __init__(self, persistencia: Persistencia):
        self.persistencia = persistencia

    def gravar(self, entidade):
        return self.persistencia.gravar(entidade)
    
    def apagar(self, termo):
        return self.persistencia.apagar(termo)

    def buscar(self, termo: str, *args):
        return self.persistencia.buscar(termo, *args)
