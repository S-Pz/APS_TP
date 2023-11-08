from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root', password='Senha123!', host='127.0.0.1',database='NFL')
cursor = cnx.cursor()
DB_NAME = 'NFL'

TABLES = {}
TABLES['JOGADOR'] = (
    "CREATE TABLE `JOGADOR` ("
    "  `cpf` varchar(20) NOT NULL,"
    "  `salario` float NOT NULL,"
    "  `nascimento` date NOT NULL,"
    "  `telefone` varchar(30) NOT NULL,"
    "  `numero_camisa` int NOT NULL UNIQUE,"
    "  `funcao` varchar(10) NOT NULL,"
    "  `nome` varchar(30) NOT NULL,"
    "  PRIMARY KEY (`cpf`)"
    ") default charset = utf8;")

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

add_jogador = ("INSERT INTO JOGADOR "
               "(cpf, salario, nascimento, telefone, numero_camisa, funcao, nome) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
cpf = "124"
salario = 10.0
nascimento = date(2000, 1, 1)
telefone = "4002"
numero_camisa = 12
funcao = "zagueiro"
nome = "Rick"
dado_jogador = (cpf, salario, nascimento, telefone, numero_camisa, funcao, nome)
cursor.execute(add_jogador, dado_jogador)
cnx.commit()
cursor.close()
cnx.close()
