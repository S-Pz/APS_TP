from abc import ABC, abstractmethod
<<<<<<< HEAD

class Persistencia(ABC):
    @abstractmethod
    def gravar(self, entidade): pass 
=======
from modelo.pessoa import Pessoa

class Persistencia(ABC):
    @abstractmethod
    def gravar(self, pessoa: Pessoa): pass 
>>>>>>> origin/main
    
    @abstractmethod
    def apagar(self, termo: str): pass 
    
    @abstractmethod
    def buscar(self, termo: str, *args): pass 
