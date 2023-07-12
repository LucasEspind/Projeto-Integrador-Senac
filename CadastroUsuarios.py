import mysql.connector
from Usuario import *
from mensagemSistema import *

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Senac2021",
    database = "trabalhofinal",
)

# CRUD
cursor = conexao.cursor()

# CREATE

def cadastrarUsuario():
    try:
        nome = input( "Nome: ")
        cargo = input( "Cargo: ")
        setor = input( "Setor: ")
        email = input( "Email: ")    
        password = input( "Senha: ")
        usuario = Usuario(nome,cargo,setor,email,password)
        comando = f"INSERT INTO usuario (nome,cargo,setor,email,password,permissao) VALUES ('{usuario.nome}', '{usuario.cargo}', '{usuario.setor}','{usuario.email}','{usuario.password}, '{usuario._permissao}')"
        cursor.execute(comando)
        conexao.commit()
    except:
        mensagemErro()
# Read
comando = f"SELECT * FROM usuario"
cursor.execute(comando)
for i in cursor.fetchall():
    print(i[1])

# UPDATE

# cursor.execute(comando)
# conexao.commit()

# DELETE
def deletarFuncionario():
    nomeExcluir = str(input("Nome:"))
    try:
        comando = f"DELETE FROM usuario WHERE nome = '{nomeExcluir}'"
        cursor.execute(comando)
        conexao.commit()
    except:
        pass