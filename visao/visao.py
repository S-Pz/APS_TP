from abc import ABC, abstractmethod
from controle.controle import Controle


class Visao(ABC):
    def __init__(self, controle: Controle):
        self.controle = controle

    def opcoes(self):
        while True:
            opcao = self.menu()
            if opcao == 0:
                return
            elif opcao == 1:
                self.insercao()
            elif opcao == 2:
                self.exclusao()
            elif opcao == 3:
                self.alteracao()
            elif opcao == 4:
                self.buscaID()
            elif opcao == 5:
                self.buscaVal()
    
    @abstractmethod
    def menu(self): pass

    @abstractmethod
    def insercao(self): pass

    @abstractmethod
    def exclusao(self): pass
    
    @abstractmethod
    def alteracao(self): pass 

    @abstractmethod
    def buscaID(self): pass 

    @abstractmethod
    def buscaVal(self): pass 
