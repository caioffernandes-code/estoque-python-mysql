# estoque-python-mysql

## Bibliotecas Utilizadas
- **pandas**: utilizada para leitura, manipulação e conversão de dados em DataFrame.
- **mysql.connector**: utilizada para estabelecer conexão entre o Python e o banco de dados MySQL

## Conexão com o Banco de Dados
A conexão com o banco de dados MySQL é realizada por meio da função
`mysql.connector.connect()`, onde são informados o host, usuário, senha
e nome do banco de dados.

Exemplo:
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="******",
    database="estoque"
)
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

O segundo parâmetro do executemany() método é uma lista de tuplas, contendo os dados que você deseja inserir:
Utilizamos o fetchall() método que busca todas as linhas da última instrução executada.
myresult = mycursor.fetchall()

Se você estiver interessado apenas em uma linha, pode usar o fetchone()método.
O fetchone()método retornará a primeira linha do resultado:
myresult = mycursor.fetchone()

## Criação de DataFrame com Pandas a partir de um Banco de Dados

df = pd.DataFrame(myresult)
df.columns = ['id_produto','marca', 'codigo_barras','modelo','categoria','preco','memoria_gb','ram_gb', 'camera_mp', 'bateria_mah','ano_lancamento','sistema']

## Geração de arquivos CSV a partir de um Banco de Dados
- df.to_csv("myresult.csv", index=False)

## leitura de um arquivo csv
 - df = pd.read_csv(inserir_csv)

## Consultas SQL Utilizadas

### Selecionar todos os produtos:
- SELECT * FROM produtos;

### Filtrar produtos por marca:
- SELECT * FROM produtos WHERE marca = 'Apple';

### Ordenar produtos por preço:
- SELECT * FROM produtos ORDER BY preco DESC;

### O que é uma instância em python?
- conn = mysql.connector.connect(...)
connect() cria uma instância de conexão
conn é um objeto com métodos e atributos

- cursor = conn.cursor()
cursor também é uma instância
criada a partir da conexão

## List Comprehension

A compreensão de listas oferece uma sintaxe mais concisa quando você deseja criar uma nova lista com base nos valores de uma lista existente.

### Exemplo:

Com base em uma lista de frutas, você deseja uma nova lista contendo apenas as frutas que têm a letra "a" no nome.

Sem a compreensão de listas, você terá que escrever uma forinstrução com um teste condicional dentro dela:

### Exemplo:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

## Com a List Comprehension, você pode fazer tudo isso com apenas uma linha de código:

### Exemplo
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
