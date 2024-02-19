CREATE DATABASE pratica_5a;

USE pratica_5a;

CREATE TABLE aluno (
	aluno_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    genero ENUM('M','F') NOT NULL,
    dataNasc DATE NOT NULL,
    morada VARCHAR(50) NOT NULL,
    telefone INT(9)
);

ALTER TABLE aluno
MODIFY COLUMN morada VARCHAR(60);


INSERT INTO aluno(nome,genero,dataNasc,morada)
	VALUES ("Abel","M","1994-12-25", "Porto"),
			("Carla", "F", "1995-01-10", "Braga"),
            ("Daniel","M","1995-02-02","Aveiro"),
            ("Susana","F","1994-12-31","Viseu");
            
CREATE TABLE curso(
	curso_id CHAR(5) PRIMARY KEY,
    curso CHAR(50) NOT NULL,
    n_anos INT NOT NULL
);

ALTER TABLE curso
MODIFY COLUMN curso VARCHAR(100);

INSERT INTO curso(curso_id,curso,n_anos)
	VALUES ("TIG","Técnico de Informática de Gestão",3),
			("TGPSI","Técnico de Gestão e Programação de Sistemas Informáticos",3);
            



	



