-- SELECT employee_id,
-- CASE
--     WHEN employee_id % 2 != 0 AND name NOT LIKE "M%" THEN salary
--     ELSE 0
-- END AS bonus
-- FROM Employees
-- ORDER BY employee_id;

-- -- faster
-- SELECT employee_id,
-- CASE
--     WHEN LEFT(name,1) != 'M' AND MOD(employee_id,2)=1 THEN salary
--     ELSE 0
-- END AS bonus

-- FROM Employees ORDER BY employee_id;

-- IF
-- IF(condition, value_if_true, value_if_false)
SELECT employee_id,
IF (employee_id % 2 != 0 AND name NOT LIKE 'M%', salary , 0) AS bonus
FROM Employees
ORDER BY employee_id;