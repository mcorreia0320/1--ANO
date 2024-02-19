USE livraria;

INSERT INTO autor (autor_id, nome, apelido) VALUES
(1, 'Machado', 'de Assis'),
(2, 'Mia', 'Couto'),
(3, 'José', 'Saramago'),
(4, 'Stephen', 'King'),
(5, 'Eduardo', 'Galeano'),
(6, 'Júlio', 'Verne'),
(7, 'Lima', 'Barreto');

INSERT INTO livro(livro_id, nome, ano_publicacao, autor_id, genero) VALUES
(1, 'Último Caderno de Lanzarote', 2018, 4, 'Acção'),
(2, 'Areias Brancas', 2018, 2, 'Terror'),
(3, 'Foi Sem Querer Que Te Quis', 2018, 5, 'Drama'),
(4, 'Next Level', 2019, 4, 'Comédia'),
(5, 'A Outra Mulher', 2019, 2, 'Acção'),
(6, 'Nobre & Poderoso', 2019, 1, 'Terror'),
(7, 'Coração em Chamas', 2019, 3, 'Drama');

INSERT INTO utilizador (utilizador_id, username) VALUES
(1, 'antoniogoncalves'),
(2, 'JoelPereira'),
(3, 'jessicaMartins'),
(4, 'BrunaSilva'),
(5, 'ricardoazevedo'),
(6, 'valerio_gomes'),
(7, 'davidjoao'),
(8, 'JoseAfonso');

INSERT INTO favorito (livro_id, utilizador_id) VALUES
(1, 1),
(2, 1),
(2, 2),
(3, 2),
(7, 2),
(4, 3),
(6, 3),
(4, 4),
(7, 4),
(5, 5),
(5, 6),
(4, 5),
(6, 4),
(7, 6);
