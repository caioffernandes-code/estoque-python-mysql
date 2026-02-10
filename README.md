# estoque-python-mysql

## Bibliotecas Utilizadas
- **pandas**: utilizada para leitura, manipulação e conversão de dados em DataFrame.
- **mysql.connector**: utilizada para estabelecer conexão entre o Python e o banco de dados MySQL

## Conexão com o Banco de Dados
A conexão com o banco de dados MySQL é realizada por meio da função
`mysql.connector.connect()`, onde são informados o host, usuário, senha
e nome do banco de dados.
```python
Exemplo:
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="******",
    database="estoque"
)
```
Após a conexão, é criado um cursor responsável por executar comandos SQL.

## Inserção de Dados no MySQL
A inserção dos dados é feita utilizando o método `executemany()`,
que permite inserir múltiplos registros de uma única vez.

Os dados do DataFrame são convertidos em uma lista de tuplas para
serem compatíveis com o comando SQL.
dados = [tuple(linha) for linha in df.values]
cursor.executemany(sql, dados)
conn.commit()
O método `commit()` confirma as alterações no banco de dados.

## Inserção de linhas no Python para o SQL
```python
O segundo parâmetro do executemany() método é uma lista de tuplas, contendo os dados que você deseja inserir:
Utilizamos o fetchall() método que busca todas as linhas da última instrução executada.
myresult = mycursor.fetchall()

Se você estiver interessado apenas em uma linha, pode usar o fetchone()método.
O fetchone()método retornará a primeira linha do resultado:
myresult = mycursor.fetchone()
```

## Comando para dar UPDATE no Banco de Dados
Você pode atualizar registros existentes em uma tabela usando a instrução "UPDATE":
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
```

## Comando de LIMIT no Banco de Dados
Você pode limitar o número de registros retornados pela consulta usando a instrução "LIMIT":
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```
## Comando de JOIN no Banco de Dados
É possível combinar linhas de duas ou mais tabelas, com base em uma coluna relacionada entre elas, usando uma instrução JOIN.
Considere que você tem uma tabela de "usuários" e uma tabela de "produtos":
Essas duas tabelas podem ser combinadas usando fav os campos de usuários e de produtos id.
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

## Criação de DataFrame com Pandas a partir de um Banco de Dados
```python
df = pd.DataFrame(myresult)
df.columns = ['id_produto','marca', 'codigo_barras','modelo','categoria','preco','memoria_gb','ram_gb', 'camera_mp', 'bateria_mah','ano_lancamento','sistema']
```

## Geração de arquivos CSV a partir de um Banco de Dados
```python
- df.to_csv("myresult.csv", index=False)
```

## leitura de um arquivo csv
```python
 - df = pd.read_csv(inserir_csv)
 ```

## Consultas SQL Utilizadas

### Selecionar todos os produtos:
```python
- SELECT * FROM produtos;
```

### Filtrar produtos por marca:
```python
- SELECT * FROM produtos WHERE marca = 'Apple';
```

### Ordenar produtos por preço:
```python
- SELECT * FROM produtos ORDER BY preco DESC;
```

### O que é uma instância em python?
```python
- conn = mysql.connector.connect(...)
connect() cria uma instância de conexão
conn é um objeto com métodos e atributos

- cursor = conn.cursor()
cursor também é uma instância
criada a partir da conexão
```

## List Comprehension

A compreensão de listas oferece uma sintaxe mais concisa quando você deseja criar uma nova lista com base nos valores de uma lista existente.

### Exemplo:

Com base em uma lista de frutas, você deseja uma nova lista contendo apenas as frutas que têm a letra "a" no nome.

Sem a compreensão de listas, você terá que escrever uma forinstrução com um teste condicional dentro dela:

### Exemplo:
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
```
## Com a List Comprehension, você pode fazer tudo isso com apenas uma linha de código:

### Exemplo
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
```
