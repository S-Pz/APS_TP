from modelo.pessoa import Pessoa

class Fornecedor (Pessoa):
    def __init__(self, nome: str, cnpj: str, produtos: list, telefone: str):
        super().__init__(nome, telefone)
        self.cnpj    = cnpj
        self.produtos = produtos

    def __str__(self):
        string = f"VENDA: {self.venda} ENDERECO: {self.endereco}"
        return super().__str__() + string


