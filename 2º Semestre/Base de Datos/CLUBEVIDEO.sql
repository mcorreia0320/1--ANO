CREATE DATABASE clubevideo;

USE clubevideo;

CREATE TABLE cliente (
	cliente_id INT AUTO_INCREMENT, 
    nome VARCHAR(100) NOT NULL,
    apelido VARCHAR(100) NOT NULL,
    morada VARCHAR (150) NOT NULL,
    telefone INT,
    PRIMARY KEY (cliente_id)
);

CREATE TABLE video (
	video_id INT AUTO_INCREMENT,
    titulo VARCHAR(45) NOT NULL,
    genero ENUM('Acção','Comedia') NOT NULL,
    duracao INT NOT NULL,
    empresa_distribuicao VARCHAR(45) NOT NULL,
    PRIMARY KEY (video_id)
);

CREATE TABLE aluguer (
	aluguer_id INT AUTO_INCREMENT,
    data_entrada DATETIME NOT NULL,
    data_saida DATETIME NOT NULL,
    cliente_id INT NOT NULL,
    video_id INT NOT NULL,
    PRIMARY KEY (aluguer_id),
    FOREIGN KEY (cliente_id) 
		REFERENCES cliente(cliente_id),
    FOREIGN KEY (video_id)
		REFERENCES video(video_id)
);