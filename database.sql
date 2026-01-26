CREATE DATABASE estoque;

USE estoque;

CREATE TABLE produtos(
	id_produto INT PRIMARY KEY AUTO_INCREMENT,
	marca VARCHAR (250),
	modelo VARCHAR (250),
	codigo_barras INT
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