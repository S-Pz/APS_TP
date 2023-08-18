from abc import ABC, abstractmethod
from modelo.pessoa import Pessoa

class Persistencia(ABC):
    @abstractmethod
    def insercao(self, pessoa: Pessoa): pass 
    
    @abstractmethod
    def alteracao(self, pessoa: Pessoa): pass 

    @abstractmethod
    def exclusao(self, pessoa: Pessoa): pass 
    
    @abstractmethod
    def buscaID(self, id: int): pass 
    
    @abstractmethod
    def buscaVal(self, valor: str): pass

    @abstractmethod
    def carregarDoArquivo(self): pass
    
    @abstractmethod
    def salvarNoArquivo(self): pass
