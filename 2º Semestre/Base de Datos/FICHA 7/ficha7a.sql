USE livraria1_1;

/* EXERCICIO E */
/* i. */
SELECT livro.titulo, editora.nome FROM livro
    INNER JOIN editora ON editora.editora_id = livro.editora_id
    WHERE editora.nome = 'Manuscrito Editora';

/* ii. */
SELECT COUNT(*) AS 'Total de leitores' FROM leitor;

/* iii. */
SELECT editora.nome,COUNT(*) AS 'Livros por editora' FROM livro
        INNER JOIN editora ON editora.editora_id = livro.editora_id
        GROUP BY livro.editora_id;

/* iv. */
SELECT palavra AS 'Palavras chaves para Next Level' FROM palavra_chave
        INNER JOIN livro_palavra ON livro_palavra.palavra_id = palavra_chave.palavra_id
        INNER JOIN livro ON livro.livro_id = livro_palavra.livro_id
        WHERE livro.titulo = 'Next Level'
        ORDER BY palavra;

/* v. */
SELECT data_requisicao AS 'Requisições feitas em 2019', leitor.nome FROM requisicao
        INNER JOIN leitor ON requisicao.leitor_id = leitor.leitor_id
        WHERE YEAR(data_requisicao) = '2019' AND leitor.nome = 'Joel Pereira';

/* vi. */
SELECT leitor.leitor_id,leitor.nome, COUNT(*) AS 'Total' FROM requisicao
        INNER JOIN leitor ON requisicao.leitor_id = leitor.leitor_id
        GROUP BY leitor.nome, leitor.leitor_id
        HAVING Total > 0
        ORDER BY leitor_id;

/* vii. */
SELECT livro.titulo AS 'Nome dos livros requisitados por Joel', requisicao.data_requisicao,
        requisicao.valor_multa AS 'Multa' FROM livro
        INNER JOIN exemplar ON livro.livro_id = exemplar.livro_id
        INNER JOIN requisicao ON exemplar.exemplar_id = requisicao.exemplar_id
        INNER JOIN leitor ON requisicao.leitor_id = leitor.leitor_id
        WHERE leitor.nome = 'Joel Pereira' AND requisicao.valor_multa IS NOT NULL;

/* viii. */
SELECT autor.autor_id, autor.nome AS 'Autores do livro Areias Brancas' FROM autor
        INNER JOIN livro_autor ON autor.autor_id = livro_autor.autor_id
        INNER JOIN livro ON livro_autor.livro_id = livro.livro_id
        WHERE livro.titulo = 'Areias Brancas';

/* ix. */
SELECT livro.livro_id, livro.titulo, leitor.localidade
        FROM livro
        INNER JOIN exemplar ON livro.livro_id = exemplar.livro_id
        INNER JOIN requisicao ON exemplar.exemplar_id = requisicao.exemplar_id
        INNER JOIN leitor ON requisicao.leitor_id = leitor.leitor_id
        WHERE leitor.localidade IN ('Funchal')
        GROUP BY livro.titulo
        ORDER BY livro.livro_id;
