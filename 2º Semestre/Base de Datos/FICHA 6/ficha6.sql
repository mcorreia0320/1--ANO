USE livraria1;

/* EXERCICIO D */

/* i. */
SELECT * FROM editora;

/* ii. */
SELECT * FROM livro
WHERE ano = '2018';

/* iii. */
SELECT AVG(ROUND(quota,0)) AS 'Media de paginas dos livros' FROM livro;

/* iv. */
SELECT titulo,ano,quota FROM livro
WHERE ano = '2019' AND quota > 400;

/* v. */
SELECT titulo, quota AS 'Livro com menos paginas' FROM livro
WHERE quota = (SELECT MIN(quota) FROM livro);


/* vi. */
SELECT titulo,quota AS 'Livro com mais paginas' FROM livro
WHERE quota = (SELECT MAX(quota) FROM livro);

/* EXERCICIO E */

/* i. */
UPDATE editora SET nome = 'Porto Editora'
WHERE editora_id = 3;

/* ii */
DELETE FROM livro WHERE livro_id = 1;
SELECT * FROM livro;

/* iii. */
DELETE FROM livro WHERE ano = '2019';
SELECT * FROM livro;