CREATE DATABASE estoque;

USE estoque;

CREATE TABLE produtos (
	id_produto INT AUTO_INCREMENT PRIMARY KEY,
	marca VARCHAR (250),
	modelo VARCHAR (250),
	codigo_barras INT,
	categoria VARCHAR (250),
	preco DECIMAL (10,2),
	memoria_gb INT,
	ram_gb INT,
	camera_mp INT,
	bateria_mah INT,
	ano_lancamento YEAR,
	sistema VARCHAR (250)
);

INSERT INTO produtos (
	marca,
	modelo,
	codigo_barras
)
VALUES (
	'Apple', 
	'Iphone 11', 
	2
);


DROP TABLE nome_da_tabela;
SELECT * FROM estoque.produtos;
SELECT * FROM produtos;

