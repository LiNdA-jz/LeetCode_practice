-- SELECT employee_id,
-- CASE
--     WHEN employee_id % 2 != 0 AND name NOT LIKE "M%" THEN salary
--     ELSE 0
-- END AS bonus
-- FROM Employees
-- ORDER BY employee_id;

-- faster
SELECT employee_id,
CASE
    WHEN LEFT(name,1) != 'M' AND MOD(employee_id,2)=1 THEN salary
    ELSE 0
END AS bonus

FROM Employees ORDER BY employee_id;