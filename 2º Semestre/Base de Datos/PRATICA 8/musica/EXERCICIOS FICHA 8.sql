USE musica_ficha8;

/* EXERCICIOS F*/

/* i. */
SELECT faixa.nome_musica FROM faixa
INNER JOIN faixa_preferida ON faixa.faixa_id = faixa_preferida.faixa_id
INNER JOIN utilizador ON utilizador.utilizador_id = faixa_preferida.utilizador_id
WHERE utilizador.nome = 'Abel';

/* ii. */
SELECT faixa.nome_musica, album.titulo FROM faixa
INNER JOIN album ON album.album_id =  faixa.album_id;

/* iii. */
SELECT COUNT(faixa.faixa_id) AS 'total_faixas', album.titulo FROM album
LEFT JOIN faixa ON album.album_id = faixa.album_id
GROUP BY album.titulo;

/* iv. */
SELECT COUNT(album.album_id) AS 'total_albums', cantor.nome FROM cantor
LEFT JOIN album ON album.cantor_id = cantor.cantor_id
GROUP BY cantor.nome;

/* v. */
SELECT COUNT(faixa.faixa_id) as 'Total_faixas', album.album_id, album.titulo FROM faixa
    INNER JOIN album ON faixa.album_id = album.album_id
    GROUP BY album.album_id, album.titulo
    HAVING Total_faixas >= 3;

/* vi. */
SELECT COUNT(faixa.faixa_id) AS 'Total de Faixas', cantor.nome FROM cantor
    LEFT JOIN album ON cantor.cantor_id = album.cantor_id
    LEFT JOIN faixa ON album.album_id = faixa.album_id
    GROUP BY cantor.nome;

/* vii. */
SELECT faixa.nome_musica AS 'Musica',SUM(faixa_preferida.pontuacao) AS 'Total Pontuação dos Portugueses' FROM utilizador
    INNER JOIN faixa_preferida ON utilizador.utilizador_id = faixa_preferida.utilizador_id
    INNER JOIN faixa ON faixa_preferida.faixa_id = faixa.faixa_id
    WHERE nacionalidade = 'Portugal'
    GROUP BY Musica;

