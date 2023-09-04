class Patrocinador:
    def __init__(self, nome: str, cnpj: str, telefone: str, valor_contrato: float, local_merchan: str):
        self.nome           = nome 
        self.telefone       = telefone 
        self.cnpj           = cnpj
        self.valor_contrato = valor_contrato
        self.local_merchan  = local_merchan
