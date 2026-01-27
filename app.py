import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="c1a2i3o4",
  database="estoque"
)

mycursor = mydb.cursor()

sql = "INSERT INTO produtos " \
"(marca, modelo, codigo_barras, categoria, preco, memoria_gb, ram_gb, camera_mp, bateria_mah, ano_lancamento, sistema) " \
"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = ("Samsung", "Galaxy S21", "1", "Premium", "3499.9", "128", "8", "64", "4000", "2021", "Android")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")