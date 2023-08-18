from modelo.jogador import Jogador
from persistencia.persistencia import Persistencia

class JogadorPersistencia(Persistencia):
    lista_clientes = []

    def insercao(self, entidade: Cliente):
        self.lista_clientes.append(entidade)
    
    def exclusao(self, entidade: Cliente):
        return self.lista_clientes.remove(entidade) 
    
    def alteracao(self, entidade: Cliente):
        for indice in range(len(self.lista_clientes)):
            if self.lista_clientes[indice].id == entidade.id:
                self.lista_clientes[indice] = entidade
                return True 
        return False

    def buscaID(self, id: int):
        for indice in range(len(self.lista_clientes)):
            if self.lista_clientes[indice].id == id: 
                return self.lista_clientes[indice] 
        return -1
    
    def buscaVal(self, valor: str):
        for indice in range(len(self.lista_clientes)):
            if self.lista_clientes[indice].nome == valor: 
                return self.lista_clientes[indice] 
        return -1

    def carregarDoArquivo(self):
        try:
            arquivo = open("clientes.txt", "rb")
            for _ in range(pickle.load(arquivo)):
                self.lista_clientes.append(pickle.load(arquivo))
            arquivo.close()
            return True
        except:
            return False
            
    def salvarNoArquivo(self):
        try:
            arquivo = open("clientes.txt", "wb")
            pickle.dump(len(self.lista_clientes), arquivo)
            for valor in self.lista_clientes:
                pickle.dump(valor, arquivo)
            arquivo.close()
            return True
        except:
            return False
