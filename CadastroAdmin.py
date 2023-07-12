import mysql.connector
from Admin import *
from mensagemSistema import *

#CRUD

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Senac2021",
    database = "trabalhofinal",
)

cursor = conexao.cursor()

# CREATE
def cadastrarAdmin():
    try:
        nome = input( "Nome: ")
        cargo = input( "Cargo: ")
        setor = input( "Setor: ")
        email = input( "Email: ")    
        password = input( "Senha: ")
        usuario = Admin(nome,cargo,setor,email,password)
        comando = f"INSERT INTO usuario (nome,cargo,setor,email,password,permissao) VALUES ('{usuario.nome}', '{usuario.cargo}', '{usuario.setor}','{usuario.email}','{usuario.password}, '{usuario._permissao}')"
        cursor.execute(comando)
        conexao.commit()
    except:
        mensagemErro()
# READ

nomeProcurar = str(input("Nome: "))

try:
    comando = f"SELECT * FROM usuario WHERE nome = '{nomeProcurar}"
    cursor.execute(comando)
    for i in cursor.fetchall():
        print(i[1])
except:
    mensagemErro()
# UPDATE


cursor.execute(comando)
conexao.commit()

# DELETE
try:
    nomeExcluir = str(input("Nome: "))
    setorExcluir = str(input("Setor: "))
    comando = f"DELETE FROM usuario WHERE nome = '{nomeExcluir}', setor = '{setorExcluir}'"
    cursor.execute(comando)
    conexao.commit()
except:
    mensagemErro()