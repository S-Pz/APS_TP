from modelo.jogador import Jogador
from persistencia.persistencia import Persistencia
import mysql.connector

class JogadorPersistencia(Persistencia):
    conexao = mysql.connector.connect(user='root', password='senha', database='NFL') 
    cursor = conexao.cursor()

    def gravar(self, entidade: Jogador):
        add_jogador = ("INSERT INTO JOGADOR "
                       "(numero_camisa, posicao, cpf_jogador) "
                       "VALUES (%s, %s, %s)")
        dado_jogador = (entidade.numero_camisa, entidade.funcao, entidade.cpf)
        self.cursor.execute(add_jogador, dado_jogador)

        add_pessoa = ("INSERT INTO PESSOA"
                      "(nome, cpf, data_nasc, salario, telefone, funcao)"
                      "VALUES (%s, %s, %s, %s, %s, %s)")
        dado_pessoa = (entidade.nome, entidade.cpf, entidade.data_nasc, entidade.salario, entidade.telefone, entidade.funcao)
        self.cursor.execute(add_pessoa, dado_pessoa)
        if not self.cursor.fetchone():
            print(f"Cadastrando jogador")
            self.conexao.commit()
            self.cursor.close()
            self.conexao.close()
            return 1
        print(f"Jogador já presente no banco")
        return -1
    
    def apagar(self, entidade: Jogador):
        del_jogador = ("DELETE FROM JOGADOR WHERE CPF=%s")
        self.cursor.execute(del_jogador, entidade.cpf)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
    
    def buscar(self, entidade: Jogador):
        busca_jogador = ("SELECT * FROM JOGADOR WHERE NOME=%s")
        self.cursor.execute(busca_jogador, entidade.nome)
        if not self.cursor.fetchall():
            print(f"Jogador não está presente")
            self.conexao.commit()
            self.cursor.close()
            self.conexao.close()
            return -1
        print(f"Jogador presente")
        return 1
