from modelo.fornecedor import Fornecedor
from persistencia.persistencia import Persistencia
import mysql.connector

class FornecedorPersistencia(Persistencia):
    def gravar(self, entidade: Fornecedor):
        conexao = mysql.connector.connect(user='root', password='Senha#123', database='NFL') 
        cursor = conexao.cursor()
        add_fornecedor = ("INSERT INTO FORNECEDOR "
                       "(nome, cnpj, telefone) "
                       "VALUES (%s, %s, %s)")
        dado_fornecedor = (entidade.nome, entidade.cnpj, entidade.telefone)
        print(f"Dados fornecedor: {dado_fornecedor}")
        try:
            cursor.execute(add_fornecedor, dado_fornecedor)
            print(f"Fornecedor adicionado")
            conexao.commit()
            return True
        except:
            print(f"Erro ao adicionar fornecedor")
            return False
        finally:
            cursor.close()
            conexao.close()
    
    def apagar(self, cnpj: str):
        conexao = mysql.connector.connect(user='root', password='Senha#123', database='NFL') 
        cursor = conexao.cursor()
        try: 
            del_fornecedor = ("DELETE FROM FORNECEDOR WHERE CNPJ=%s")
            cursor.execute(del_fornecedor, (cnpj,))
            conexao.commit()
            if cursor.rowcount != 0 :
                print(f"Fornecedor deletado")
                return True
            else:
                print(f"Fornecedor não encontrado")
                return False
        finally:
            cursor.close()
            conexao.close()
    
    def buscar(self, termo):
        conexao = mysql.connector.connect(user='root', password='Senha#123', database='NFL') 
        cursor = conexao.cursor()
        busca_fornecedor = ("SELECT * FROM FORNECEDOR WHERE NOME LIKE %s")

        try:
            cursor.execute(busca_fornecedor, (termo + "%",))
            resultado = cursor.fetchall()
            return resultado
        except:
            print(f"Fornecedor não encontrado")
            return False
        finally:
            cursor.close()
            conexao.close()
