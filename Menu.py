import CadastroUsuarios
from Itens import *
import mensagemSistema

mensagemSistema.purple()
print("___________               .__                  .___")
print("\_   _____/  ______ __ __ |__|______    ____   |   |_______   ____    ____  _____   ")
print(" |    __)_  / ____/|  |  \|  |\____ \ _/ __ \  |   |\_  __ \ /  _ \ _/ ___\ \__  \  ")
print(" |        \< <_|  ||  |  /|  ||  |_> >\  ___/  |   | |  | \/(  <_> )\  \___  / __ \_")
print("/_______  / \__   ||____/ |__||   __/  \___  > |___| |__|    \____/  \___  >(____  /")                               
print("        \/     |__|           |__|         \/                            \/      \/ ")
mensagemSistema.resetColor()

try:
    iniciar = str(input("1 - Login\n2 - Cadastrar Novo Usuário\n"))
    if int(iniciar) == 1 or iniciar.upper().split() == "LOGIN":
        pass
    elif int(iniciar) == 2 or iniciar.upper().split() == "CADASTRAR":
        perm = int(input("1 - Usuário Normal\n2 - Admin"))
        if perm == 1:
            CadastroUsuarios.cadastrarUsuario()
except:
    mensagemSistema.mensagemErro()