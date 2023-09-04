from abc import ABC

class Pessoa (ABC):
    def __init__(self, nome: str, cpf: str, data_nasc: str, salario: float, telefone: str, funcao: str):
        self.nome      = nome 
        self.cpf       = cpf 
        self.data_nasc = data_nasc
        self.salario   = salario 
        self.telefone  = telefone
        self.funcao    = funcao
