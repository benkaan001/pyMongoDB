SELECT MAX(id)
FROM cars
GROUP BY model, brand
HAVING COUNT(*) > 1;

-- (5,)
-- (6,)


SELECT *
FROM cars
WHERE id IN
            (SELECT MAX(id)
            FROM cars
            GROUP BY model, brand
            HAVING COUNT(*) > 1);


-- (5, 'Model S', 'Tesla', 'Silver', 2018)
-- (6, 'Ioniq 5', 'Hyundai', 'Green', 2021)