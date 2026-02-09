import mysql.connector
import pandas as pd

def connect():
    mydb = mysql.connector.connect(
        host= "localhost",
        user= "root",
        password= "caio12345678",
        database = "estoque"
    )

    cursor = mydb.cursor()
    return cursor, mydb
print(connect())

def insert(arquivo):
    data_frame = pd.read_csv(arquivo)

    sql = """
        INSERT INTO produtos (
        marca, modelo, codigo_barras, categoria, preco,
        memoria_gb, ram_gb, camera_mp, bateria_mah,
        ano_lancamento, sistema
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    dados = [tuple(linha) for linha in data_frame.values]

    cursor, conn = connect()

    cursor.executemany(sql, dados)
    conn.commit()

    cursor.close()
    conn.close()



insert('inserir.csv')