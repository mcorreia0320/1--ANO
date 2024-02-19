CREATE DATABASE livraria1;

USE livraria1;

CREATE TABLE leitor(
	leitor_id INT AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(50) NOT NULL,
    cod_postal VARCHAR(50) NOT NULL,
    localidade VARCHAR(50) NOT NULL,
    complemento VARCHAR(50) NOT NULL,
    PRIMARY KEY (leitor_id)
);

CREATE TABLE editora(
	editora_id INT AUTO_INCREMENT,
	nome VARCHAR(50) NOT NULL,
	endereco VARCHAR(50) NOT NULL,
	cod_postal VARCHAR(50) NOT NULL,
    PRIMARY KEY (editora_id)
);

CREATE TABLE autor(
	autor_id INT AUTO_INCREMENT,
	nome VARCHAR(50) NOT NULL,
    ddn VARCHAR(50),
    PRIMARY KEY (autor_id)
);

CREATE TABLE palavra_chave(
	palavra_id INT AUTO_INCREMENT,
    palavra VARCHAR(50) NOT NULL,
    PRIMARY KEY (palavra_id)
);

CREATE TABLE livro(
	livro_id INT AUTO_INCREMENT,
    editora_id INT NOT NULL,
    isbn VARCHAR(50) NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    ano INT NOT NULL,
    edicao VARCHAR(50) NOT NULL,
    quota VARCHAR(50),
    PRIMARY KEY (livro_id),
    FOREIGN KEY (editora_id)
		REFERENCES editora(editora_id)
);

CREATE TABLE exemplar(
	exemplar_id INT AUTO_INCREMENT,
    livro_id INT NOT NULL,
    data_de_aquisicao DATETIME NOT NULL,
    PRIMARY KEY (exemplar_id),
    FOREIGN KEY (livro_id)
		REFERENCES livro(livro_id)
);

CREATE TABLE requisicao(
	requisicao_id INT AUTO_INCREMENT,
    exemplar_id INT NOT NULL,
    leitor_id INT NOT NULL,
    data_requisicao DATE  NOT NULL,
    data_prev_entrega DATE NOT NULL,
    data_real_entrega DATE NOT NULL,
    valor_multa FLOAT,
    PRIMARY KEY (requisicao_id),
    FOREIGN KEY (exemplar_id)
		REFERENCES exemplar(exemplar_id),
	FOREIGN KEY (leitor_id)
		REFERENCES leitor(leitor_id)
);

CREATE TABLE livro_autor(
	livro_id INT NOT NULL,
    autor_id INT NOT NULL,
    PRIMARY KEY (livro_id, autor_id),
    FOREIGN KEY (livro_id)
		REFERENCES livro(livro_id),
	FOREIGN KEY (autor_id)
		REFERENCES autor(autor_id)
);

CREATE TABLE livro_palavra(
	livro_id INT NOT NULL,
    palavra_id INT NOT NULL,
    PRIMARY KEY (livro_id, palavra_id),
    FOREIGN KEY (livro_id)
		REFERENCES livro(livro_id),
	FOREIGN KEY (palavra_id)
		REFERENCES palavra_chave(palavra_id)
);

INSERT INTO editora(nome, endereco, cod_postal)
	VALUES ("Lua de Papel", "Lisboa", "9100"),
			("Manuscrito Editora", "Porto", "9300"),
            ("Porto Editora, S.A.", "Funchal", "9000"),
            ("Desassossego", "Santana", "9200");
            
INSERT INTO livro(editora_id, isbn, titulo, ano, edicao, quota)
		VALUES (3,"9789720031280", "Último Caderno de Lanzarote", 2018,"10-2018","272"),
				(1,"9789897224140", "Areias Brancas", 2018, "07-2018", "232"),
                (4,"9789898871657", "Foi Sem Querer Que Te Quis 2", 2018, "11-2018", "312"),
                (2,"9789897801037", "Next Level", 2019, "03-2019", "280"),
                (3,"9788491392903", "A Outra Mulher", 2019, "03-2019", "464"),
                (2,"9789892344379", "Nobre & Poderoso", 2019, "03-2019", "320"),
                (2,"9789897103360", "Coração em Chamas", 2019, "04-2019", "448");
                