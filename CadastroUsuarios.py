from time import sleep
import mysql.connector
from Usuario import *
from mensagemSistema import *
from CadastrarRastrear import *
from CadastroItems import *

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "trabalhofinal",
)

cursor = conexao.cursor()

# CRUD

# CREATE

def cadastrarUsuario():
    try:
        nome = input( "Nome: ")
        cargo = input( "Cargo: ")
        setor = input( "Setor: ")
        email = input( "Email: ")
        login = input( "Login: ")
        password = input( "Senha: ")
        usuario = Usuario(nome, cargo, setor, email, login, password)
        comando = "INSERT INTO usuario (nome, cargo, setor, email, login, password, permissao) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (usuario.nome, usuario.cargo, usuario.setor, usuario.email, usuario.login, usuario.password, usuario._permissao)
        cursor.execute(comando, valores)
        conexao.commit()
        ProgramaUsuario()
    except:
        mensagemErro()
        cadastrarUsuario()

# Read

def loginUsuario():
    login = str(input("Login: "))
    senha = str(input("Senha: "))
    try:
        comando = "SELECT * FROM usuario WHERE login=%s AND password=%s"
        valores = (login, senha)
        cursor.execute(comando, valores)
        conta = cursor.fetchall()
        if conta:
            ProgramaUsuario()
        else:
            mensagemErro()
            loginUsuario()
    except:
        mensagemErro()
        loginUsuario()

# UPDATE

def atualizarCadastroUsuario():
    nomeAtt = str(input("Qual admin deseja atualizar? "))
    setorAtt = str(input("Qual o setor? "))
    while True:
        comando = "SHOW COLUMNS FROM usuario"
        cursor.execute(comando)
        atualizar = cursor.fetchall()
        atualizar.pop(0)
        for indice, colunas in enumerate(atualizar, start=1):
            print(f"{indice} - {colunas[0]}", end=" | ".capitalize())

        colunaAtt = str(input("Informe o número da coluna a ser atualizada: "))

        if 1 <= int(colunaAtt) <= len(atualizar):
            if int(colunaAtt) == 7 or colunaAtt.upper() == "PERMISSAO":
                escolha = str(input("Informe o novo valor para a coluna {}:\n1- Admin\n2 - Usuario ".format(colunas[int(colunaAtt) - 1][0])))
                if int(escolha) == 1 or escolha.upper().startswith('A'):
                    novoValor = "Admin"
                elif int(escolha) == 2 or escolha.upper().startswith('U'):
                    novoValor = "User"
                else:
                    print("Opção inválida.")
                    continue

                try:
                    consulta_update = "UPDATE usuario SET {} = %s WHERE nome = %s AND setor = %s".format(colunas[int(colunaAtt) - 1][0])
                    valores = (novoValor.encode(), nomeAtt, setorAtt)

                    cursor.execute(consulta_update, valores)
                    conexao.commit()

                    print("Atualização concluída.")
                except:
                    mensagemErro()
                    sleep(2)
                    atualizarCadastroUsuario()
            else:
                colunaEscolhida = atualizar[int(colunaAtt) - 1][0]

                novoValor = input("Informe o novo valor para a coluna {}: ".format(colunaEscolhida))

                try:
                    consulta_update = "UPDATE usuario SET {} = %s WHERE nome = %s AND setor = %s".format(colunas[int(colunaAtt) - 1][0])
                    valores = (novoValor.encode(), nomeAtt, setorAtt)

                    cursor.execute(consulta_update, valores)
                    conexao.commit()

                    print("Atualização concluída.")
                except:
                    mensagemErro()
                    sleep(2)
                    atualizarCadastroUsuario()
        else:
            print("Número da coluna inválido.")
        continuar = str(input("Deseja atualizar outra coluna?\n1 - Sim\n2 - Não\nEscolha: "))
        if int(continuar) == 2 or continuar.upper().startswith('N'):
            break
        ProgramaUsuario()


# DELETE

def deletarUsuario():
    nomeExcluir = str(input("Nome: "))
    setorExcluir = str(input("Setor: "))
    try:
        comando = f"DELETE FROM usuario WHERE nome = '{nomeExcluir}', setor = '{setorExcluir}'"
        cursor.execute(comando)
        conexao.commit()
        print("Usuario excluido com sucesso!")
        ProgramaUsuario()
    except:
        sleep(2)
        ProgramaUsuario()


#Programa

def ProgramaUsuario():
    escolha = int(input("O que deseja visualizar:\n1 - Gerenciamento de Estoque\n2 - Gerenciamento de Rastreamento\nEscolha: "))
    if escolha == 1:
        procurarItem()
    elif escolha == 2:
        verificarPedido()
    