CREATE DATABASE spotify;

USE spotify;

CREATE TABLE genero(
	genero_id INT AUTO_INCREMENT,
    genre VARCHAR(90) NOT NULL,
    sigla CHAR(5),
    PRIMARY KEY (genero_id)
);

CREATE TABLE artista(
	artista_id INT AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL,
    data_de_nasc DATETIME NOT NULL,
    data_de_falecimento DATETIME,
    PRIMARY KEY (artista_id)
);

CREATE TABLE album(
	album_id INT NOT NULL,
    genero_id INT NOT NULL,
    artista_id INT NOT NULL,
    nome VARCHAR(150) NOT NULL,
    data_lanc DATE NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (album_id),
    FOREIGN KEY (genero_id)
		REFERENCES genero(genero_id),
	FOREIGN KEY (artista_id) 
		REFERENCES artista(artista_id)
);