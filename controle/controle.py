from abc import ABC
from persistencia.persistencia import Persistencia
from modelo.entidades import Entidade


class Controle(ABC): 
    def __init__(self, persistencia: Persistencia):
        self.persistencia = persistencia

    def insercao(self, entidade: Entidade):
        self.persistencia.insercao(entidade)
    
    def alteracao(self, entidade: Entidade):
        return self.persistencia.alteracao(entidade)
    
    def exclusao(self, entidade: Entidade):
        return self.persistencia.exclusao(entidade)

    def buscaID(self, id: int):
        return self.persistencia.buscaID(id)

    def buscaVal(self, valor: str):
        return self.persistencia.buscaVal(valor)

    def carregar(self):
        return self.persistencia.carregarDoArquivo()
    
    def salvar(self):
        return self.persistencia.salvarNoArquivo()
