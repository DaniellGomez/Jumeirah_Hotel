CREATE TABLE contacto (
    num_doc    VARCHAR       PRIMARY KEY
                             REFERENCES pass_role (num_doc) 
                             NOT NULL,
    nombre     VARCHAR       NOT NULL,
    email      VARCHAR       NOT NULL,
    comentario VARCHAR (500) 
);