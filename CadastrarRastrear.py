import mysql.connector
from Rastrear import Rastrear

# CRUD

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Senac2021",
    database = "trabalhofinal",
)

cursor = conexao.cursor()

rastrear = Rastrear(1)

# CREATE

id = int(input( "Qual o id do produto: "))
rastrear = Rastrear(id)
comando = f"INSERT INTO rastreamento (id_rastreamento, status_entrega) VALUES ('{rastrear.idItem}', '{rastrear.statusEntrega}')"
cursor.execute(comando)
conexao.commit()

# READ

comando = f"SELECT * FROM rastreamento"
cursor.execute(comando)
for i in cursor.fetchall():
    print(i[1])

# UPDATE 

comando = f"UPDATE rastreamento SET id_rastreamento = 1 WHERE status_entrega = 'pedidos feitos'"
cursor.execute(comando)
conexao.commit()

# DELETE
comando = f"DELETE FROM rastreamento WHERE id_rastreamento = '1'"
cursor.execute(comando)
conexao.commit()