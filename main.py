from time import sleep
from menuAdmin import adminMenu
from menuLogin import loginMenu
from menuUser import userMenu

while True:
    user = loginMenu()

    if user:
        if user[7] == "Admin":
            adminMenu()
        elif user[7]  == "Usuario":
            userMenu()
    else:
        print("Opção inválida!")
        sleep(2)
        continue