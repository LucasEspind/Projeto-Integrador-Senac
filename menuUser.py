from controllerTracking import verifyTracking
from controllerItem import findItem


def userMenu():
    while True:
        print("MENU DO USUARIO")
        print("1 - Ver Item \n2 - Rastrear Item \n3 - Sair")
        option = input()
        if(option == "1"):
            itemMenu() 
        elif(option == "2"):
            trackingMenu()
        elif(option == "3"):
            break

def itemMenu():
    while True:
        print("Digite o codigo do item ou digite 0 para sair\nEscolha: ")
        codigo = input()
        if(codigo == "0"):
            break
        else:
            resultados = findItem(codigo)
            if resultados:
                for itens in resultados:
                    print(itens, end=" | ")
            else:
                print("Não foi possivel encontrar item com este códio")
        print()

def trackingMenu():
    while True:
        print("Digite o codigo de rastreamento ou digite 0 para sair\nEscolha: ")
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