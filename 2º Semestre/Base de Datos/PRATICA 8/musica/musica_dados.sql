USE musica_ficha8;

INSERT INTO cantor(cantor_id, nome) VALUES
(1, 'Tony Carreira'),
(2, 'BossAC'),
(3, 'Mariza'),
(4, 'Tiago');

INSERT INTO album (album_id, titulo, cantor_id) VALUES
(1, 'Sempre', 1),
(2, 'Manda Chuva', 2),
(3, 'Preto no Branco', 2),
(4, 'Terra', 3),
(5, 'Adeus Amigo', 1),
(6, 'Fado em Mim', 3),
(7, 'Fado Curvo', 3);

INSERT INTO faixa(faixa_id, nome_musica, album_id) VALUES
(1, 'Nunca Mais', 1),
(2, 'Sonhos de Menino', 1),
(3, 'Quem Me Dera', 4),
(4, 'Melhor De Mim', 4),
(5, 'Chuva', 4),
(6, 'Deixou-me', 2);

INSERT INTO utilizador(utilizador_id, nome, genero, nacionalidade) VALUES
(1, 'Abel', 'M', 'Portugal'),
(2, 'Carla', 'F', 'Espanha'),
(3, 'Daniel', 'M', 'Portugal'),
(4, 'Susana', 'F', 'Portugal');

INSERT INTO faixa_preferida(faixa_id, utilizador_id, pontuacao) VALUES
(1, 1, 10),
(1, 2, 7),
(2, 1, 5),
(3, 2, 6),
(4, 3, 8),
(5, 3, 10),
(6, 1, 4);