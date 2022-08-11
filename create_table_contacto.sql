CREATE TABLE contacto (
    id_contacto INTEGER       PRIMARY KEY AUTOINCREMENT,
    num_doc     VARCHAR       REFERENCES pass_role (num_doc) 
                              NOT NULL,
    nombre      VARCHAR       NOT NULL,
    email       VARCHAR       NOT NULL,
    comentario  VARCHAR (500) 
);