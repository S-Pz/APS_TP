from modelo.pessoa import Pessoa

class Patrocinador (Pessoa):
    def __init__(self, nome: str, cnpj: str, telefone: str, valor_contrato: float, local_merchan: str):
        super().__init__(nome, telefone)
        self.cnpj    = cnpj
        self.valor_contrato = valor_contrato
        self.local_merchan  = local_merchan

    def __str__(self):
        return super().__str__() + f"NOME: {self.nome} PREÇO: R${self.preco:.2f} "
