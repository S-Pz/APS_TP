from abc import ABC, abstractmethod

class Persistencia(ABC):
    @abstractmethod
    def gravar(self, entidade): pass 
    
    @abstractmethod
    def apagar(self, termo: str): pass 
    
    @abstractmethod
    def buscar(self, termo: str, *args): pass 
