CREATE DATABASE IF NOT EXISTS cars_db2;

CREATE TABLE IF NOT EXISTS cars(
    id INT,
    model VARCHAR(50),
    brand VARCHAR(50),
    color VARCHAR(30),
    make INT
)

INSERT INTO cars VALUES (1, 'Model S', 'Tesla', 'Blue', 2018);
INSERT INTO cars VALUES (2, 'EQS', 'Mercedes-Benz', 'Black', 2022);
INSERT INTO cars VALUES (3, 'iX', 'BMW', 'Red', 2022);
INSERT INTO cars VALUES (4, 'Ioniq 5', 'Hyundai', 'White', 2021);
INSERT INTO cars VALUES (1, 'Model S', 'Tesla', 'Blue', 2018);
INSERT INTO cars VALUES (4, 'Ioniq 5', 'Hyundai', 'White', 2021);


SELECT * FROM cars;

-- (1, 'Model S', 'Tesla', 'Blue', 2018)
-- (2, 'EQS', 'Mercedes-Benz', 'Black', 2022)
-- (3, 'iX', 'BMW', 'Red', 2022)
-- (4, 'Ioniq 5', 'Hyundai', 'White', 2021)
-- (1, 'Model S', 'Tesla', 'Blue', 2018)
-- (4, 'Ioniq 5', 'Hyundai', 'White', 2021)