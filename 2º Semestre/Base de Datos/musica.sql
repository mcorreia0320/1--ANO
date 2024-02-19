CREATE DATABASE musica;

USE musica;

CREATE TABLE utilizador(
	utilizador_id INT AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    genero ENUM('M','F') NOT NULL,
    nacionalidade VARCHAR(45) NOT NULL,
    PRIMARY KEY (utilizador_id)
);

CREATE TABLE cantor(
	cantor_id INT AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL,
    PRIMARY KEY (cantor_id)
);

CREATE TABLE album(
	album_id INT AUTO_INCREMENT,
    titulo VARCHAR(45) NOT NULL,
    cantor_id INT NOT NULL,
    PRIMARY KEY (album_id),
    FOREIGN KEY (cantor_id)
		REFERENCES cantor(cantor_id)
);

CREATE TABLE faixa(
	faixa_id INT AUTO_INCREMENT,
    nome_musica VARCHAR(45) NOT NULL,
    album_id INT NOT NULL,
    PRIMARY KEY (faixa_id),
    FOREIGN KEY (album_id) 
		REFERENCES album(album_id)
);

CREATE TABLE faixa_preferida(
	faixa_id INT NOT NULL,
    utilizador_id INT NOT NULL,
    pontuacao DOUBLE,
    PRIMARY KEY (faixa_id, utilizador_id),
    FOREIGN KEY (faixa_id) 
		REFERENCES faixa(faixa_id),
	FOREIGN KEY (utilizador_id)
		REFERENCES utilizador(utilizador_id)
);

INSERT INTO utilizador(nome,genero,nacionalidade)
	VALUES ("Abel","M","Portugal"),
			("Carla","F","Espanha"),
            ("Daniel","M","Inglaterra"),
            ("Susana","F","Portugal");

INSERT INTO cantor(nome)
	VALUES ("Tony Carreira"),
			("BossAC");
