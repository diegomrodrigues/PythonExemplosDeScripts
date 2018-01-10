# -*- coding: utf-8 -*-
'''
Utilizando o banco de dados MySQL no Python

pip install mysqlclient

Artigo: https://www.linkedin.com/pulse/...................

Diego Mendes Rodrigues
'''
import MySQLdb

# Conectando no servidor MySQL
db = MySQLdb.connect(host="192.168.*****", # IP do Servidor
                     user="root",          # Usuário
                     passwd="*****",       #Senha
                     db="")                #Database

# Criando um cursor
cursor = db.cursor()

# Executa uma instrução SQL
cursor.execute("SELECT user,host FROM mysql.user")

# Armazenando o resultset como uma tupla
result = cursor.fetchall()

# Navegandi pelo resultset
print("USER - HOST")
for record in result:
    print(record[0], " - " , record[1])