from modelo.fornecedor import Fornecedor
from persistencia.persistencia import Persistencia
import mysql.connector

class FornecedorPersistencia(Persistencia):
    conexao = mysql.connector.connect(user='root', password='senha', database='NFL') 
    cursor = conexao.cursor()
    def gravar(self, entidade: Fornecedor):
        add_fornecedor = ("INSERT INTO FORNECEDOR "
                       "(nome, cnpj, produtos, telefone) "
                       "VALUES (%s, %s, %s, %s)")
        dado_fornecedor = (entidade.nome, entidade.cnpj, entidade.produtos, entidade.telefone)
        self.cursor.execute(add_fornecedor, dado_fornecedor)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
    
    def apagar(self, entidade: Fornecedor):
        del_fornecedor = ("DELETE FROM FORNECEDOR WHERE CNPJ=%s")
        self.cursor.execute(del_fornecedor, entidade.cnpj)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
    
    def buscar(self, entidade: Fornecedor):
        busca_fornecedor = ("SELECT * FROM FORNECEDOR WHERE NOME=%s")
        self.cursor.execute(busca_fornecedor, entidade.nome)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
