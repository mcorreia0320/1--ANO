CREATE SCHEMA IF NOT EXISTS livraria1 ;
USE livraria1 ;

CREATE TABLE IF NOT EXISTS leitor (
  leitor_id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(100) NOT NULL,
  endereco VARCHAR(50) NOT NULL,
  cod_postal VARCHAR(50) NOT NULL,
  localidade VARCHAR(50) NOT NULL,
  complemento VARCHAR(50) NULL,
  PRIMARY KEY (leitor_id));

CREATE TABLE IF NOT EXISTS autor (
  autor_id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(50) NOT NULL,
  ddn VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (autor_id));

CREATE TABLE IF NOT EXISTS editora (
  editora_id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(50) NOT NULL,
  endereco VARCHAR(50) NOT NULL,
  cod_postal VARCHAR(50) NOT NULL,
  PRIMARY KEY (editora_id));

CREATE TABLE IF NOT EXISTS livro (
  livro_id INT NOT NULL AUTO_INCREMENT,
  editora_id INT NOT NULL,
  isbn VARCHAR(50) NOT NULL,
  titulo VARCHAR(100) NOT NULL,
  ano INT NOT NULL,
  edicao VARCHAR(50) NOT NULL,
  quota VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (livro_id),
  CONSTRAINT 
    FOREIGN KEY (editora_id)
    REFERENCES editora (editora_id));

CREATE TABLE IF NOT EXISTS exemplar (
  exemplar_id INT NOT NULL AUTO_INCREMENT,
  livro_id INT NOT NULL,
  data_de_aquisicao DATETIME NOT NULL,
  PRIMARY KEY (exemplar_id),
    FOREIGN KEY (livro_id)
    REFERENCES livro (livro_id));

CREATE TABLE IF NOT EXISTS livro_autor (
  livro_id INT NOT NULL,
  autor_id INT NOT NULL,
  PRIMARY KEY (livro_id, autor_id),
    FOREIGN KEY (livro_id)
    REFERENCES livro (livro_id),
    FOREIGN KEY (autor_id)
    REFERENCES autor (autor_id));


CREATE TABLE IF NOT EXISTS palavra_chave (
  palavra_id INT NOT NULL AUTO_INCREMENT,
  palavra VARCHAR(50) NOT NULL,
  PRIMARY KEY (palavra_id));


CREATE TABLE IF NOT EXISTS livro_palavra (
  livro_id INT NOT NULL,
  palavra_id INT NOT NULL,
  PRIMARY KEY (livro_id, palavra_id),
    FOREIGN KEY (livro_id)
    REFERENCES livro (livro_id),
    FOREIGN KEY (palavra_id)
    REFERENCES palavra_chave (palavra_id));


CREATE TABLE IF NOT EXISTS requisicao (
  requisicao_id INT NOT NULL AUTO_INCREMENT,
  exemplar_id INT NOT NULL,
  leitor_id INT NOT NULL,
  data_requisicao DATE NOT NULL,
  data_prev_entrega DATE NOT NULL,
  data_real_entrega DATE NOT NULL,
  valor_multa DECIMAL(5,2) NULL DEFAULT NULL,
  PRIMARY KEY (requisicao_id),
    FOREIGN KEY (exemplar_id)
    REFERENCES exemplar (exemplar_id),
    FOREIGN KEY (leitor_id)
    REFERENCES leitor (leitor_id));

