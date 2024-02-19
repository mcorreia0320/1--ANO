
/* DML PROJETO BASE DE DADOS - JACKELINE CAMARA E MIGUEL PEÑARANDA */

USE projeto_sgbd;

/* INSERT VALUES ON TABLES */

INSERT INTO usuario(nome, apelido, idade)
            VALUES ("Jacky","Camara",18),
                   ("Miguel","Correia",20),
                   ("Saul", "Pinto", 23),
                   ("Roberto","Moniz",27),
                   ("Magno", "Andrade",30),
                   ("Salomon", "Villada",30),
                   ("Tiago", "Pachecho",21),
                   ("Cristiano","Aveiro",38),
                   ("Benito","Martinez", 29);

INSERT INTO transporte(tipo_transporte)
                    VALUES ("Carro"),
                           ("Moto"),
                           ("Bike"),
                           ("Bicicleta Eletrica"),
                           ("Patinete Eletrico"),
                           ("Metro"),
                           ("Autocarro"),
                           ("Ando a pé");

INSERT INTO usuario_transporte(usuario_id, transporte_id, distancia_percorrida, emissao_co2)
                    VALUES (1, 7, 100, 1.89),
                           (3, 5,750,118.30),
                           (7,6,130,2.46),
                           (4, 1,1200,202.80),
                           (2, 1,500,84.50),
                           (8, 6, 3000, 741),
                           (5, 2, 2000, 47),
                           (6, 3,200,0.10);

INSERT INTO dieta(tipo_dieta)
            VALUES ("Não faço dieta"),
                   ("Vegetarian"),
                   ("Vegan");

INSERT INTO habito_alimenticio(produtos_locais, emissao_co2, usuario_id, dieta_id)
            VALUES (0, 27.2, 1, 1),
                   (1, 1.3, 6, 3),
                   (1,35.2,2,1),
                   (1,37.1,4,1),
                   (0, 3.4,7,2),
                   (0,4.1, 8, 2),
                   (1,26.5,5,1),
                   (1,21.3,3,1);

INSERT INTO postal(codigo)
            VALUES ("9000-210"),
                   ("9060-415"),
                   ("9020-105"),
                   ("9004-512"),
                   ("9070-602"),
                   ("9050-041"),
                   ("9030-306"),
                   ("9010-703");

INSERT INTO consumo_gas(consumo_mensal, emissao_co2)
              VALUES (50.4, 260),
                     (20.4, 110),
                     (30.7, 170),
                     (45.1, 210.3),
                     (80.4, 402.1),
                     (101.7, 517.3),
                     (47.3, 220.7),
                     (55.2, 278.6);

INSERT INTO consumo_eletrico(consumo_mensal, emissao_co2)
              VALUES (51.2, 11.5),
                     (10.5, 2.3),
                     (30.1, 6.6),
                     (40.7, 9.4),
                     (90.3, 19.9),
                     (120, 26.4),
                     (74.7,16.4),
                     (55.5,12.3);

INSERT INTO recomendacao(titulo, descricao)
              VALUES ("Aprovecha la luz natural","Abra cortinas e persianas durante o dia para aproveitar a luz natural em vez de usar luzes elétricas. Isso ajudará a reduzir o consumo
                     de eletricidade para iluminar sua casa."),
                     ("Use lâmpadas LED eficientes", "Substitua lâmpadas incandescentes por lâmpadas LED de alta eficiência energética. As lâmpadas LED consomem menos eletricidade e têm
                     uma vida útil mais longa, reduzindo o consumo e os custos a longo prazo."),
                     ("Desligue dispositivos em modo de espera", "Muitos dispositivos eletrônicos continuam consumindo energia mesmo quando estão em modo de espera.
                     Desligue-os completamente quando não estiverem em uso para evitar consumo desnecessário de eletricidade."),
                     ("Use eletrodomésticos eficientes", "Escolha eletrodomésticos com alta eficiência energética, como máquinas de lavar roupa, geladeiras e aparelhos de ar condicionado.
                     Esses eletrodomésticos consomem menos eletricidade em comparação com modelos menos eficientes."),
                     ("Isola adequadamente a tua casa", "Melhora o isolamento da tua casa para evitar fugas de calor. Certifica-te de que as janelas e portas estão bem seladas e considera
                     adicionar isolamento adicional em paredes, sótãos e pisos. Isso ajudará a reter o calor e reduzir a necessidade de usar aquecimento a gás."),
                     ("Utiliza termostatos programáveis","Instala um termostato programável para controlar a temperatura da tua casa. Programa temperaturas mais baixas durante as horas em
                     que não estás em casa ou durante a noite, quando estás a dormir. Isso reduzirá o tempo de funcionamento do sistema de aquecimento e, portanto, o consumo de gás."),
                     ("Manutenção do teu sistema de aquecimento", "Certifica-te de fazer a manutenção regular do teu sistema de aquecimento a gás. Limpa e verifica regularmente os
                     radiadores, purga os radiadores para remover o ar acumulado e programa uma revisão anual por um profissional para garantir que o sistema funcione de forma eficiente."),
                     ("Utiliza cortinas e persianas","Aproveita o calor do sol abrindo cortinas e persianas durante o dia para deixar entrar a luz solar e aquecer naturalmente a tua casa.
                     À noite, fecha as cortinas e persianas para isolar melhor as janelas e evitar a perda de calor."),
                     ("Reduza o consumo de carne","Diminua a quantidade de carne que consome e opte por mais opções à base de plantas, como frutas, legumes, grãos e leguminosas. A produção
                     e carne tem um alto impacto ambiental devido à emissão de gases de efeito estufa."),
                     ("Escolha alimentos sazonais e locais", "Priorize alimentos sazonais e produzidos localmente. Isso reduz a necessidade de transportar produtos a longas distâncias,
                     o que, por sua vez, reduz as emissões de CO2 associadas ao transporte."),
                     ("Evite o desperdício de alimentos","Planeje suas refeições e compre apenas o necessário. Aproveite ao máximo os alimentos e evite jogar comida fora. O desperdício
                     de alimentos contribui para o impacto ambiental e as emissões de CO2 geradas durante a produção."),
                     ("Opte por alimentos orgânicos","Escolha alimentos cultivados sem o uso de pesticidas e fertilizantes químicos. Métodos agrícolas sustentáveis
                     podem ajudar a reduzir as emissões de CO2 e o impacto ambiental.");


INSERT INTO hogar(quantidade_pessoa, tamanho, endereço, reciclagem, total_emissao_co2, postal_id, consumo_eletrico_id, consumo_gas_id, usuario_id)
              VALUES (3,120.4,"Rua da Liberdade, Residencial Flores, 123, 2B",0,234.3,2,1,5,7),
                     (1,80.5,"Travessa das Flores, Casa dos Sonhos, 25", 1, 50.2, 8, 3, 4, 8),
                     (5,160.7,"Avenida do Mar, Edifício Atlântico, 56, 3", 1, 102.3,1,7,1,1),
                     (2,90,"Rua dos Girassóis, Villa Sol, 7", 0, 40.3, 4, 5, 2, 3),
                     (1, 100, "Caminho do Leão, Quinta da Vista, 10, 1", 1, 35.5, 3, 4, 7, 4),
                     (4, 130, "Rua da Paz, Casa Bela Vista, 32", 1, 183.4, 5, 6, 3, 2),
                     (1, 92.4, "Rua das Palmeiras, Residencial Sol Nascente, 18, 1A", 0, 40.1, 6, 2, 6, 5),
                     (3, 140.5, "Avenida da República, Edifício Central, 88, 4C", 1, 63.6, 7, 8, 8, 6);

INSERT INTO hogar_recomendacao(hogar_id, recomendacao_id)
              VALUES (2, 5),
                     (5, 1),
                     (1, 3),
                     (4, 2),
                     (3,8),
                     (6,4),
                     (7,6),
                     (8,7),
                     (2,1),
                     (2,8),
                     (4,5),
                     (4,12),
                     (7, 9),
                     (7,2);

/* QUERIES */

UPDATE usuario SET usuario.nome = "Lorenzo" WHERE usuario_id = 6;
UPDATE usuario_transporte SET distancia_percorrida = 40.2 WHERE usuario_id = 4;
UPDATE transporte SET tipo_transporte = "Avião" WHERE transporte_id = 1;
UPDATE habito_alimenticio SET produtos_locais = 0 WHERE usuario_id = 2;
UPDATE dieta SET tipo_dieta = "Omnivoro" WHERE dieta_id = 3;
UPDATE hogar SET quantidade_pessoa = 2 WHERE hogar_id = 3;
UPDATE postal SET codigo = 9000-250 WHERE postal_id = 5;
UPDATE consumo_gas SET consumo_mensal = 80.3 WHERE consumo_gas_id = 8;
UPDATE consumo_eletrico SET emissao_co2 = 30.5 WHERE consumo_eletrico_id = 6;
UPDATE recomendacao  SET titulo = 'Cuidado eletrico' WHERE recomendacao_id = 3;


SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;


DELETE FROM usuario WHERE nome = 'Jacky';
DELETE FROM habito_alimenticio WHERE produtos_locais = 0 AND dieta_id = 2;
DELETE FROM hogar WHERE quantidade_pessoa = 2;
DELETE FROM usuario_transporte WHERE usuario_id = 7;
DELETE FROM transporte WHERE tipo_transporte = 'Autocarro';
DELETE FROM postal WHERE codigo = '9020-105';
DELETE FROM dieta WHERE tipo_dieta = 'Vegan';
DELETE FROM consumo_gas WHERE consumo_mensal > 30.1;
DELETE FROM consumo_eletrico WHERE emissao_co2 BETWEEN 30 AND 60;
DELETE FROM hogar_recomendacao WHERE hogar_id = 2 AND recomendacao_id = 5;
DELETE FROM recomendacao WHERE titulo = 'Use eletrodomésticos eficientes';

SET FOREIGN_KEY_CHECKS = 1;
SET SQL_SAFE_UPDATES = 1;

/* Que usuarios usam Carro ou Metro? */

SELECT CONCAT(usuario.nome, ' ', usuario.apelido) AS 'Usuarios que usam Carro ou Metro' FROM usuario
INNER JOIN usuario_transporte ON usuario.usuario_id = usuario_transporte.usuario_id
INNER JOIN transporte ON usuario_transporte.transporte_id = transporte.transporte_id
WHERE transporte.tipo_transporte IN ("Carro","Metro");

/* Que usuarios não consumen produtos locais */

SELECT usuario.nome AS 'Usuarios que não consumen produtos locais' FROM usuario
INNER JOIN habito_alimenticio ON usuario.usuario_id = habito_alimenticio.usuario_id
INNER JOIN dieta ON habito_alimenticio.dieta_id = dieta.dieta_id
WHERE habito_alimenticio.produtos_locais = 0 AND dieta.dieta_id = 2;

/* QUAL é o tipo de deita que tem o usuario com o nome de Jacky */

SELECT dieta.tipo_dieta AS 'Dieta de Jacky' FROM dieta
INNER JOIN habito_alimenticio ON dieta.dieta_id = habito_alimenticio.dieta_id
INNER JOIN usuario ON habito_alimenticio.usuario_id = usuario.usuario_id
WHERE usuario.nome = "Jacky";

/* Para cada usuario quantas recomendações foram atribuidas? */

SELECT usuario.nome, COUNT(recomendacao.recomendacao_id) AS 'Total de tips atribuidos' FROM usuario
LEFT JOIN hogar ON usuario.usuario_id = hogar.usuario_id
LEFT JOIN hogar_recomendacao ON hogar.hogar_id = hogar_recomendacao.hogar_id
LEFT JOIN recomendacao ON hogar_recomendacao.recomendacao_id = recomendacao.recomendacao_id
GROUP BY usuario.nome;

/* Para cada usuario quanto é o seu consumo Total de emissões, ordenado de forma ascendente? */

SELECT usuario.nome, ROUND((SUM(usuario_transporte.emissao_co2) + SUM(habito_alimenticio.emissao_co2) +
                     SUM(consumo_gas.emissao_co2) + SUM(consumo_eletrico.emissao_co2)), 2) AS 'Total de emissão'
FROM usuario
INNER JOIN habito_alimenticio ON usuario.usuario_id = habito_alimenticio.usuario_id
INNER JOIN usuario_transporte ON usuario.usuario_id = usuario_transporte.usuario_id
INNER JOIN hogar ON usuario.usuario_id = hogar.usuario_id
INNER JOIN consumo_eletrico ON hogar.consumo_eletrico_id = consumo_eletrico.consumo_eletrico_id
INNER JOIN consumo_gas ON hogar.consumo_gas_id = consumo_gas.consumo_gas_id
GROUP BY usuario.nome
ORDER BY `Total de emissão`;

/* Que usuarios moram com mais de duas pessoas? */

SELECT usuario.nome, hogar.quantidade_pessoa AS 'Total' FROM usuario
INNER JOIN hogar ON usuario.usuario_id = hogar.usuario_id
WHERE quantidade_pessoa > 2;

/* Que usuarios tem um consumo mensal eletrico menor do que 50€, ordenado de forma descendente */

SELECT usuario.nome, consumo_eletrico.consumo_mensal AS 'Total' FROM usuario
INNER JOIN hogar ON usuario.usuario_id = hogar.usuario_id
INNER JOIN consumo_eletrico ON hogar.consumo_eletrico_id = consumo_eletrico.consumo_eletrico_id
WHERE consumo_eletrico.consumo_mensal < 50
ORDER BY consumo_mensal DESC ;

/* Qual é o endereço do usuario com maior consumo de gas? */

SELECT hogar.endereço, postal.codigo, MAX(consumo_mensal) AS 'Total' FROM hogar
INNER JOIN postal ON hogar.postal_id = postal.postal_id
INNER JOIN consumo_gas ON hogar.consumo_gas_id = consumo_gas.consumo_gas_id;

/* Quantos usuarios são vegetarianas */

SELECT COUNT(usuario.usuario_id) AS 'Total de vegetarianos' FROM usuario
INNER JOIN habito_alimenticio ON usuario.usuario_id = habito_alimenticio.usuario_id
INNER JOIN dieta ON habito_alimenticio.dieta_id = dieta.dieta_id
WHERE dieta.tipo_dieta = 'Vegetarian';

/* A que pessoas foi lhe atribuida a recomendação "Isola adequadamente a tua casa" ? */

SELECT usuario.nome AS 'Pessoas que devem isolar adequadamente a sua casa' FROM usuario
INNER JOIN hogar ON usuario.usuario_id = hogar.usuario_id
INNER JOIN hogar_recomendacao ON hogar.hogar_id = hogar_recomendacao.hogar_id
INNER JOIN recomendacao ON hogar_recomendacao.recomendacao_id = recomendacao.recomendacao_id
WHERE recomendacao.titulo = 'Isola adequadamente a tua casa';

/* Que usuarios tem idade comprendida entre 25 e 45 ?*/
SELECT * FROM usuario
WHERE idade BETWEEN 25 AND 45
ORDER BY idade;










