from modelo.fornecedor import Fornecedor

class Produto:
<<<<<<< HEAD
    def __init__(self, nome: str, preco: float, qtd: int, chave: str):
        self.nome = nome 
        self.preco = preco 
        self.qtd = qtd 
        self.chave = chave
=======
    def __init__(self, nome: str, preco: float, qtd: int, chave: Fornecedor):
        self.nome = nome 
        self.preco = preco 
        self.qtd = qtd 
        self.chave = chave.cnpj
>>>>>>> origin/main
