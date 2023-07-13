from asyncio import sleep
import mysql.connector
from Rastrear import Rastrear
from mensagemSistema import mensagemErro, pularLinha

# CRUD

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="trabalhofinal",
)

cursor = conexao.cursor()


def realizarPedido():
    while True:
        id = input("Qual o id do produto a ser pedido: ")
        if id.isdigit():
            rastrear = Rastrear(id)
            try:
                comando = "INSERT INTO rastreamento (id_rastreamento, status_entrega) VALUES (%s, %s)"
                valores = (rastrear.idItem, rastrear.statusEntrega)
                cursor.execute(comando, valores)
                conexao.commit()
            except:
                mensagemErro()
                sleep(2)
                continue
            continuar = input(
                "Deseja fazer outra consulta?\n1 - Sim\n2 - Não\nEscolha: "
            )
            if int(continuar) == 2 or continuar.upper().startswith("N"):
                break
            elif int(continuar) == 2 and int(continuar) == 1 and continuar.upper()[0] != "S":
                mensagemErro()
                break
        else:
            mensagemErro()


def verificarPedido():
    while True:
        idItem = int(input("Qual o id do item que deseja rastrear? "))
        try:
            comando = "SELECT * FROM rastreamento WHERE id_rastreamento = %s"
            cursor.execute(comando, (idItem,))
            resultados = cursor.fetchall()
            if resultados:
                for itens in resultados:
                    for c in range(0, 5):
                        print(itens[c], end=" | ")
            else:
                print("Nenhum item encontrado.")
            pularLinha()
            continuar = input(
                "Deseja fazer outra consulta?\n1 - Sim\n2 - Não\nEscolha: "
            )
            if int(continuar) == 2 or continuar.upper().startswith("N"):
                break
            elif int(continuar) == 2 and int(continuar) == 1 and continuar.upper()[0] != "S":
                mensagemErro()
                break
        except:
            mensagemErro()
            sleep(2)


def verificarPedidoAdmin():
    while True:
        idItem = int(input("Qual o id do item que deseja rastrear? "))
        try:
            comando = "SELECT * FROM rastreamento WHERE id_rastreamento = %s"
            cursor.execute(comando, (idItem,))
            resultados = cursor.fetchall()
            if resultados:
                for rastrear in resultados:
                    for c in range(0, 5):
                        print(rastrear[c], end=" | ")
            else:
                print("Nenhum item encontrado.")
            pularLinha()
            continuar = input(
                "Deseja fazer outra consulta?\n1 - Sim\n2 - Não\nEscolha: "
            )
            if int(continuar) == 2 or continuar.upper().startswith("N"):
                break
            elif int(continuar) == 2 and int(continuar) == 1 and continuar.upper()[0] != "S":
                mensagemErro()
                break
        except:
            mensagemErro()
            sleep(2)


def atualizarPedido():
    idPedido = int(input("Id do item: "))
    while True:
        escolha = str(input("Novo status do pedido:\n1 - Pedido Realizado\n2 - Pedido Entregue\n3 - Pausar Pedido\nEscolha: "))
        if int(escolha) == 1:
            novoStatus = "Pedido Realizado"
            break
        elif int(escolha) == 2:
            novoStatus = "Pedido Entregue"
            break
        elif int(escolha) == 3:
            novoStatus = "Pausar Pedido"
            break
        else:
            mensagemErro()
            pass
    try:
        comando = "UPDATE rastreamento SET status_entrega = %s WHERE id_rastreamento = %s"
        valores = (novoStatus, idPedido)
        cursor.execute(comando, valores)
        conexao.commit()
        RastrearAdmin()
    except:
        mensagemErro()
        atualizarPedido()


def excluirPedido():
    try:
        idRastrear = int(input("Qual o ID do item que deseja rastrear? "))
        comando = "DELETE FROM rastreamento WHERE id_rastreamento = %s"
        valores = (idRastrear,)

        cursor.execute(comando, valores)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Pedido excluído com sucesso!")
        else:
            print("Nenhum pedido encontrado com o ID fornecido.")
    except:
        mensagemErro()
        excluirPedido()
    RastrearAdmin()


def RastrearAdmin():
    escolha = input(
        "O que deseja realizar:\n1 - Realizar Pedido\n2 - Verificar Pedido\n3 - Atualizar Pedido\n4 - Excluir Pedido\n5 - Sair\nEscolha: "
    )
    if int(escolha) == 1:
        realizarPedido()
    elif int(escolha) == 2:
        verificarPedido()
    elif int(escolha) == 3:
        atualizarPedido()
    elif int(escolha) == 4:
        excluirPedido()
    elif int(escolha) == 5:
        return
    else:
        mensagemErro()
        RastrearAdmin()
