import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "caio12345678",
    database = "estoque"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM produtos")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)