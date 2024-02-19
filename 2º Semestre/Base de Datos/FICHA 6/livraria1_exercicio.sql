USE livraria1;

SELECT * FROM vEditora;
SELECT * FROM onlyNome;

CREATE VIEW vEditora
    AS SELECT nome,endereco FROM editora;

CREATE VIEW onlyNome
    AS SELECT nome FROM editora;

SHOW FULL TABLES;
