from modelo.pessoa import Pessoa

class Comissao:
    def __init__(self, pessoa: Pessoa, cargo: str):
        self.pessoa = pessoa
        self.cargo  = cargo

    def __str__(self): 
        texto = f"CLIENTE: {self.cliente.nome} PRODUTO(S): "
        for produto in self.lista_produto:
            texto += f"\n\t{produto} " 
        texto += f"\n\tTOTAL: R${self.total_venda():.2f}"
        return super().__str__() + texto 
