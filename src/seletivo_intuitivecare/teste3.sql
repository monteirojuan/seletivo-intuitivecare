CREATE TABLE relatorio_cadop
(
    id                  SERIAL,
    registro_ans        integer,
    cnpj                VARCHAR(14),
    razao_social        VARCHAR(255),
    nome_fantasia       VARCHAR(255),
    modalidade          VARCHAR(50),
    logradouro          VARCHAR(255),
    numero              VARCHAR(50),
    complemento         VARCHAR(255),
    bairro              VARCHAR(255),
    cidade              VARCHAR(255),
    uf                  VARCHAR(2),
    cep                 VARCHAR(8),
    ddd                 varchar(2),
    telefone            VARCHAR(9),
    fax                 VARCHAR(9),
    endereco_eletronico VARCHAR(255),
    representante       VARCHAR(255),
    cargo_representante VARCHAR(255),
    data_registro       DATE,
    PRIMARY KEY (id)
);

COPY relatorio_cadop FROM PROGRAM 'tail -n +3 /public/relatorio_cadop.csv' DELIMITER ',' CSV;

CREATE TABLE demonstracao_contabil
(
    id                SERIAL,
    data              DATE,
    registro_ans      INTEGER,
    cd_conta_contabil VARCHAR(50),
    descricao         VARCHAR(255),
    vl_saldo_inicial  FLOAT,
    vl_saldo_final    FLOAT,
    PRIMARY KEY (id)
);

COPY demonstracao_contabil FROM PROGRAM 'tail -n +1 /public/1T2021.csv' DELIMITER ',' CSV;
COPY demonstracao_contabil FROM PROGRAM 'tail -n +1 /public/2T2021.csv' DELIMITER ',' CSV;
COPY demonstracao_contabil FROM PROGRAM 'tail -n +1 /public/3T2021.csv' DELIMITER ',' CSV;
COPY demonstracao_contabil FROM PROGRAM 'tail -n +1 /public/4T2021.csv' DELIMITER ',' CSV;
COPY demonstracao_contabil FROM PROGRAM 'tail -n +1 /public/1T2020.csv' DELIMITER ',' CSV;
COPY demonstracao_contabil FROM PROGRAM 'tail -n +1 /public/2T2020.csv' DELIMITER ',' CSV;
COPY demonstracao_contabil FROM PROGRAM 'tail -n +1 /public/3T2020.csv' DELIMITER ',' CSV;
COPY demonstracao_contabil FROM PROGRAM 'tail -n +1 /public/4T2020.csv' DELIMITER ',' CSV;