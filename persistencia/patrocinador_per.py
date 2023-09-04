from modelo.patrocinador import Patrocinador
from persistencia.persistencia import Persistencia
import mysql.connector

class PatrocinadorPersistencia(Persistencia):
    conexao = mysql.connector.connect(user='root', password='senha', database='NFL') 
    cursor = conexao.cursor()

    def gravar(self, entidade: Patrocinador):
        add_patrocinador = ("INSERT INTO PATROCINADOR "
                       "(nome, cnpj, telefone, valor_contrato, local_merchan) "
                       "VALUES (%s, %s, %s, %s, %s)")
        dado_patrocinador = (entidade.nome, entidade.cnpj, entidade.telefone, entidade.valor_contrato, entidade.local_merchan)
        self.cursor.execute(add_patrocinador, dado_patrocinador)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
    
    def apagar(self, entidade: Patrocinador):
        del_patrocinador = ("DELETE FROM PATROCINADOR WHERE CNPJ=%s")
        self.cursor.execute(del_patrocinador, entidade.cnpj)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
    
    def buscar(self, entidade: Patrocinador):
        busca_patrocinador = ("SELECT * FROM PATROCINADOR WHERE NOME=%s")
        self.cursor.execute(busca_patrocinador, entidade.nome)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
