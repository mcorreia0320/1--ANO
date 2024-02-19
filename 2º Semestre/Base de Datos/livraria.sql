CREATE DATABASE livraria;

USE livraria;

CREATE TABLE utilizador(
	utilizador_id INT AUTO_INCREMENT,
    username VARCHAR(200) NOT NULL,
    criado_a DATETIME,
    actualizado_a DATETIME,
    PRIMARY KEY (utilizador_id)
);

CREATE TABLE autor(
	autor_id INT AUTO_INCREMENT,
    nome VARCHAR(250) NOT NULL,
    apelido VARCHAR(250) NOT NULL,
    criado_a DATETIME,
    actualizado_a DATETIME,
    PRIMARY KEY (autor_id)
);

CREATE TABLE livro(
	livro_id INT AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    autor_id INT NOT NULL,
    ano_publicacao INT NOT NULL,
    genero VARCHAR(255) NOT NULL,
    criado_a DATETIME,
    actualizado_a DATETIME,
    PRIMARY KEY (livro_id),
    FOREIGN KEY (autor_id)
		REFERENCES autor(autor_id)
);

CREATE TABLE favorito(
	utilizador_id INT NOT NULL,
    livro_id INT NOT NULL,
    criado_a TIMESTAMP,
    actualizado_a TIMESTAMP,
    FOREIGN KEY (utilizador_id)
		REFERENCES utilizador(utilizador_id),
	FOREIGN KEY (livro_id)
		REFERENCES livro(livro_id)
);
