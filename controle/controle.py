from abc import ABC
from persistencia.persistencia import Persistencia

class Controle(ABC): 
    def __init__(self, persistencia: Persistencia):
        self.persistencia = persistencia

    def gravar(self, entidade):
        self.persistencia.gravar(entidade)
    
    def apagar(self, entidade):
        return self.persistencia.apagar(entidade)

    def buscar(self, user: str, *args):
        return self.persistencia.buscar(user, *args)
