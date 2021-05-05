CREATE TABLE example.example_table
(
    id   BIGINT(20)   NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    year INT          NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `name_UNIQUE` (`name`)
);

INSERT INTO example.example_table (name, year)
VALUES ('Carl Sagan', 1934),
       ('Richard Feynman', 1918);

