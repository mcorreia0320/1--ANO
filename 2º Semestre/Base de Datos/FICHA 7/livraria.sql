CREATE DATABASE livraria;
USE livraria;

CREATE TABLE utilizador (
  utilizador_id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(200) NOT NULL,
  criado_a DATETIME NULL,
  actualizado_a DATETIME NULL,
  PRIMARY KEY (utilizador_id)
 );

CREATE TABLE autor (
  autor_id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  apelido VARCHAR(255) NOT NULL,
  criado_a DATETIME NULL,
  actualizado_a DATETIME NULL,
  PRIMARY KEY (autor_id)
 );

CREATE TABLE livro (
  livro_id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(100) NOT NULL,
  autor_id INT NOT NULL,
  ano_publicacao INT NOT NULL,
  genero VARCHAR(255) NOT NULL,
  criado_a DATETIME NULL,
  actualizado_a DATETIME NULL,
  PRIMARY KEY (livro_id),
  CONSTRAINT fk_livro_autor
    FOREIGN KEY (autor_id)
    REFERENCES autor(autor_id)
);

CREATE TABLE favorito (
  utilizador_id INT NOT NULL,
  livro_id INT NOT NULL,
  criado_a TIMESTAMP DEFAULT current_timestamp,
  actualizado_a TIMESTAMP DEFAULT current_timestamp,
  PRIMARY KEY (utilizador_id, livro_id),
  CONSTRAINT fk_favorito_utilizador
    FOREIGN KEY (utilizador_id)
    REFERENCES utilizador(utilizador_id),
  CONSTRAINT fk_favorito_livro
    FOREIGN KEY (livro_id)
    REFERENCES livro(livro_id)
);

