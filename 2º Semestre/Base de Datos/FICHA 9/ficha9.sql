/* 1. Para que serve a indexação? */

/* A indexação consiste numa estrutura adicional que permite simular a ordenação dos dados. Na realidade,
baseia-se normalmente numa “árvore” de termos ou valores que apontam para uma determinada posição na
tabela. Serve como um metodo para procurar informação numa sequencia mais reduzida, comparando
o tamanho das letras segundo a ordem alfabetica. Por exemplo: D > A, porque D vem depois que A. */

/* 2. Quais são os três tipos de índices? */

/* 1º --> Indice Simples */
/* 2º --> Indice Composto */
/* 3º --> Indice Unico */

/* 3. Qual a finalidade dos seguintes comandos: */

    /* a. CREATE INDEX */

        /* Serve para criar um índice numa tabela, valores duplicados são permitidos, neste
            é designado os campos a tratar. */

    /* b. CREATE UNIQUE INDEX */

        /* Serve para criar um índice numa tabela, valores duplicados não são permitidos. */

    /* c. DROP INDEX */

        /* Serve para apagar um índice numa tabela */

    /* d. SHOW INDEXES */

        /* Serve para apresentar os índices existentes numa tabela */

/* 4. As chaves primárias têm sempre um índice associado. */

/* La afirmación es verdadera.
   Las claves primarias en una base de datos siempre tienen un índice asociado.
   Un índice es una estructura de datos que se utiliza para mejorar el rendimiento
   de las consultas en una base de datos. El índice se crea sobre una o varias columnas
   de una tabla y contiene una referencia a la ubicación física de los datos almacenados
   en la tabla. Al crear un índice sobre la clave primaria, se garantiza la unicidad de
   cada fila en la tabla, y se permite una búsqueda rápida y eficiente de los datos utilizando
   la clave primaria. */

/* 5. */

/* La afirmación es falsa. Por defecto, en MySQL, las claves foráneas (o claves externas)
   sí tienen un índice asociado.

   Cuando se crea una clave foránea en una tabla de MySQL, se crea automáticamente un índice
   en la columna o columnas que se usan para hacer referencia a la clave primaria de otra
   tabla. Este índice se llama "índice de clave foránea" (foreign key index) y se utiliza
   para optimizar las operaciones de búsqueda y actualización de datos que involucran la
   clave foránea.

   Es cierto que, en algunos casos, puede ser necesario ajustar manualmente la creación
   de índices en las claves foráneas, especialmente si se trabaja con grandes volúmenes de
   datos o si se realizan operaciones de actualización masiva. Sin embargo, en general,
   MySQL crea un índice en las claves foráneas de forma predeterminada para garantizar la
   eficiencia y la integridad de los datos en la base de datos. */

/* 6. */

    /* a. */
        CREATE INDEX index_nome
        ON jogador(nome);

    /* b. */
        CREATE UNIQUE INDEX index_funcao
        ON jogador(funcao);

    /* c. */
       /* Não, porque se forem inseridos mais jogador com a mesma função não vão ser
          considerados na consulta, porque o indice unico não admite duplicados. */