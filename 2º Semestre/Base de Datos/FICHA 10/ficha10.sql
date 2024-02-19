/* 1. */

    /* O MySQL encripta a password antes de guardar o utilizador na
tabela user. */

/* 2. */

    /* Após a criação de um novo utilizador deve-se conceder-lhe alguns privilegios com o comando
       GRANT. */

/* 3. */

    /* 1º Forma */
        UPDATE user
        SET password = PASSWORD('golfinho')
        WHERE user = 'name_user' AND host = 'localhost';

    /* 2º Forma */
        SET PASSWORD FOR 'name_user'@'localhost'= PASSWORD('tuburao');

    /* 3º Forma */
            ALTER USER 'name_user'@'localhost' IDENTIFIED BY 'teste';

/* 4. */

        /* Serve para apresentar as informações do utilizador actual.
            Comando alternativo: SELECT current_user(); */

/* 5. */

        /*  Por username, password(encriptada), servidor y privilegios */

/* 6. */

        /* a. */
            CREATE USER 'departamento_financeiro'@'localhost' IDENTIFIED BY '123456';

        /* b. */
            SELECT user();

        /* c. */
            SHOW GRANTS FOR 'departamento_financeiro'@'localhost';

/* 7. */

        /* Os dois comandos dos privilegios são GRANT e REVOKE.
            GRANT serve para conceder privilegios a um ou mais usuarios.
            REVOKE serve para anular os privilegios concedidos a um ou mais usuarios.*/

/* 8. */

        /* Os privilegios são aplicados ás tabelas ou base de dados */

/* 9. */
            GRANT SELECT ON musica.* TO 'departamento'@'localhost';

/* 10. */

        /* a. */
            CREATE USER 'stock'@'localhost' IDENTIFIED BY '123456';

        /* b. */
            GRANT SELECT, INSERT ON musica.cantor TO 'stock'@'localhost';
            GRANT SELECT, INSERT ON  musica.abum TO 'stock'@'localhost';

        /* c. */
            GRANT UPDATE ON livraria.* TO 'stock'@'localhost';

        /* d. */
            SHOW GRANTS FOR 'stock'@'localhost';

/* 11. */
        GRANT ALL PRIVILEGES ON musica TO 'stock'@'localhost';

/* 12. */
        REVOKE INSERT ON musica FROM 'stock'@'localhost';
        SHOW GRANTS FOR 'stock'@'localhost';


