
/* DDL PROJETO BASE DE DADOS - JACKELINE CAMARA E MIGUEL PEÑARANDA */


CREATE SCHEMA projeto_sgbd;

USE projeto_sgbd;

CREATE TABLE usuario(
    usuario_id INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    apelido VARCHAR(50) NOT NULL,
    idade INT,
    PRIMARY KEY (usuario_id)
);

CREATE TABLE transporte(
    transporte_id INT AUTO_INCREMENT NOT NULL,
    tipo_transporte VARCHAR(100),
    PRIMARY KEY (transporte_id)
);

CREATE TABLE usuario_transporte(
    usuario_id INT NOT NULL,
    transporte_id INT NOT NULL,
    distancia_percorrida FLOAT,
    emissao_co2 FLOAT,
    PRIMARY KEY (usuario_id, transporte_id),
    FOREIGN KEY (usuario_id)
                REFERENCES usuario(usuario_id),
    FOREIGN KEY (transporte_id)
                REFERENCES transporte(transporte_id)
);

CREATE TABLE dieta(
    dieta_id INT AUTO_INCREMENT,
    tipo_dieta VARCHAR(100) NOT NULL,
    PRIMARY KEY (dieta_id)
);

CREATE TABLE habito_alimenticio(
    habito_alimenticio_id INT NOT NULL AUTO_INCREMENT,
    produtos_locais BOOLEAN NOT NULL,
    emissao_co2 FLOAT NOT NULL,
    usuario_id INT NOT NULL,
    dieta_id INT NOT NULL,
    PRIMARY KEY (habito_alimenticio_id),
    FOREIGN KEY (usuario_id)
                REFERENCES usuario(usuario_id),
    FOREIGN KEY (dieta_id)
                REFERENCES dieta(dieta_id)
);

CREATE TABLE postal(
    postal_id INT AUTO_INCREMENT,
    codigo VARCHAR(15) NOT NULL,
    PRIMARY KEY (postal_id)
);

CREATE TABLE consumo_eletrico(
    consumo_eletrico_id INT AUTO_INCREMENT,
    consumo_mensal FLOAT NOT NULL,
    emissao_co2 FLOAT NOT NULL,
    PRIMARY KEY (consumo_eletrico_id)
);

CREATE TABLE consumo_gas(
    consumo_gas_id INT AUTO_INCREMENT,
    consumo_mensal FLOAT NOT NULL,
    emissao_co2 FLOAT NOT NULL,
    PRIMARY KEY (consumo_gas_id)
);

CREATE TABLE hogar(
    hogar_id INT AUTO_INCREMENT NOT NULL ,
    quantidade_pessoa INT NOT NULL,
    tamanho FLOAT NOT NULL,
    endereço VARCHAR(250),
    reciclagem BOOLEAN NOT NULL,
    total_emissao_co2 FLOAT NOT NULL,
    postal_id INT NOT NULL,
    consumo_eletrico_id INT NOT NULL,
    consumo_gas_id INT NOT NULL,
    usuario_id INT NOT NULL,
    PRIMARY KEY (hogar_id),
    FOREIGN KEY (postal_id)
                REFERENCES postal(postal_id),
    FOREIGN KEY (consumo_eletrico_id)
                REFERENCES consumo_eletrico(consumo_eletrico_id),
    FOREIGN KEY (consumo_gas_id)
                  REFERENCES consumo_gas(consumo_gas_id),
    FOREIGN KEY (usuario_id)
                REFERENCES usuario(usuario_id)
);

CREATE TABLE recomendacao(
    recomendacao_id INT AUTO_INCREMENT,
    titulo VARCHAR(50) NOT NULL,
    descricao VARCHAR(1000) NOT NULL,
    PRIMARY KEY (recomendacao_id)
);

CREATE TABLE hogar_recomendacao(
    hogar_id INT NOT NULL,
    recomendacao_id INT NOT NULL,
    PRIMARY KEY (hogar_id,recomendacao_id),
    FOREIGN KEY (hogar_id)
                REFERENCES hogar(hogar_id),
    FOREIGN KEY (recomendacao_id)
                REFERENCES recomendacao(recomendacao_id)
);

