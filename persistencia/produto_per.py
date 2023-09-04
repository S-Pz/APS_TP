from modelo.produto import Produto
from persistencia.persistencia import Persistencia
import mysql.connector

class ProdutoPersistencia(Persistencia):
    conexao = mysql.connector.connect(user='root', password='senha', database='NFL') 
    cursor = conexao.cursor()

    def gravar(self, entidade: Produto):
        add_produto = ("INSERT INTO PRODUTO "
                       "(nome, preco, qtd, chave) "
                       "VALUES (%s, %s, %s, %s)")
        dado_produto = (entidade.nome, entidade.preco, entidade.qtd, entidade.chave)
        self.cursor.execute(add_produto, dado_produto)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
    
    def apagar(self, entidade: Produto):
        del_produto = ("DELETE FROM PRODUTO WHERE CPF=%s")
        self.cursor.execute(del_produto, entidade.pessoa.cpf)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
    
    def buscar(self, entidade: Produto):
        busca_produto = ("SELECT * FROM PRODUTO WHERE NOME=%s")
        self.cursor.execute(busca_produto, entidade.pessoa.nome)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
