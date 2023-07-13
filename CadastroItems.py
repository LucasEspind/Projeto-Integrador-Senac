from time import sleep
import mysql.connector
from Item import *
from mensagemSistema import *

# CRUD

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "trabalhofinal",
)


cursor = conexao.cursor()

# CREATE
def cadastrarItem():
    nome = input( "Nome do item: ")
    quantidade = int(input("Quantidade no Estoque: "))
    preco = float(input("Preço: "))
    vendasFeitas = int(input("Vendas realizadas: "))
    item = Item(nome, quantidade, preco, vendasFeitas)
    try:
        comando = f"INSERT INTO itens (nome, quantidade, preco, vendasFeitas) VALUES %s, %s, %s, %s)"
        valores = (item.nome, item.quantidade, item.preco, item.vendasFeitas)
        cursor.execute(comando, valores)
        conexao.commit()
    except:
        mensagemErro()
        sleep(2)
        cadastrarItem()

# READ

def procurarItem():
    nomeItem = str(input("Nome do item: "))
    try:
        comando = f"SELECT * FROM itens WHERE nome = %s"
        cursor.execute(comando, (nomeItem,))
        for i in cursor.fetchall():
            print(i[1])
    except:
        mensagemErro()
        sleep(2)
        procurarItem()

# UPDATE
def atualizarItem():
    nomeAtt = str(input("Qual item deseja atualizar? "))

    while True:
        comando = "SHOW COLUMNS FROM itens"
        cursor.execute(comando)
        atualizar = cursor.fetchall()
        atualizar.pop(0)
        
        for indice, colunas in enumerate(atualizar, start=1):
            print(f"{indice} - {colunas[0]}", end=" | ".capitalize())

        colunaAtt = str(input("Informe o número da coluna a ser atualizada: "))

        if 1 <= int(colunaAtt) <= len(atualizar):
            colunaEscolhida = atualizar[int(colunaAtt) - 1][0]

            novoValor = input("Informe o novo valor para a coluna {}: ".format(colunaEscolhida))

            try:
                consulta_update = "UPDATE itens SET {} = %s WHERE nome = %s".format(colunaEscolhida)
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

        continuar = str(input("Deseja atualizar outra coluna?\n1 - Sim\n2 - Não\nEscolha: "))
        if int(continuar) == 2 or continuar.upper().startswith('N'):
            break

    EstoqueAdmin()


# DELETE
def excluirItem():
    nomeExcluir = str(input("Nome: "))
    try:
        comando = f"DELETE FROM itens WHERE nome = %s"
        valores = (nomeExcluir,)
        cursor.execute(comando, valores)
        conexao.commit()
        print("Item excluido com sucesso!")
        EstoqueAdmin()
    except:
        sleep(2)
        EstoqueAdmin()


def EstoqueAdmin():
    escolha = str(input("O que quer fazer:\n1 - Cadastrar Novo Item\n2 - Procurar por um Item\n3 - Atualizar Item existente\n4 - Excluir Item\nEscolha: "))
    if escolha == '1':
        cadastrarItem()
    elif escolha == '2':
        procurarItem()
    elif escolha == '3':
        atualizarItem()
    elif escolha == '4':
        excluirItem()
    else:
        print("Opção inválida.")
        EstoqueAdmin()