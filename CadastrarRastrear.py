import mysql.connector
from Rastrear import Rastrear

# CRUD

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "trabalhofinal",
)

cursor = conexao.cursor()

rastrear = Rastrear(1)

# CREATE
def realizarPedido():
    id = int(input( "Qual o id do produto: "))
    rastrear = Rastrear(id)
    comando = f"INSERT INTO rastreamento (id_rastreamento, status_entrega) VALUES ('{rastrear.idItem}', '{rastrear.statusEntrega}')"
    cursor.execute(comando)
    conexao.commit()

# READ
def verificarPedido():
    comando = f"SELECT * FROM rastreamento"
    cursor.execute(comando)
    for i in cursor.fetchall():
        print(i[1])

# UPDATE 
def atualizarPedido():
    comando = f"UPDATE rastreamento SET id_rastreamento = 1 WHERE status_entrega = 'pedidos feitos'"
    cursor.execute(comando)
    conexao.commit()

# DELETE
def excluirPedido():
    comando = f"DELETE FROM rastreamento WHERE id_rastreamento = '1'"
    cursor.execute(comando)
    conexao.commit()


def RastrearAdmin():
    escolha = str(input("O que deseja realizar:\n1 - Realizar Pedido\n2 - Verificar Pedido\n3 - Atualizar Pedido\n4 - Excluir Pedido"))
    if int(escolha) == 1:
        realizarPedido()
    if int(escolha) == 1:
        verificarPedido()
    if int(escolha) == 1:
        atualizarPedido()
    if int(escolha) == 1:
        excluirPedido()