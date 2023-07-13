from time import sleep
import mysql.connector
from Admin import *
from mensagemSistema import *
from CadastrarRastrear import *
from CadastroItems import *
from CadastroUsuarios import *

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="trabalhofinal",
)

cursor = conexao.cursor()

# CRUD


# CREATE
def cadastrarAdmin():
    try:
        nome = input("Nome: ")
        cargo = input("Cargo: ")
        setor = input("Setor: ")
        login = input("Login: ")
        email = input("Email: ")
        password = input("Senha: ")
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
        ProgramaAdmin()
    except:
        mensagemErro()
        cadastrarAdmin()


# READ
def loginAdmin():
    login = input("Login: ")
    senha = input("Senha: ")
    comando = "SELECT * FROM usuario WHERE login = %s AND password = %s"
    valores = (login, senha)
    cursor.execute(comando, valores)
    conta = cursor.fetchall()
    if conta:
        if conta[0][7] != "Admin":
            print("A conta em questão não possui permissões de administrador")
        elif conta[0][7] == "Admin":
            verificar = int(
                input(f"Seu nome é {conta[0][1]}?\n1 - Sim\n2 - Não\nEscolha: ")
            )
            if verificar == 1:
                ProgramaAdmin()
            elif verificar == 2:
                continuar = int(
                    input("Deseja tentar logar novamente?\n1 - Sim\n2 - Não\nEscolha: ")
                )
                if continuar == 1:
                    loginAdmin()
                elif continuar == 2:
                    pass
    else:
        print("Login e/ou senha incorretos.")
        sleep(2)
        loginAdmin()


# UPDATE
def atualizarCadastroAdmin():
    nomeAtt = input("Qual admin deseja atualizar? ")
    setorAtt = input("Qual o setor? ")
    while True:
        comando = "SHOW COLUMNS FROM usuario"
        cursor.execute(comando)
        atualizar = cursor.fetchall()
        atualizar.pop(0)
        for indice, colunas in enumerate(atualizar, start=1):
            print(f"{indice} - {colunas[0]}", end=" | ".capitalize())
        colunaAtt = input("Informe o número da coluna a ser atualizada: ")
        if 1 <= int(colunaAtt) <= len(atualizar):
            if int(colunaAtt) == 7 or colunaAtt.upper() == "PERMISSAO":
                escolha = input(
                    f"Informe o novo valor para a coluna {atualizar[int(colunaAtt) - 1][0]}:\n1- Admin\n2 - Usuario "
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
                    atualizarCadastroAdmin()
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
                    atualizarCadastroAdmin()
        else:
            print("Número da coluna inválido.")
        continuar = input("Deseja atualizar outra coluna?\n1 - Sim\n2 - Não\nEscolha: ")
        if int(continuar) == 2 or continuar.upper().startswith("N"):
            break
        elif int(continuar) == 2 and int(continuar) == 1 and continuar.upper()[0] != "S":
            mensagemErro()
            break
        ProgramaAdmin()


# DELETE
def deletarAdmin():
    nomeExcluir = input("Nome: ")
    setorExcluir = input("Setor: ")
    try:
        comando = f"DELETE FROM usuario WHERE nome = '{nomeExcluir}' AND setor = '{setorExcluir}'"
        cursor.execute(comando)
        conexao.commit()
        print("Admin excluído com sucesso!")
        ProgramaAdmin()
    except:
        mensagemErro()
        sleep(2)
        ProgramaAdmin()


# Programa
def ProgramaAdmin():
    escolha = int(
        input(
            "O que deseja visualizar:\n1 - Gerenciamento de Estoque\n2 - Gerenciamento de Rastreamento\n3 - Gerenciamento de Admin\n4 - Gerenciamento de Usuários\n5 - Sair\nEscolha: "
        )
    )
    if escolha == 1:
        EstoqueAdmin()
    elif escolha == 2:
        RastrearAdmin()
    elif escolha == 3:
        escolha = int(input("O que deseja fazer:\n1 - Cadastrar novo Admin\n2 - Atualizar Cadastro de Admin\n3 - Deletar cadastro de Admin\nEscolha: "))
        if escolha == 1:
            cadastrarAdmin()
        elif escolha == 2:
            atualizarCadastroAdmin()
        elif escolha == 3:
            deletarAdmin()
    elif escolha == 4:
        ProgramaUsuarioAdmin()
    elif escolha == 5:
        return
    else:
        print("Escolha Inválida!")
        sleep(2)
        ProgramaAdmin()
