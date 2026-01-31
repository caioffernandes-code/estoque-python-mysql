import pandas as pd
import mysql.connector

def inserir_csv_no_mysql(inserir_csv):
    
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="caio12345678",
    database="estoque"
    )

    cursor = conn.cursor()

    
    df = pd.read_csv(inserir_csv)

    sql = """
        INSERT INTO produtos (
        marca, modelo, codigo_barras, categoria, preco,
        memoria_gb, ram_gb, camera_mp, bateria_mah,
        ano_lancamento, sistema
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    dados = [tuple(linha) for linha in df.values]

    cursor.executemany(sql, dados)
    conn.commit()

    print(f"{cursor.rowcount} registros inseridos com sucesso.")

    cursor.close()
    conn.close()



inserir_csv_no_mysql("inserir.csv")
