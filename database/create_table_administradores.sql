CREATE TABLE administradores (
    num_doc VARCHAR PRIMARY KEY
                    NOT NULL
                    REFERENCES pass_role (num_doc),
    nombre  VARCHAR NOT NULL,
    email   VARCHAR NOT NULL
);