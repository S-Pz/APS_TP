from modelo.pessoa import Pessoa

class Jogador (Pessoa):
    def __init__(self, nome: str, cpf: str, data_nasc: str, salario: float, telefone: str, numero_camisa: int, funcao: str, posicao: str):
        super().__init__(nome, cpf, data_nasc, salario, telefone, funcao)
        self.numero_camisa = numero_camisa
        self.posicao       = posicao
