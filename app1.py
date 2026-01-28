import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="c1a2i3o4",
    database="estoque"
)

mycursor = mydb.cursor()

sql = """
INSERT INTO produtos 
(marca, modelo, codigo_barras, categoria, preco, memoria_gb, ram_gb,
 camera_mp, bateria_mah, ano_lancamento, sistema)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

val = [
    ("Apple", "iPhone 13", 2, "Premium", 4299.90, 128, 6, 12, 3240, 2021, "iOS"),
    ("Xiaomi", "Redmi Note 12", 3, "Intermediário", 1399.90, 128, 6, 50, 5000, 2023, "Android"),
    ("Motorola", "Moto G53", 4, "Entrada", 899.90, 128, 4, 50, 5000, 2023, "Android"),
    ("Samsung", "Galaxy A15", 5, "Entrada", 799.90, 64, 4, 48, 5000, 2024, "Android"),
    ("Apple", "iPhone 11", 6, "Usado", 2499.90, 64, 4, 12, 3110, 2019, "iOS")
]

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "registros inseridos com sucesso!")
