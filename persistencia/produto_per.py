from modelo.produto import Produto
from persistencia.persistencia import Persistencia
import mysql.connector

class ProdutoPersistencia(Persistencia):
    def gravar(self, entidade: Produto):
        conexao = mysql.connector.connect(user='root', password='Senha#123', database='NFL') 
        cursor = conexao.cursor()
        add_produto = ("INSERT INTO PRODUTO "
                       "(nome, preco, qtd, cnpj_forn) "
                       "VALUES (%s, %s, %s, %s)")
        dado_produto = (entidade.nome, entidade.preco, entidade.qtd, entidade.chave)
        print(f"Dado produto: {dado_produto}")
        try:
            cursor.execute(add_produto, dado_produto)
            print(f"Produto adicionado")
            conexao.commit()
            return True
        except:
            print(f"Erro ao adicionar produto")
            return False
        finally:
            cursor.close()
            conexao.close()
    
    def apagar(self, entidade: Produto):
        conexao = mysql.connector.connect(user='root', password='Senha#123', database='NFL') 
        cursor = conexao.cursor()
        try: 
            del_produto = ("DELETE FROM PRODUTO WHERE CHAVE=%s")
            cursor.execute(del_produto, (entidade.chave,))
            conexao.commit()
            print(f"Produto deletado")
            return True
        except:
            print(f"Erro ao deletar produto")
            return False
        finally:
            cursor.close()
            conexao.close()

    def buscar(self, entidade: Produto):
        conexao = mysql.connector.connect(user='root', password='Senha#123', database='NFL') 
        cursor = conexao.cursor()
        busca_produto = ("SELECT * FROM PRODUTO WHERE NOME=%s")
        try:
            cursor.execute(busca_produto, (entidade.nome,))
            resultado = cursor.fetchall()
            return resultado
        except:
            print(f"Produto não encontrado")
            return False
        finally:
            cursor.close()
            conexao.close()
