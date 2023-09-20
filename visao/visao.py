from abc import ABC, abstractmethod
from controle.controle import Controle

class Visao(ABC):
    def __init__(self, controle: Controle):
        self.controle = controle

    @abstractmethod
    def menu(self): pass

    @abstractmethod
    def gravar(self): pass

    @abstractmethod
    def apagar(self): pass
    
    @abstractmethod
    def buscar(self): pass 
