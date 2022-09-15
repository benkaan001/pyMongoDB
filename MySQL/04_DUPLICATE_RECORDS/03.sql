SELECT *, ROW_NUMBER() OVER(PARTITION BY model,brand) row_num
FROM cars;

-- (2, 'EQS', 'Mercedes-Benz', 'Black', 2022, 1)
-- (4, 'Ioniq 5', 'Hyundai', 'White', 2021, 1)
-- (6, 'Ioniq 5', 'Hyundai', 'Green', 2021, 2)
-- (3, 'iX', 'BMW', 'Red', 2022, 1)
-- (1, 'Model S', 'Tesla', 'Blue', 2018, 1)
-- (5, 'Model S', 'Tesla', 'Silver', 2018, 2)

SELECT id
FROM (SELECT *, ROW_NUMBER() OVER(PARTITION BY model,brand) row_num
FROM cars) x
WHERE x.row_num > 1;

-- (6,)
-- (5,)

SELECT *
FROM cars
WHERE id IN
			(SELECT id
			FROM (SELECT *, ROW_NUMBER() OVER(PARTITION BY model,brand) row_num FROM cars) x
			WHERE x.row_num > 1);

-- (5, 'Model S', 'Tesla', 'Silver', 2018)
-- (6, 'Ioniq 5', 'Hyundai', 'Green', 2021)