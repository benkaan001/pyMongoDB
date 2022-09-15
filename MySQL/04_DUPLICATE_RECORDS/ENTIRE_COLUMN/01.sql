SELECT *
FROM cars
WHERE ID IN
            (SELECT MAX(id)
            FROM cars
            GROUP BY model, brand
            HAVING COUNT(*) > 1)