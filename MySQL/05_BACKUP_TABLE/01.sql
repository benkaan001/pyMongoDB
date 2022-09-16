CREATE TABLE IF NOT EXISTS cars_backup
AS
SELECT *
FROM cars
WHERE id NOT IN
                (SELECT MAX(id)
                FROM cars
                GROUP BY brand, model
                HAVING COUNT(*) > 1);

DROP TABLE cars;

ALTER TABLE cars_backup RENAME TO cars;