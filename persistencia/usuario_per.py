from modelo.usuario import Usuario
from persistencia.persistencia import Persistencia
import mysql.connector

class UsuarioPersistencia(Persistencia):
    def gravar(self, entidade: Usuario):
        conexao = mysql.connector.connect(user='root', password='Senha#123', database='NFL') 
        cursor = conexao.cursor()
        add_usuario = ("INSERT INTO USUARIO "
                       "(nome, tipo, login, senha) "
                       "VALUES (%s, %s, %s, %s)")
        dado_usuario = (entidade.nome, entidade.tipo, entidade.login, entidade.senha)
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
        conexao = mysql.connector.connect(user='root', password='Senha#123', database='NFL') 
        cursor = conexao.cursor()
        try: 
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
            print(f"Usuário não deletado")
            return False
    
    def buscar(self, nome: str, *args): # True: buscar banco, False: buscar usuario
        conexao = mysql.connector.connect(user='root', password='Senha#123', database='NFL') 
        cursor = conexao.cursor()
        print(f"Len args: {len(args)} args: {args[0]}")

        # args [0][1]: True ou False; args[0][0]: senha
        if len(args[0]) > 0:
            if args[0][1]:
                busca_banco = ("SELECT * FROM USUARIO WHERE LOGIN=%s AND SENHA=%s")
                cursor.execute(busca_banco, (nome, args[0][0]))
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
        else: 
            busca_usuario = ("SELECT * FROM USUARIO WHERE NOME LIKE %s")
            cursor.execute(busca_usuario, (nome + "%",))
            usuarios = cursor.fetchall()
            cursor.close()
            conexao.close()
            return usuarios

        print(f"Usuário não está presente no banco")
        cursor.close()
        conexao.close()
        return False
