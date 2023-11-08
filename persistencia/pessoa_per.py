from modelo.pessoa import Pessoa
from persistencia.persistencia import Persistencia
import mysql.connector

class PessoaPersistencia(Persistencia):
    def gravar(self, entidade: Pessoa) -> bool:
        conexao = mysql.connector.connect(user='root', password='Senha#123', database='NFL') 
        cursor = conexao.cursor()
        add_pessoa = ("INSERT INTO PESSOA"
                     "(nome, cpf, data_nasc, salario, telefone, funcao)"
                     "VALUES (%s, %s, %s, %s, %s, %s)")
        dado_pessoa = (entidade.nome, entidade.cpf, entidade.data_nasc, entidade.salario, entidade.telefone, entidade.funcao)
        try:
            cursor.execute(add_pessoa, dado_pessoa)
            print(f"Cadastrando pessoa")
            conexao.commit()
            cursor.close()
            conexao.close()
            return True
        except mysql.connector.errors.IntegrityError:
            print(f"Pessoa já presente no banco")
            conexao.commit()
            cursor.close()
            conexao.close()
            return False

    def apagar(self, cpf: str):
        conexao = mysql.connector.connect(user='root', password='Senha#123', database='NFL') 
        cursor = conexao.cursor()
        del_pessoa = ("DELETE FROM PESSOA WHERE CPF=%s")
        try:
            cursor.execute(del_pessoa, (cpf,))
            conexao.commit()
            cursor.close()
            conexao.close()
            print(f"Pessoa excluída com sucesso")
            return True
        except:
            print(f"Pessoa não pode ser excluída")
            conexao.commit()
            cursor.close()
            conexao.close()
            return False
    
    def buscar(self, termo: str):
        conexao = mysql.connector.connect(user='root', password='Senha#123', database='NFL') 
        cursor = conexao.cursor()
        print(f"Termo: {termo}")
        busca_pessoa = ("SELECT * FROM PESSOA WHERE NOME LIKE %s")
        cursor.execute(busca_pessoa, (termo + "%",))
        pessoas = cursor.fetchall()
        for row in pessoas:
            print(f"ROW: {row}")
        conexao.commit()
        cursor.close()
        conexao.close()
        return pessoas
