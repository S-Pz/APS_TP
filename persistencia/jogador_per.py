from modelo.jogador import Jogador
from mysql.connector.cursor import CursorBase
from persistencia.persistencia import Persistencia
import mysql.connector

class JogadorPersistencia(Persistencia):

    def gravar(self, entidade: Jogador):
        conexao = mysql.connector.connect(user='root', password='senha', database='NFL') 
        cursor = conexao.cursor()
        add_jogador = ("INSERT INTO JOGADOR "
                       "(numero_camisa, posicao, cpf_jogador) "
                       "VALUES (%s, %s, %s)")
        dado_jogador = (entidade.numero_camisa, entidade.funcao, entidade.cpf)
        cursor.execute(add_jogador, dado_jogador)

        add_pessoa = ("INSERT INTO PESSOA"
                      "(nome, cpf, data_nasc, salario, telefone, funcao)"
                      "VALUES (%s, %s, %s, %s, %s, %s)")
        dado_pessoa = (entidade.nome, entidade.cpf, entidade.data_nasc, entidade.salario, entidade.telefone, entidade.funcao)
        cursor.execute(add_pessoa, dado_pessoa)
        if not cursor.fetchone():
            print(f"Cadastrando jogador")
            conexao.commit()
            cursor.close()
            conexao.close()
            return 1
        print(f"Jogador já presente no banco")
        return -1
    
    def apagar(self, cpf: str):
        conexao = mysql.connector.connect(user='root', password='senha', database='NFL') 
        cursor = conexao.cursor()
        del_jogador = ("DELETE FROM JOGADOR WHERE CPF='%s'")
        cursor.execute(del_jogador, cpf)
        conexao.commit()
        cursor.close()
        conexao.close()
    
    def buscar(self, termo: str):
        conexao = mysql.connector.connect(user='root', password='senha', database='NFL') 
        cursor = conexao.cursor()
        print(f"Termo: {termo}")
        busca_jogador = ("SELECT * FROM PESSOA WHERE INSTR(PESSOA.nome, %s) > 0 AND PESSOA.funcao='jogador'")
        cursor.execute(busca_jogador, (termo, ))
        jogadores = cursor.fetchall()
        for row in jogadores:
            print(f"ROW: {row}")
        conexao.commit()
        cursor.close()
        conexao.close()
        return jogadores
