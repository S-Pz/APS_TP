from modelo.pessoa import Pessoa

class RH:
    def __init__(self, pessoa: Pessoa, cargo: str):
        self.pessoa = pessoa
        self.cargo  = cargo

