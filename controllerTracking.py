from asyncio import sleep
import mysql.connector
from modelRastrear import Rastrear
from mensagemSistema import mensagemErro, pularLinha

# CRUD

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="trabalhofinal",
)

cursor = conexao.cursor()


def createTracking(idTracking):
    rastrear = Rastrear(idTracking)
    try:
        comando = "INSERT INTO rastreamento (id_rastreamento, status_entrega) VALUES (%s, %s)"
        valores = (rastrear.idItem, rastrear.statusEntrega)
        cursor.execute(comando, valores)
        conexao.commit()
        return True
    except:
        return False


def verifyTracking(idItem):
    while True:
            comando = "SELECT * FROM rastreamento WHERE id_rastreamento = %s"
            cursor.execute(comando, (idItem,))
            resultados = cursor.fetchone()
            if resultados:
                return resultados
            else:
                False


def updateTracking(idPedido, novoStatus):
    try:
        comando = "UPDATE rastreamento SET status_entrega = %s WHERE id_rastreamento = %s"
        valores = (novoStatus, idPedido)
        cursor.execute(comando, valores)
        conexao.commit()
        return True
    except:
        return False


def removeTracking(idRastrear):
    try:
        
        comando = "DELETE FROM rastreamento WHERE id_rastreamento = %s"
        valores = (idRastrear,)

        cursor.execute(comando, valores)
        conexao.commit()
        if cursor.rowcount > 0:
            return True
        else:
            return False
        
    except:
        return False