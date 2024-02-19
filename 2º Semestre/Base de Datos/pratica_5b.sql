CREATE DATABASE srs;

USE srs;

SET SQL_SAFE_UPDATES = 0;

CREATE TABLE medicamento(
	medicamento_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    preco DECIMAL(5,2) NOT NULL,
    substancia VARCHAR(155) NOT NULL,
    origem VARCHAR(45) NOT NULL
);

ALTER TABLE medicamento CHANGE substancia substancia_ativa VARCHAR(155);
ALTER TABLE medicamento DROP origem;
ALTER TABLE medicamento ADD forma_farmaceutica ENUM('Comprimido', 'Comprimido efervescente', 'Comprimido revestido', 'Comprimido revestido com pelicula');
ALTER TABLE medicamento
MODIFY COLUMN nome VARCHAR(100);


INSERT INTO medicamento(nome,preco,substancia_ativa,forma_farmaceutica)
	VALUES ("Dafalgan 1g",1.72,"Paracetamol","Comprimido efervescente"),
			("Ciprofloxacina Sandoz",4.51,"Ciprofloxacina","Comprimido revestido"),
            ("Nurofen", 3.59, "Ibuprofeno", "Comprimido revestido"),
            ("Ben-U-Ron", 2.37, "Paracetamol","Comprimido"),
            ("Rosilan",4.82, "Deflazacorte", "Comprimido"),
            ("Aspirina Microactive",1.32, "Ácido acetilsalicílico", "Comprimido revestido"),
            ("Lepicortinolo",1.95, "Prednisolona", "Comprimido"),
             ("Deflazacorte Farmoz",4.19, "Deflazacorte", "Comprimido"),
             ("Alka-Seltzer",6.44, "Bicarbonato de sódio", "Comprimido efervescente");
             
UPDATE medicamento
SET preco = 3.07
WHERE medicamento_id = 4;

UPDATE medicamento
SET nome = "Brufen"
WHERE medicamento_id = 3;

UPDATE medicamento
SET forma_farmaceutica = "Comprimido revestido com pelicula", preco = preco + 0.50
WHERE forma_farmaceutica = "Comprimido revestido";

DELETE FROM medicamento WHERE substancia_ativa = "Deflazacorte";

CREATE TABLE doenca(
	doenca_id INT AUTO_INCREMENT,
    nome VARCHAR(150),
    data_descoberta DATE,
    origem VARCHAR(45),
    PRIMARY KEY (doenca_id)
);

CREATE TABLE medicamento_doenca(
	medicamento_id INT NOT NULL,
    doenca_id INT NOT NULL,
    FOREIGN KEY (medicamento_id)
		REFERENCES medicamento(medicamento_id),
	FOREIGN KEY (doenca_id)
		REFERENCES doenca(doenca_id)
);

SET SQL_SAFE_UPDATES = 1;

SELECT nome, preco FROM medicamento;


            



