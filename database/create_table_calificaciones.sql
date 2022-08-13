CREATE TABLE calificaciones (
    id_calificacion INTEGER PRIMARY KEY AUTOINCREMENT
                            NOT NULL,
    num_doc         VARCHAR REFERENCES huespedes (num_doc) 
                            NOT NULL,
    num_habitacion  INTEGER REFERENCES habitaciones (num_habitacion) 
                            NOT NULL,
    codigo_reserva  INTEGER REFERENCES reservaciones (codigo_reserva) 
                            NOT NULL,
    comentarios     VARCHAR,
    calificacion    INTEGER
);
