import pickle
from modelo.venda import Venda
from persistencia.persistencia import Persistencia


class VendaPersistencia(Persistencia):
    lista_vendas = []

    def insercao(self, entidade: Venda):
        self.lista_vendas.append(entidade)
    
    def exclusao(self, entidade: Venda):
        return self.lista_vendas.remove(entidade) 
    
    def alteracao(self, entidade: Venda):
        for indice in range(len(self.lista_vendas)):
            if self.lista_vendas[indice].id == entidade.id:
                self.lista_vendas[indice] = entidade
                return True 
        return False

    def buscaID(self, id: int):
        for indice in range(len(self.lista_vendas)):
            if self.lista_vendas[indice].id == id:
                return self.lista_vendas[indice] 
        return -1
    
    def buscaVal(self, valor: str):
        for indice in range(len(self.lista_vendas)):
            if self.lista_vendas[indice].cliente.nome == valor:
                return self.lista_vendas[indice] 
        return -1
    
    def carregarDoArquivo(self):
        try:
            arquivo = open("vendas.txt", "rb")
            for _ in range(pickle.load(arquivo)):
                self.lista_vendas.append(pickle.load(arquivo))
            arquivo.close()
            return True
        except:
            return False
    
    def salvarNoArquivo(self):
        try:
            arquivo = open("vendas.txt", "wb")
            pickle.dump(len(self.lista_vendas), arquivo)
            for valor in self.lista_vendas:
                pickle.dump(valor, arquivo)
            arquivo.close()
            return True
        except:
            return False