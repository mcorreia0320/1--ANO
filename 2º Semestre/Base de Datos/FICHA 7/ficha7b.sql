/* i. */
SELECT livro.nome AS 'Livros de Mia Couto' FROM livro
    INNER JOIN autor ON livro.autor_id = autor.autor_id
    WHERE autor.nome= 'Mia' AND autor.apelido = 'Couto';

/* ii. */
SELECT COUNT(*) AS 'Total de livros' FROM livro;

/* iii. */
SELECT CONCAT(autor.nome, ' ', autor.apelido) AS 'Autor' ,COUNT(livro_id) AS 'Total' FROM livro
    INNER JOIN autor ON livro.autor_id = autor.autor_id
    GROUP BY Autor;

/* iv. */
SELECT livro.nome AS 'Livros favoritos de Bruna Silva' FROM utilizador
        INNER JOIN favorito ON utilizador.utilizador_id = favorito.utilizador_id
        INNER JOIN livro ON favorito.livro_id = livro.livro_id
        WHERE utilizador.username = 'BrunaSilva';

/* v. */
SELECT utilizador.utilizador_id, utilizador.username FROM utilizador
        LEFT JOIN favorito ON utilizador.utilizador_id = favorito.utilizador_id
        WHERE favorito.livro_id IS NULL;

/* vi. */
SELECT DISTINCT genero FROM livro;

/* vii. */
SELECT utilizador.username, COUNT(favorito.livro_id) AS 'Total' FROM utilizador
        INNER JOIN favorito ON utilizador.utilizador_id = favorito.utilizador_id
        GROUP BY utilizador.username
        HAVING Total > 2
        ORDER BY username DESC;
