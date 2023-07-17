from controllerTracking import *
from controllerItem import *
from controllerUsers import *


def adminMenu():
    while True:
        print("MENU DO ADMIN")
        print("1 - Gerenciar Usuários do sistema  \n2 - Gerenciar os Itens   \n3 - Gerenciar os Rastreamentos \n4 - Sair")
        option = input()
        if(option == "1"):
            userMenu()
        elif(option == "2"):
            itemMenu()
        elif(option == "3"):
            trackingMenu()
        elif(option == "4"):
            break
        else:
            print("Opção inválida!")

# User things

def userMenu():
    while True: 
        print("MENU DO USUARIO")
        print("1 - Cadastrar usuário  \n2 - Remover usuário \n3 - Atualizar usuário \n4 - Exibir usuário \n5 - Sair")
        option = input()
        if(option == "1"):
            registerUserMenu()
        elif(option == "2"):
            removeUserMenu()
        elif(option == "3"):
            updateUserMenu()
        elif(option == "4"):
            showUserMenu()
        elif(option == "5"):
            break
        else:
            print("Opção inválida!")
            

def registerUserMenu():
    while True:
        linha()
        nome = input("Nome: ")
        cargo = input("Cargo: ")
        setor = input("Setor: ")
        email = input("Email: ")
        login = input("Login: ")
        password = input("Senha: ")
        while True:
            print("1 - Admin\n2 - Usuário")
            tipo = input()
            if int(tipo) == 1 or tipo.upper().startswith("A"):
                register = registerUser(nome, cargo, setor, email, login, password, True)
                break
            elif int(tipo) == 2 or tipo.upper().startswith("U"):
                register = registerUser(nome, cargo, setor, email, login, password, False)
                break
            else:
                print("Verifique os dados informados e tente novamente!")
        if register:
            print("Usuário registrado com sucesso!")
            break
        else:
            print("Verifique os dados informados e tente novamente!")

def removeUserMenu():
    while True:
        nomeExcluir = str(input("Nome: "))
        setorExcluir = str(input("Setor: "))
        remove = removeUser(nomeExcluir, setorExcluir)
        if remove:
            print("Usuário excluído com sucesso!")
            break
        else:
            print("Usuário não encontrado! Verifique os dados informados.")

def updateUserMenu():
     while True:
        linha()
        nomeAtt = input("Qual usuário deseja atualizar? ")
        setorAtt = input("Qual o setor? ")
        update = updateUser(nomeAtt, setorAtt)
        if update:
            print("Colunas atualizadas com sucesso!")
            break
        else:
            print("Ocorreu algum erro ou um campo foi preenchido de forma incorreta!")


def showUserMenu():
    Nome = input("Nome do usuário: ")
    Setor = input("Setor do usuário: ")
    results = showUser(Nome, Setor)
    if results:
        for itens in results:
            print(itens, end=" | ")
    else:
        print("Usuário não encontrado!")
# End of User Functions


# Item things

def itemMenu():
    while True:
        print("MENU DO ITEM")
        print("1 - Cadastrar item  \n2 - Remover item \n3 - Listar itens \n4 - Atualizar Item\n 5 - Sair")
        option = input()
        if(option == "1"):
            createItemMenu()
        elif(option == "2"):
            removeItemMenu()
        elif(option == "3"):
            showItemMenu()
        elif(option == "4"):
            updateItemMenu()
        elif(option == "5"):
            break
        else:
            print("Opção inválida!")

def createItemMenu():
    while True:
        nome = input("Nome do item: ")
        quantidade = int(input("Quantidade no Estoque: "))
        preco = float(input("Preço: "))
        vendasFeitas = int(input("Vendas realizadas: "))
        item = createItem(nome, quantidade, preco, vendasFeitas)
        if item:
            print("Item cadastrado com sucesso!")
            continuar = input("Deseja cadastrar outro item?\n1 - Sim\n2 - Não\nEscolha: ")
            if int(continuar) == 2 or continuar.upper().startswith("N"):
                break
            elif int(continuar) == 1 and continuar.upper()[0] != "S":
                continue
            else:
                print("Opção inválida, retornando ao menu.")
                break
        else:
            print("Verifique os dados informados e tente novamente!")


def removeItemMenu():
    while True:
        codeItem = input("Código do item: ")
        remove = deleteItem(codeItem)
        if remove:
            print("Item removido com sucesso!")
            continuar = input("Deseja excluir outro item?\n1 - Sim\n2 - Não\nEscolha: ")
            if int(continuar) == 2 or continuar.upper().startswith("N"):
                break
            elif int(continuar) == 1 and continuar.upper()[0] != "S":
                continue
            else:
                print("Opção inválida, retornando ao menu.")
                break
        else:
            print("Código não encontrado no sistema!")


def updateItemMenu():
    while True:
        nomeAtt = input("Qual item deseja atualizar? ")
        update = updateItem(nomeAtt)
        if update:
            print("Colunas atualizadas com sucesso!")
            break
        else:
            print("Ocorreu algum erro ou um campo foi preenchido de forma incorreta!")
    

def showItemMenu():
    while True:
        print("Digite o codigo do item ou digite 0 para sair")
        code = input()
        if(code == "0"):
            break
        else:
            results = findItem(code)
            if results:
                for itens in results:
                    print(itens, end=" | ")
            else:
                print("Não foi possivel encontrar item com este códio")

# End of Item Functions

# Tracking things


def trackingMenu():
    while True:
        print("MENU DO RASTREAMENTO")
        print("1 - Cadastrar rastreamento  \n2 - Remover rastreamento \n3 - Listar rastreamentos \n4 - Sair")
        option = input()
        if(option == "1"):
            print("Cadastrar rastreamento")
        elif(option == "2"):
            print("Remover rastreamento")
        elif(option == "3"):
            showTrackingMenu()
        elif(option == "4"):
            print("Atualizar")
        elif(option == "5"):
            break
        else:
            print("Opção inválida!")
            

def createTrackingMenu():
    id = input("Qual o id do produto a ser pedido: ")
    if id.isdigit():
        create = createTracking(id)

def removeTrackingMenu():
    while True:
        idRastrear = int(input("Digite o codigo de rastreamento ou digite 0 para sair: "))
        if idRastrear == 0:
            break
        else:
            rastreamento = removeTracking(idRastrear)
            if rastreamento:
                print("Rastreamento excluído com sucesso!")
                break
            else:
                print("Id inexistente no sistema!")


def showTrackingMenu():
    while True:
        print("Digite o codigo de rastreamento ou digite 0 para sair: ")
        codigo = input()
        if(codigo == "0"):
            break
        else:
            find = verifyTracking(codigo)
            if find:
                for order in find:
                    print(order, end=" | ")
            else:
                print("Não foi possivel encontrar um rastreamento com este código")

def updateTrackingMenu():
    while True:
        idPedido = int(input("Digite o codigo de rastreamento ou digite 0 para sair: "))
        if idPedido != 0:
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
                    print("Escolha inválida!")
                    continue
            update = updateTracking(idPedido, novoStatus)
            if update:
                print("Pedido atualizado!")
            else:
                print("Não foi possível encontrar um rastreamento para este item!")
        else:
            break
        
# End of Tracking Functions