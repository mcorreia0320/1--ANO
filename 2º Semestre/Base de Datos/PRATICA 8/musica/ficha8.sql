USE musica_ficha8;

/* EXERCICIO f */

/* i. */
SELECT faixa.nome_musica AS 'Faixas Preferidas do Abel' FROM faixa
    INNER JOIN faixa_preferida ON faixa.faixa_id = faixa_preferida.faixa_id
    INNER JOIN utilizador ON faixa_preferida.utilizador_id = utilizador.utilizador_id
    WHERE utilizador.nome = 'Abel';

/* ii. */
SELECT faixa.nome_musica AS 'Musica',album.titulo AS 'Album' FROM faixa
    INNER JOIN album ON faixa.album_id = album.album_id;

/* iii. */
SELECT album.titulo AS 'Album', COUNT(faixa.faixa_id) AS 'Total de musicas' FROM faixa
    RIGHT JOIN album ON album.album_id = faixa.album_id
    GROUP BY album.titulo
    ORDER BY `Total de musicas`;

/* iv. */
SELECT cantor.nome AS 'Cantor', COUNT(album_id) AS 'Total de albumes' FROM cantor
    LEFT JOIN album ON cantor.cantor_id = album.cantor_id
    GROUP BY cantor.nome
    ORDER BY `Total de albumes`;

/* v. */
SELECT album.titulo AS 'Album', COUNT(faixa.faixa_id) AS 'Total de faixas' FROM album
    INNER JOIN faixa ON album.album_id = faixa.album_id
    GROUP BY Album
    HAVING `Total de faixas` >= 3;

/* vi. */
SELECT cantor.nome AS 'Cantor', COUNT(faixa.faixa_id) AS 'Total de musicas' FROM cantor
    LEFT JOIN album ON cantor.cantor_id = album.cantor_id
    LEFT JOIN faixa ON album.album_id = faixa.album_id
    GROUP BY Cantor
    ORDER BY `Total de musicas`;

/* vii. */
SELECT faixa.nome_musica AS 'Musica',SUM(faixa_preferida.pontuacao) AS 'Total Pontuação dos Portugueses' FROM utilizador
    INNER JOIN faixa_preferida ON utilizador.utilizador_id = faixa_preferida.utilizador_id
    INNER JOIN faixa ON faixa_preferida.faixa_id = faixa.faixa_id
    WHERE nacionalidade = 'Portugal'
    GROUP BY Musica;

/* viii. */
SELECT cantor.nome AS 'Cantores preferidos pelos Espanhois' FROM cantor
    INNER JOIN album ON cantor.cantor_id = album.cantor_id
    INNER JOIN faixa ON album.album_id = faixa.album_id
    INNER JOIN faixa_preferida ON faixa.faixa_id = faixa_preferida.faixa_id
    INNER JOIN utilizador ON faixa_preferida.utilizador_id = utilizador.utilizador_id
    WHERE utilizador.nacionalidade = 'Espanha';

/* EXERCICIO g */

    /* a */
    SELECT cantor.nome FROM cantor
        INNER JOIN album ON cantor.cantor_id = album.cantor_id;

/* EXERCICIO h */

    /* a */
    UPDATE cantor SET nome = 'Boss AC' WHERE cantor_id = 2;

    /* b */
    SET SQL_SAFE_UPDATES = 0;
    DELETE FROM faixa
    WHERE faixa.album_id
              = (SELECT album.album_id FROM album WHERE album.titulo = 'Sempre');
    SET SQL_SAFE_UPDATES = 1;