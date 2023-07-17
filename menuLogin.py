from time import sleep
from controllerUser import registerUser, userLogin
from mensagemSistema import purple, resetColor
from menuAdmin import registerUserMenu


def loginMenu():
    purple()
    print(" ________________________________________________________________________________________________")
    print("|                                                                                                |")
    print("|     ___________               .__                  .___                                        |")
    print("|     \_   _____/  ______ __ __ |__|______    ____   |   |_______   ____    ____  _____          |")
    print("|      |    __)_  / ____/|  |  \|  |\____ \ _/ __ \  |   |\_  __ \ /  _ \ _/ ___\ \__  \         |")
    print("|      |        \< <_|  ||  |  /|  ||  |_> >\  ___/  |   | |  | \/(  <_> )\  \___  / __ \_       |")
    print("|     /_______  / \__   ||____/ |__||   __/  \___  > |___| |__|    \____/  \___  >(____  /       |")                               
    print("|             \/     |__|           |__|         \/                            \/      \/        |")
    print("|________________________________________________________________________________________________|")
    resetColor()
    option = str(input("1 - Login\n2 - Cadastrar Novo Usuário\n"))
    if(option == "1"):    
        print("Digite seu login: ")
        login = input()
        print("Digite sua senha: ")
        senha = input()

        user = userLogin(login, senha)

        if user:
            return user
        
        else:
            print("Login ou senha incorretos!")
            return False

    elif(option == "2"):
        while True:
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
        sleep(2)