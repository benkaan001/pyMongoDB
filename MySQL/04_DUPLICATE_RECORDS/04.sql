SELECT MIN(id)
FROM cars
GROUP BY brand, model
HAVING COUNT(*) > 1

-- (1,)
-- (4,)

SELECT *
FROM cars
WHERE id NOT IN
                (SELECT MIN(id)
                FROM cars
                GROUP BY model, brand
                HAVING COUNT(*) > 1)

-- (1, 'Model S', 'Tesla', 'Blue', 2018)
-- (2, 'EQS', 'Mercedes-Benz', 'Black', 2022)
-- (3, 'iX', 'BMW', 'Red', 2022)
-- (4, 'Ioniq 5', 'Hyundai', 'White', 2021)