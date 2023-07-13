from time import sleep
import mysql.connector
from Item import *
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
def cadastrarItem():
    linha()
    nome = input("Nome do item: ")
    quantidade = int(input("Quantidade no Estoque: "))
    preco = float(input("Preço: "))
    vendasFeitas = int(input("Vendas realizadas: "))
    item = Item(nome, quantidade, preco, vendasFeitas)
    try:
        comando = "INSERT INTO itens (nome, quantidade, preco, vendasFeitas) VALUES (%s, %s, %s, %s)"
        valores = (item.nome, item.quantidade, item.preco, item.vendasFeitas)
        cursor.execute(comando, valores)
        conexao.commit()
        print("Item cadastrado com sucesso!")
        continuar = input("Deseja cadastrar outro item?\n1 - Sim\n2 - Não\nEscolha: ")
        if int(continuar) == 2 or continuar.upper().startswith("N"):
            return
        elif int(continuar) == 2 and int(continuar) == 1 and continuar.upper()[0] != "S":
            mensagemErro()
            return
        cadastrarItem()
    except:
        mensagemErro()
        cadastrarItem()


# READ
def procurarItem():
    linha()
    nomeItem = input("Nome do item: ")
    linha()
    try:
        comando = "SELECT * FROM itens WHERE nome = %s"
        cursor.execute(comando, (nomeItem,))
        resultados = cursor.fetchall()
        if resultados:
            for itens in resultados:
                for c in range(0, 5):
                    print(itens[c], end=" | ")
        else:
            print("Nenhum item encontrado.")
        pularLinha()
        continuar = input("Deseja fazer outra consulta?\n1 - Sim\n2 - Não\nEscolha: ")
        if int(continuar) == 2 or continuar.upper().startswith("N"):
            return
        elif int(continuar) == 2 and int(continuar) == 1 and continuar.upper()[0] != "S":
            mensagemErro()
            return
        procurarItem()
    except:
        mensagemErro()
        sleep(2)
        procurarItem()


def procurarItemAdmin():
    linha()
    nomeItem = input("Nome do item: ")
    linha()
    try:
        comando = "SELECT * FROM itens WHERE nome = %s"
        cursor.execute(comando, (nomeItem,))
        resultados = cursor.fetchall()
        if resultados:
            for itens in resultados:
                for c in range(0, 5):
                    print(itens[c], end=" | ")
        else:
            print("Nenhum item encontrado.")
        pularLinha()
        continuar = input("Deseja fazer outra consulta?\n1 - Sim\n2 - Não\nEscolha: ")
        if int(continuar) == 2 or continuar.upper().startswith("N"):
            return
        elif int(continuar) == 2 and int(continuar) == 1 and continuar.upper()[0] != "S":
            mensagemErro()
            return
        procurarItemAdmin()
    except:
        mensagemErro()
        sleep(2)
        procurarItem()


# UPDATE
def atualizarItem():
    linha()
    nomeAtt = input("Qual item deseja atualizar? ")
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
                mensagemErro()
                sleep(2)
                atualizarItem()
        else:
            print("Número da coluna inválido.")
        continuar = input("Deseja atualizar outra coluna?\n1 - Sim\n2 - Não\nEscolha: ")
        if int(continuar) == 2 or continuar.upper().startswith("N"):
            return
        elif int(continuar) == 2 and int(continuar) == 1 and continuar.upper()[0] != "S":
            mensagemErro()
            return


# DELETE
def excluirItem():
    linha()
    nomeExcluir = input("Nome: ")
    try:
        comando = f"DELETE FROM itens WHERE nome = %s"
        valores = (nomeExcluir,)
        cursor.execute(comando, valores)
        conexao.commit()
        print("Item excluído com sucesso!")
        continuar = input("Deseja excluir outro item?\n1 - Sim\n2 - Não\nEscolha: ")
        if int(continuar) == 2 or continuar.upper().startswith("N"):
            return
        elif int(continuar) == 2 and int(continuar) == 1 and continuar.upper()[0] != "S":
            mensagemErro()
            return
        excluirItem()
    except:
        mensagemErro()
        excluirItem()



def EstoqueAdmin():
    linha()
    escolha = input(
        "O que quer fazer:\n1 - Cadastrar Novo Item\n2 - Procurar por um Item\n3 - Atualizar Item existente\n4 - Excluir Item\n5 - Sair\nEscolha: "
    )
    if escolha == "1":
        cadastrarItem()
    elif escolha == "2":
        procurarItemAdmin()
    elif escolha == "3":
        atualizarItem()
    elif escolha == "4":
        excluirItem()
    elif escolha == "5":
        return
    else:
        print("Opção inválida.")
        EstoqueAdmin()