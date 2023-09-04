from controle.controle import Controle
from modelo.usuario import Usuario
from persistencia.usuario_per import UsuarioPersistencia

class UsuarioControle(Controle):
    def __init__(self):
        super().__init__(UsuarioPersistencia())

    def buscar(self, nome: str, senha: str):
        return super().buscar(nome, senha)
