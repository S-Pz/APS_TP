from modelo.usuario import Usuario
from mysql.connector.cursor import CursorBase
from persistencia.persistencia import Persistencia
import mysql.connector

class UsuarioPersistencia(Persistencia):
    #conexao = mysql.connector.connect(user='root', password='senha', database='NFL') 
    #cursor = conexao.cursor()
    #print(f"Cursor: {cursor}")

    def gravar(self, entidade: Usuario):
        add_usuario = ("INSERT INTO USUARIO "
                       "(nome, tipo, login, senha) "
                       "VALUES (%s, %s, %s, %s)")
        dado_usuario = (entidade.nome, entidade.tipo, entidade.login, entidade.senha)
        self.cursor.execute(add_usuario, dado_usuario)
        if not self.cursor.fetchone():
            print(f"Cadastrando usuário")
            self.conexao.commit()
            self.cursor.close()
            self.conexao.close()
            return 1
        print(f"Usuário já presente no banco")
        self.cursor.close()
        self.conexao.close()
        return -1
    
    def apagar(self, entidade: Usuario):
        del_usuario = ("DELETE FROM USUARIO WHERE CPF=%s")
        self.cursor.execute(del_usuario, entidade.pessoa.cpf)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
    
    def buscar(self, nome: str, senha: str):
        conexao = mysql.connector.connect(user='root', password='senha', database='NFL') 
        cursor = conexao.cursor()
        print(f"User: {nome}\tSenha: {senha}")
        busca_usuario = ("SELECT * FROM USUARIO WHERE LOGIN=%s AND SENHA=%s")
        cursor.execute(busca_usuario, ( nome, senha ))
        
        row = cursor.fetchone()
        if row and "NORMAL" in row:
            print(f"Usuário normal no banco")
            conexao.commit()
            cursor.close()
            conexao.close()
            return 1
        elif row and "ADMIN" in row:
            print(f"Usuário admin no banco")
            conexao.commit()
            cursor.close()
            conexao.close()
            return 2 
        print(f"Usuário não está presente no banco")
        cursor.close()
        conexao.close()
        return 0
