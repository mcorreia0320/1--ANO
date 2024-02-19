USE livraria1_1;

1.
SELECT livro.* FROM livro
INNER JOIN editora ON editora.editora_id = livro.editora_id
WHERE editora.nome = 'Manuscrito Editora';

2.
SELECT COUNT (*) as 'Total de Leitores' FROM leitor;

3.
SELECT livro.editora_id, editora.nome, COUNT(*) as Total FROM livro
INNER JOIN editora ON editora.editora_id = livro.editora_id
GROUP BY livro.editora_id, editora.nome;

4.
SELECT palavra_chave.palavra FROM palavra_chave
INNER JOIN livro_palavra ON livro_palavra.palavra_id = palavra_chave.palavra_id
INNER JOIN livro ON livro.livro_id = livro_palavra.livro_id
WHERE livro.titulo = 'Next Level'
ORDER BY palavra_chave.palavra ASC;

5.
SELECT requisicao.* FROM requisicao
INNER JOIN leitor ON requisicao.leitor_id = leitor.leitor_id
WHERE leitor.nome = 'Joel Pereira' AND YEAR(requisicao.data_requisicao) = 2019;

/* Que leitores não tem requisições */
SELECT requisicao.*, leitor.* FROM leitor
LEFT JOIN requisicao ON requisicao.leitor_id = leitor.leitor_id
WHERE requisicao.requisicao_id IS NULL;

6.
SELECT leitor.leitor_id, leitor.nome, COUNT(*) AS Total FROM requisicao
INNER JOIN leitor  ON leitor.leitor_id = requisicao.leitor_id
GROUP BY leitor.leitor_id, leitor.nome;

7.
SELECT livro.titulo, requisicao.data_requisicao FROM requisicao
INNER JOIN leitor ON requisicao.leitor_id = leitor.leitor_id
INNER JOIN exemplar ON requisicao.exemplar_id = exemplar.exemplar_id
INNER JOIN livro ON exemplar.livro_id = livro.livro_id
WHERE leitor.nome = 'Joel Pereira' AND requisicao.valor_multa IS NOT NULL;