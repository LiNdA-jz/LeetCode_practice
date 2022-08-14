-- SELECT name, population, area
-- FROM World
-- WHERE area >= 3000000
-- OR population >= 25000000
-- GROUP BY name, population, area;

-- union
-- SELECT name, population, area
-- FROM World
-- WHERE area >= 3000000
-- UNION
-- SELECT name, population, area
-- FROM World
-- WHERE population >= 25000000;

-- faster
SELECT name, population, area
FROM
(SELECT name, population, area,
    CASE 
        WHEN area >= 3000000 THEN true
        WHEN population >= 25000000 THEN true 
        ELSE false
        END AS is_bigger FROM world) has_big
WHERE is_bigger > 0;