CREATE DATABASE IF NOT EXISTS database_desafio;

CREATE TABLE pessoas(
  `id_pessoa` TINYINT(255) NOT NULL AUTO_INCREMENT,
  `nome` CHAR(100) NOT NULL,
  `rg` CHAR(100) NOT NULL,
  `cpf` CHAR(100) NOT NULL,
  `data_nascimento` DATE NOT NULL,
  `data_admissao` DATE NOT NULL,
  `funcao` CHAR(100) NULL,
PRIMARY KEY (`id_pessoa`));