from abc import ABC, abstractmethod
from modelo.pessoa import Pessoa

class Persistencia(ABC):
    @abstractmethod
    def gravar(self, pessoa: Pessoa): pass 
    
    @abstractmethod
    def apagar(self, pessoa: Pessoa): pass 
    
    @abstractmethod
    def buscar(self, termo: str, *args): pass 
