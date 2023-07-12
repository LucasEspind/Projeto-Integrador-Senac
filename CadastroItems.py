import mysql.connector
from Item import *

# CRUD

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Senac2021",
    database = "trabalhofinal",
)


cursor = conexao.cursor()

# CREATE

nome = input( "Qual nome do item? ")
quantidade = int(input("Qual a quantidade? "))
preco = float(input("Qual o preco? "))
vendasFeitas = int(input("Quantas vendas foram feitas? "))
item = Item(nome,quantidade,preco,vendasFeitas)
comando = f"INSERT INTO itens (nome, quantidade, preco, vendasFeitas) VALUES ('{item.nome}', '{item.quantidade}', '{item.preco}','{item.vendasFeitas}')"
cursor.execute(comando)
conexao.commit()

# READ

comando = f"SELECT * FROM itens"
cursor.execute(comando)
for i in cursor.fetchall():
    print(i[1])

# UPDATE

comando = f"UPDATE itens SET nome = prego WHERE quantidade = 1"
cursor.execute(comando)
conexao.commit()

# DELETE
comando = f"DELETE FROM itens WHERE nome = prego"
cursor.execute(comando)
conexao.commit()