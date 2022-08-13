CREATE TABLE reservaciones (
    codigo_reserva INTEGER PRIMARY KEY AUTOINCREMENT
                           NOT NULL,
    num_doc        VARCHAR REFERENCES huespedes (num_doc) 
                           NOT NULL,
    fecha_inicio   DATE    NOT NULL,
    fecha_fin      DATE    NOT NULL,
    num_habitacion INTEGER REFERENCES habitaciones (num_habitacion) 
                           NOT NULL
);