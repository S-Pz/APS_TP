import pickle
from modelo.produto import Produto
from persistencia.persistencia import Persistencia


class ProdutoPersistencia(Persistencia):
    lista_produtos = []

    def insercao(self, entidade: Produto):
        print(f"Entidade: {entidade.__str__()}")
        self.lista_produtos.append(entidade)

    def exclusao(self, entidade: Produto):
        return self.lista_produtos.remove(entidade)

    def alteracao(self, entidade: Produto):
        for indice in range(len(self.lista_produtos)):
            if self.lista_produtos[indice].id == entidade.id:
                self.lista_produtos[indice] = entidade
                return True
        return False

    def buscaID(self, id: int):
        for indice in range(len(self.lista_produtos)):
            if self.lista_produtos[indice].id == id:
                return self.lista_produtos[indice]
        return -1

    def buscaVal(self, valor: str):
        for indice in range(len(self.lista_produtos)):
            if self.lista_produtos[indice].nome == valor:
                return self.lista_produtos[indice]
        return -1

    def carregarDoArquivo(self):
        try:
            arquivo = open("produtos.txt", "rb")
            for _ in range(pickle.load(arquivo)):
                self.lista_produtos.append(pickle.load(arquivo))
            arquivo.close()
            return True
        except:
            return False
    
    def salvarNoArquivo(self):
        try:
            arquivo = open("produtos.txt", "wb")
            pickle.dump(len(self.lista_produtos), arquivo)
            for valor in self.lista_produtos:
                pickle.dump(valor, arquivo)
            arquivo.close()
            return True
        except:
            return False