SELECT c1.id
FROM cars c1
INNER JOIN cars c2
ON c1.model = c2.model AND c1.brand = c2.brand
WHERE c1.id > c2.id

-- (5,)
-- (6,)


SELECT *
FROM cars
WHERE id IN
            (SELECT c1.id
            FROM cars c1
            INNER JOIN cars c2
            ON c1.model = c2.model AND c1.brand = c2.brand
            WHERE c1.id > c2.id)

-- (5, 'Model S', 'Tesla', 'Silver', 2018)
-- (6, 'Ioniq 5', 'Hyundai', 'Green', 2021)