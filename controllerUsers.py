from time import sleep
import mysql.connector
from modelAdmin import Admin
from modelUsuario import *
from mensagemSistema import *


conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="trabalhofinal",
)

cursor = conexao.cursor()

# CRUD

# CREATE


def registerUser(nome, cargo, setor, email, login, password, tipo):
    try:
        if tipo:
            usuario = Admin(nome, cargo, setor, email, login, password)
            comando = "INSERT INTO usuario (nome, cargo, setor, email, login, password, permissao) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            valores = (
                usuario.nome,
                usuario.cargo,
                usuario.setor,
                usuario.email,
                usuario.login,
                usuario.password,
                usuario._permissao,
            )
            cursor.execute(comando, valores)
            conexao.commit()
            return True
        else:
            usuario = Usuario(nome, cargo, setor, email, login, password)
            comando = "INSERT INTO usuario (nome, cargo, setor, email, login, password, permissao) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            valores = (
                usuario.nome,
                usuario.cargo,
                usuario.setor,
                usuario.email,
                usuario.login,
                usuario.password,
                usuario._permissao,
            )
            cursor.execute(comando, valores)
            conexao.commit()
            return True
    except:
        return False


# Read


def userLogin(loginUsuario, senhaUsuario):      
    comando = "SELECT * FROM usuario WHERE login=%s AND password=%s"
    valores = (loginUsuario, senhaUsuario)
    cursor.execute(comando, valores)
    conta = cursor.fetchone()
    if conta:
        return conta
    else:
        return False


def showUser(Nome, Setor):
    comando = "SELECT * FROM usuario WHERE nome=%s AND setor=%s"
    valores = (Nome, Setor)
    cursor.execute(comando, valores)
    conta = cursor.fetchone()
    if conta:
        return conta
    else:
        return False


# UPDATE


def updateUser(nomeAtt, setorAtt):
    comando = "SELECT * FROM usuario WHERE nome = %s AND setor = %s"
    valores = (nomeAtt, setorAtt)
    cursor.execute(comando, valores)
    conta = cursor.fetchone()
    if conta:
        while True:
            comando = "SHOW COLUMNS FROM usuario"
            cursor.execute(comando)
            atualizar = cursor.fetchall()
            atualizar.pop(0)
            for indice, colunas in enumerate(atualizar, start=1):
                print(f"{indice} - {colunas[0]}", end=" | ".capitalize())
            print()

            colunaAtt = input("\nInforme o número da coluna a ser atualizada: ")

            if 1 <= int(colunaAtt) <= len(atualizar):
                if int(colunaAtt) == 7 or colunaAtt.upper() == "PERMISSAO":
                    escolha = input(
                        "Informe o novo valor para a coluna {}:\n1- Admin\n2 - Usuario ".format(
                            atualizar[int(colunaAtt) - 1][0]
                        )
                    )
                    if int(escolha) == 1 or escolha.upper().startswith("A"):
                        novoValor = "Admin"
                    elif int(escolha) == 2 or escolha.upper().startswith("U"):
                        novoValor = "User"
                    else:
                        print("Opção inválida.")
                        continue

                    try:
                        consulta_update = "UPDATE usuario SET {} = %s WHERE nome = %s AND setor = %s".format(
                            atualizar[int(colunaAtt) - 1][0]
                        )
                        valores = (novoValor.encode(), nomeAtt, setorAtt)

                        cursor.execute(consulta_update, valores)
                        conexao.commit()

                        print("Atualização concluída.")
                    except:
                        mensagemErro()
                        sleep(2)
                else:
                    colunaEscolhida = atualizar[int(colunaAtt) - 1][0]

                    novoValor = input(
                        "Informe o novo valor para a coluna {}: ".format(colunaEscolhida)
                    )

                    try:
                        consulta_update = "UPDATE usuario SET {} = %s WHERE nome = %s AND setor = %s".format(
                            colunaEscolhida
                        )
                        valores = (novoValor.encode(), nomeAtt, setorAtt)

                        cursor.execute(consulta_update, valores)
                        conexao.commit()

                        print("Atualização concluída.")
                    except:
                        mensagemErro()
                        sleep(2)
            else:
                print("Número da coluna inválido.")

            continuar = input("Deseja atualizar outra coluna?\n1 - Sim\n2 - Não\nEscolha: ")
            if int(continuar) == 2 or continuar.upper().startswith("N"):
                break
        return True
    else:
        return False


# DELETE


def removeUser(nomeExcluir, setorExcluir):
    try:
        comando = f"DELETE FROM usuario WHERE nome = %s AND setor = %s"
        valores = (nomeExcluir, setorExcluir)
        cursor.execute(comando, valores)
        conexao.commit()
        return True
    except:
        return False