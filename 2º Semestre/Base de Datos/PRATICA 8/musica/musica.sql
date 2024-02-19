CREATE DATABASE musica_ficha8;
USE musica_ficha8;

CREATE TABLE cantor (
  cantor_id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(45) NOT NULL,
  PRIMARY KEY (cantor_id)
);

CREATE TABLE album (
  album_id INT NOT NULL AUTO_INCREMENT,
  titulo VARCHAR(45) NOT NULL,
  cantor_id INT NOT NULL,
  PRIMARY KEY (album_id),
  CONSTRAINT fk_album_cantora
    FOREIGN KEY (cantor_id)
    REFERENCES cantor (cantor_id)
);

CREATE TABLE faixa (
  faixa_id INT NOT NULL AUTO_INCREMENT,
  nome_musica VARCHAR(45) NOT NULL,
  album_id INT NOT NULL,
  PRIMARY KEY (faixa_id),
  CONSTRAINT fk_faixa_album
    FOREIGN KEY (album_id)
    REFERENCES album(album_id)
);

CREATE TABLE utilizador (
  utilizador_id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(100) NOT NULL,
  genero ENUM('M', 'F') NOT NULL,
  nacionalidade VARCHAR(45) NOT NULL,
  PRIMARY KEY (utilizador_id)
);

CREATE TABLE faixa_preferida (
  faixa_id INT NOT NULL,
  utilizador_id INT NOT NULL,
  pontuacao DOUBLE NULL,
  PRIMARY KEY (faixa_id, utilizador_id),
  CONSTRAINT fk_faixa_preferida_faixa
    FOREIGN KEY (faixa_id)
    REFERENCES faixa(faixa_id),
  CONSTRAINT fk_faixa_preferida_utilizador
    FOREIGN KEY (utilizador_id)
    REFERENCES utilizador(utilizador_id)
);
