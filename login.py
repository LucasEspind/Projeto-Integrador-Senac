from CadastroAdmin import loginAdmin, cadastrarAdmin
from CadastroUsuarios import *
from CadastroAdmin import *
from CadastroItems import *
from CadastrarRastrear import *
from mensagemSistema import *

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

iniciar = str(input("1 - Login\n2 - Cadastrar Novo Usuário\n"))
try:
    if int(iniciar) == 1 or iniciar.upper().split() == "LOGIN":
        perm = int(input("1 - Usuário Normal\n2 - Admin\nEscolha: "))
        if perm == 1:
            loginUsuario()
        elif perm == 2:
            loginAdmin()
    elif int(iniciar) == 2 or iniciar.upper().split() == "CADASTRAR":
        perm = int(input("1 - Usuário Normal\n2 - Admin\nEscolha: "))
        if perm == 1:
            cadastrarUsuario()
        elif perm == 2:
            cadastrarAdmin()
except:
    mensagemErro()