from modelo.pessoa import Pessoa

class Jogador (Pessoa):
    def __init__(self, nome: str, cpf: str, data_nasc: str, salario: float, telefone: str, numero_camisa: int, funcao: str):
        super().__init__(nome, cpf, data_nasc, salario, telefone)
        self.numero_camisa = numero_camisa
        self.funcao        = funcao

    def __str__(self):
        return super().__str__() + f"NOME: {self.nome} CPF: {self.cpf} "
