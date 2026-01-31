# estoque-python-mysql

Inserir várias linhas
Para inserir várias linhas em uma tabela, use o executemany()método.

O segundo parâmetro do executemany()método é uma lista de tuplas, contendo os dados que você deseja inserir:

Utilizamos o fetchall() método que busca todas as linhas da última instrução executada.
myresult = mycursor.fetchall()

Se você estiver interessado apenas em uma linha, pode usar o fetchone()método.
O fetchone()método retornará a primeira linha do resultado:
myresult = mycursor.fetchone()


Criação de DataFrame com Pandas a partir de um Banco de Dados
df = pd.DataFrame(myresult)
df.columns = ['id_produto','marca', 'codigo_barras','modelo','categoria','preco','memoria_gb','ram_gb', 'camera_mp', 'bateria_mah','ano_lancamento','sistema']

Geração de arquivos CSV a partir de um Banco de Dados
df.to_csv("myresult.csv", index=False)

Função responsável por inserir os dados no Banco de dados e conexão com o banco
def inserir_csv_no_mysql(inserir_csv):
    
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="caio12345678",
    database="estoque"
    )

 Converte cada linha (que é uma lista/array) em tupla necessária para o banco de dados 
 dados = [tuple(linha) for linha in df.values]


Consultas SQL Utilizadas

Selecionar todos os produtos:
SELECT * FROM produtos;

Filtrar produtos por marca:
SELECT * FROM produtos WHERE marca = 'Apple';

Ordenar produtos por preço:
SELECT * FROM produtos ORDER BY preco DESC;
