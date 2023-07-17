from time import sleep
import mysql.connector
from modelItem import *
from mensagemSistema import *

# Estabelecendo a conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="trabalhofinal",
)

cursor = conexao.cursor()


# CREATE
def createItem(nome, quantidade, preco, vendasFeitas):    
    item = Item(nome, quantidade, preco, vendasFeitas)
    try:
        comando = "INSERT INTO itens (nome, quantidade, preco, vendasFeitas) VALUES (%s, %s, %s, %s)"
        valores = (item.nome, item.quantidade, item.preco, item.vendasFeitas)
        cursor.execute(comando, valores)
        conexao.commit()
        return True
    except:
        return False


# READ
def findItem(codigoItem):
    comando = "SELECT * FROM itens WHERE id_item = %s"
    cursor.execute(comando, (codigoItem,))
    resultados = cursor.fetchone()
    if resultados:
        return resultados
    else:
        return False


# UPDATE
def updateItem(nomeAtt):    
    while True:    
        comando = "SHOW COLUMNS FROM itens"
        cursor.execute(comando)
        atualizar = cursor.fetchall()
        atualizar.pop(0)
        for indice, colunas in enumerate(atualizar, start=1):
            print(f"{indice} - {colunas[0]}", end=" | ".capitalize())
        colunaAtt = input("Informe o número da coluna a ser atualizada: ")
        if 1 <= int(colunaAtt) <= len(atualizar):
            colunaEscolhida = atualizar[int(colunaAtt) - 1][0]
            novoValor = input(
                "Informe o novo valor para a coluna {}: ".format(colunaEscolhida)
            )
            try:
                consulta_update = "UPDATE itens SET {} = %s WHERE nome = %s".format(
                    colunaEscolhida
                )
                valores = (novoValor.encode(), nomeAtt)
                cursor.execute(consulta_update, valores)
                conexao.commit()
                print("Atualização concluída.")
            except:
                return False
        else:
            print("Número da coluna inválido.")
        continuar = input("Deseja atualizar outra coluna?\n1 - Sim\n2 - Não\nEscolha: ")
        if int(continuar) == 2 or continuar.upper().startswith("N"):
            return True
        elif int(continuar) == 2 and int(continuar) == 1 and continuar.upper()[0] != "S":
            mensagemErro()
            continue


# DELETE
def deleteItem(codeItem):    
    try:
        comando = f"DELETE FROM itens WHERE nome = %s"
        valores = (codeItem,)
        cursor.execute(comando, valores)
        conexao.commit()
        print("Item excluído com sucesso!")
        
    except:
        mensagemErro()
