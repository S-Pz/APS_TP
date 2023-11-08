from modelo.patrocinador import Patrocinador
from persistencia.persistencia import Persistencia
import mysql.connector

class PatrocinadorPersistencia(Persistencia):
<<<<<<< HEAD
    def gravar(self, entidade: Patrocinador):
        conexao = mysql.connector.connect(user='root', password='Senha#123', database='NFL') 
        cursor = conexao.cursor()
=======
    conexao = mysql.connector.connect(user='root', password='senha', database='NFL') 
    cursor = conexao.cursor()

    def gravar(self, entidade: Patrocinador):
>>>>>>> origin/main
        add_patrocinador = ("INSERT INTO PATROCINADOR "
                       "(nome, cnpj, telefone, valor_contrato, local_merchan) "
                       "VALUES (%s, %s, %s, %s, %s)")
        dado_patrocinador = (entidade.nome, entidade.cnpj, entidade.telefone, entidade.valor_contrato, entidade.local_merchan)
<<<<<<< HEAD
        try:
            cursor.execute(add_patrocinador, dado_patrocinador)
            print(f"Patrocinador adicionado")
            conexao.commit()
            return True
        except:
            print(f"Erro ao adicionar patrocinador")
            return False
        finally:
            cursor.close()
            conexao.close()
    
    def apagar(self, cnpj: str):
        conexao = mysql.connector.connect(user='root', password='Senha#123', database='NFL') 
        cursor = conexao.cursor()
        try: 
            del_patrocinador = ("DELETE FROM PATROCINADOR WHERE CNPJ=%s")
            cursor.execute(del_patrocinador, (cnpj,))
            conexao.commit()
            if cursor.rowcount != 0 :
                print(f"Patrocinador deletado")
                return True
            else:
                print(f"Patrocinador não encontrado")
                return False
        finally:
            cursor.close()
            conexao.close()
    
    def buscar(self, termo):
        conexao = mysql.connector.connect(user='root', password='Senha#123', database='NFL') 
        cursor = conexao.cursor()
        busca_patrocinador = ("SELECT * FROM PATROCINADOR WHERE NOME LIKE %s")
        try:
            cursor.execute(busca_patrocinador, (termo + "%",))
            resultado = cursor.fetchall()
            return resultado
        except:
            print(f"Patrocinador não encontrado")
            return False
        finally:
            cursor.close()
            conexao.close()
=======
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
>>>>>>> origin/main
