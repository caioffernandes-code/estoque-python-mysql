import mysql.connector

mydb = mysql.connector.connect(
    
    host = 'localhost',
    user = 'root'
    password = 'caio12345678'
    database = 'estoque'

)

mycursor = mydb.cursor()

sql = "SELECT * FROM produtos ORDER BY preco"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)