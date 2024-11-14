CREATE TABLE IF NOT EXISTS apartamentos (
    id SERIAL PRIMARY KEY,
    numero INT,
    ocupado BOOLEAN,
    ingreso NUMERIC
);

CREATE TABLE IF NOT EXISTS mantenimientos (
    id SERIAL PRIMARY KEY,
    apartamento_id INT REFERENCES apartamentos(id),
    fecha_solicitud TIMESTAMP,
    fecha_resolucion TIMESTAMP
);

CREATE TABLE IF NOT EXISTS encuestas (
    id SERIAL PRIMARY KEY,
    apartamento_id INT REFERENCES apartamentos(id),
    puntuacion INT CHECK (puntuacion BETWEEN 1 AND 5)
);

INSERT INTO apartamentos (numero, ocupado, ingreso) VALUES
(101, TRUE, 1500), (102, FALSE, NULL), (103, TRUE, 2000);

INSERT INTO mantenimientos (apartamento_id, fecha_solicitud, fecha_resolucion) VALUES
(101, '2024-01-01 10:00', '2024-01-02 10:00'),
(103, '2024-01-03 11:00', NULL);

INSERT INTO encuestas (apartamento_id, puntuacion) VALUES
(101, 4), (103, 5);