DROP TABLE IF EXISTS cars_backup;

CREATE TABLE IF NOT EXISTS cars_backup
AS
SELECT * FROM cars
WHERE 1=0;

INSERT INTO cars_backup
VALUES
    SELECT *
    FROM cars
    WHERE id IN
                (SELECT MAX(id)
                FROM cars
                GROUP BY model, brand
                HAVING COUNT(*) > 1)

SELECT * FROM cars_backup;

-- (5, 'Model S', 'Tesla', 'Silver', 2018)
-- (6, 'Ioniq 5', 'Hyundai', 'Green', 2021)

DROP TABLE cars_backup;
