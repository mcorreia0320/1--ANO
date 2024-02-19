CREATE DATABASE pastelaria;

USE pastelaria;

CREATE TABLE cliente (
	cliente_id INT AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    apelido VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    morada VARCHAR(150) NOT NULL,
    contribuinte INT NOT NULL,
    telefone INT,
    PRIMARY KEY (cliente_id)
);

CREATE TABLE ingrediente(
	ingrediente_id INT AUTO_INCREMENT,
	nome VARCHAR(45) NOT NULL,
    unidade CHAR(6) NOT NULL,
    stock INT NOT NULL,
    PRIMARY KEY (ingrediente_id)
);

CREATE TABLE receita(
	receita_id INT AUTO_INCREMENT,
    designacao VARCHAR(75) NOT NULL,
    tempo_preparacao INT NOT NULL,
    peso VARCHAR(45) NOT NULL,
    calorias INT NOT NULL,
    custo DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (receita_id)
);

CREATE TABLE encomenda (
	encomenda_id INT AUTO_INCREMENT,
    cliente_id INT NOT NULL,
    data_encomenda DATETIME NOT NULL,
    local_encomenda VARCHAR(100) NOT NULL,
    PRIMARY KEY (encomenda_id),
    FOREIGN KEY (cliente_id)
		REFERENCES cliente(cliente_id)
);

CREATE TABLE ingrediente_receita(
	ingrediente_id INT,
    receita_id INT NOT NULL,
    quantidade INT NOT NULL,
    PRIMARY KEY (ingrediente_id,receita_id),
    FOREIGN KEY (ingrediente_id)
		REFERENCES ingrediente(ingrediente_id),
	FOREIGN KEY (receita_id)
		REFERENCES receita(receita_id)
);

CREATE TABLE encomenda_receita(
	encomenda_id INT,
    receita_id INT,
    quantidade INT NOT NULL,
    PRIMARY KEY (encomenda_id, receita_id),
    FOREIGN KEY (encomenda_id) 
		REFERENCES encomenda(encomenda_id),
	FOREIGN KEY (receita_id)
		REFERENCES receita(receita_id)
);

USE pastelaria;

INSERT INTO ingrediente(nome, unidade, stock)	
	VALUES ("Farinha", "kg", 20),
			("Agua", "1", 1000),
            ("Ovos", "g", 5);

