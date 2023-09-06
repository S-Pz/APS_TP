from modelo.usuario import Usuario
from persistencia.persistencia import Persistencia
import mysql.connector

class UsuarioPersistencia(Persistencia):
    def gravar(self, entidade: Usuario):
        conexao = mysql.connector.connect(user='root', password='senha', database='NFL') 
        cursor = conexao.cursor()
        add_usuario = ("INSERT INTO USUARIO "
                       "(tipo, login, senha) "
                       "VALUES (%s, %s, %s)")
        dado_usuario = (entidade.tipo, entidade.login, entidade.senha)
        try:
            cursor.execute(add_usuario, dado_usuario)
            print(f"Cadastrando usuário")
            conexao.commit()
            cursor.close()
            conexao.close()
            return True
        except:
            print(f"Usuário já presente no banco")
            conexao.commit()
            cursor.close()
            conexao.close()
            return False
    
    def apagar(self, login: str):
        conexao = mysql.connector.connect(user='root', password='senha', database='NFL') 
        cursor = conexao.cursor()
        del_pessoa = ("DELETE FROM PESSOA WHERE CPF=%s")
        try: 
            cursor.execute(del_pessoa, (login,))
            del_usuario = ("DELETE FROM USUARIO WHERE LOGIN=%s")
            cursor.execute(del_usuario, (login,))
            conexao.commit()
            cursor.close()
            conexao.close()
            print(f"Usuário deletado")
            return True
        except:
            conexao.commit()
            cursor.close()
            conexao.close()
            print(f"Usuário deletado")
            return False
    
    def buscar(self, nome: str, senha: str):
        conexao = mysql.connector.connect(user='root', password='senha', database='NFL') 
        cursor = conexao.cursor()
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
        return False
