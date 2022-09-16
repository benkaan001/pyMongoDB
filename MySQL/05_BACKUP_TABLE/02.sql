DROP TABLE IF EXISTS cars_backup;

CREATE TABLE IF NOT EXISTS cars_backup
AS
SELECT *
FROM cars
WHERE 1=0;

INSERT INTO cars_backup
AS
SELECT *
FROM cars
WHERE id NOT IN
                (SELECT MIN(id)
                FROM cars
                GROUP BY model, brand
                HAVING COUNT(id) > 1 )

TRUNCATE table cars;

INSERT INTO cars
AS
SELECT * FROM cars_backup;

DROP TABLE cars_backup;