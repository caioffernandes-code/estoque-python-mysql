import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "caio12345678",
    database = "estoque"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM produtos WHERE marca = 'Apple'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

df = pd.DataFrame(myresult)
df.columns = ['id_produto','marca', 'codigo_barras','modelo','categoria','preco','memoria_gb','ram_gb', 'camera_mp', 'bateria_mah','ano_lancamento','sistema']
print(df)

df.to_csv("myresult.csv", index=False)