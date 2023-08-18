from abc import ABC

class Pessoa (ABC):
    def __init__(self, nome: str, cpf: str, data_nasc: str, salario: float, telefone: str):
        self.nome      = nome 
        self.cpf       = cpf 
        self.data_nasc = data_nasc
        self.salario   = salario 
        self.telefone  = telefone

    def __str__(self): 
        return f"ID: {self.id} "
