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
                self.gravar()
            elif opcao == 2:
                self.apagar()
            elif opcao == 3:
                self.buscar()
    
    @abstractmethod
    def menu(self): pass

    @abstractmethod
    def gravar(self): pass

    @abstractmethod
    def apagar(self): pass
    
    @abstractmethod
    def buscar(self): pass 
