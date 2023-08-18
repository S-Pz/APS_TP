import pickle
from modelo.entrega import Entrega
from persistencia.persistencia import Persistencia

class EntregaPersistencia(Persistencia):
    lista_entregas = [] # aqui vai ser a parte de BD

    def insercao(self, entidade: Entrega):
        self.lista_entregas.append(entidade)
    
    def exclusao(self, entidade: Entrega):
        return self.lista_entregas.remove(entidade) 
    
    def alteracao(self, entidade: Entrega):
        for indice in range(len(self.lista_entregas)):
            if self.lista_entregas[indice].id == entidade.id:
                self.lista_entregas[indice] = entidade
                return True 
        return False

    def buscaID(self, id: int):
        for indice in range(len(self.lista_entregas)):
            if self.lista_entregas[indice].id == id: 
                return self.lista_entregas[indice] 
        return -1
    
    def buscaVal(self, valor: str):
        for indice in range(len(self.lista_entregas)):
            if self.lista_entregas[indice].venda.cliente.nome == valor:
                return self.lista_entregas[indice] 
        return False

    def carregarDoArquivo(self):
        try:
            arquivo = open("entregas.txt", "rb")
            for _ in range(pickle.load(arquivo)):
                self.lista_entregas.append(pickle.load(arquivo))
            arquivo.close()
            return True
        except:
            return False
    
    def salvarNoArquivo(self):
        try:
            arquivo = open("entregas.txt", "wb")
            pickle.dump(len(self.lista_entregas), arquivo)
            for valor in self.lista_entregas:
                pickle.dump(valor, arquivo)
            arquivo.close()
            return True
        except:
            return False
