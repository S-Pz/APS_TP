"""
Feito por:  Leonardo da Silva Vieira
            Marco Antonio de Abreu Barbosa
            Pedro Otavio Ferreira Pereira
            Renan Aguiar Chagas
            Savio Francisco Cirino da Paz
"""
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'NFL'

TABLES = {}
TABLES['PESSOA'] = (
        "CREATE TABLE `PESSOA` ("
         "`nome` varchar(30) NOT NULL,"
         "`cpf` varchar(15) NOT NULL,"
         "`data_nasc` date NOT NULL,"
         "`salario` decimal(12, 2) NOT NULL,"
         "`telefone` varchar(20) NOT NULL,"
         "`funcao` varchar(20) NOT NULL,"
         "FOREIGN KEY(`cpf`) REFERENCES USUARIO(`login`)"
         ") DEFAULT CHARSET = utf8"
        )

TABLES['USUARIO'] = (
        "CREATE TABLE `USUARIO` ("
        "`tipo` enum('ADMIN', 'NORMAL') NOT NULL,"
        "`login` varchar(30) NOT NULL,"
        "`senha` varchar(30) NOT NULL,"
        "PRIMARY KEY(`login`)"
        ") DEFAULT CHARSET = utf8"
        )

TABLES['FORNECEDOR'] = (
        "CREATE TABLE `FORNECEDOR` ("
        "`nome` varchar(30) NOT NULL,"
        "`cnpj` varchar(20) NOT NULL,"
        "`telefone` varchar(20) NOT NULL,"
        "PRIMARY KEY(`cnpj`),"
        "UNIQUE KEY `nome` (`nome`)"
        ") DEFAULT CHARSET = utf8"
        )

TABLES['PRODUTO'] = (
        "CREATE TABLE `PRODUTO` ("
        "`nome` varchar(30) NOT NULL,"
        "`preco` decimal(11,2) NOT NULL,"
        "`qtd` date NOT NULL,"
        "`cnpj_forn` varchar(30) NOT NULL,"
        "UNIQUE KEY `nome` (`nome`),"  
        "FOREIGN KEY(`cnpj_forn`) REFERENCES FORNECEDOR(`cnpj`)"
        ") DEFAULT CHARSET = utf8"
        )


TABLES['PATROCINADOR'] = (
        "CREATE TABLE `PATROCINADOR` ("
        "`nome` varchar(30) NOT NULL,"
        "`telefone` varchar(20) NOT NULL,"
        "`cnpj` varchar(20) NOT NULL,"
        "`valor_contrato` decimal(12, 2) NOT NULL,"
        "`local_merchan` varchar(20) NOT NULL,"
        "UNIQUE KEY `nome` (`nome`),"
        "PRIMARY KEY(`cnpj`)"
        ") DEFAULT CHARSET = utf8"
        )

cnx = mysql.connector.connect(user='root', host='localhost', port='3306', password='senha')
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()

from visao.mainvisao import MainVisao
MainVisao().menu()
