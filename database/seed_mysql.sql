USE portafolio_clientes_pedidos;

INSERT INTO cliente (nombre, ciudad, telefono, edad) VALUES
('Juan', 'Bogota', '3001234567', 20),
('Julieta', 'Medellin', '3156201367', 25),
('Carlos', 'Cali', '3205557788', 30),
('Laura', 'Barranquilla', '3005551234', 22),
('Andres', 'Bogota', '3109998877', 28);

INSERT INTO pedido (fecha, valor, id_cliente) VALUES
('2026-01-10', 150000, 1),
('2026-01-12', 230000, 2),
('2026-01-13', 90000, 1),
('2026-01-15', 310000, 3),
('2026-01-20', 180000, 5);
