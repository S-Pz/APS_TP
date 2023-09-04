from modelo.pessoa import Pessoa
from persistencia.persistencia import Persistencia
import mysql.connector

class PessoaPersistencia(Persistencia):
    conexao = mysql.connector.connect(user='root', password='senha', database='NFL') 
    cursor = conexao.cursor()

    def gravar(self, entidade: Pessoa):
        add_pessoa = ("INSERT INTO PESSOA "
                       "(nome, cpf, data_nasc, salario, telefone, funcao) "
                       "VALUES (%s, %s, %s, %s, %s, %s)")
        dado_pessoa = (entidade.nome, entidade.cpf, entidade.data_nasc, entidade.salario, entidade.telefone, entidade.funcao)
        if entidade.funcao.strip().lower() == "jogador":
            pass
        self.cursor.execute(add_pessoa, dado_pessoa)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

    def apagar(self, entidade: Pessoa):
        del_pessoa = ("DELETE FROM PESSOA WHERE CPF=%s")
        self.cursor.execute(del_pessoa, entidade.pessoa.cpf)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

    def buscar(self, entidade: Pessoa):
        busca_pessoa = ("SELECT * FROM PESSOA WHERE NOME=%s")
        self.cursor.execute(busca_pessoa, entidade.pessoa.nome)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
