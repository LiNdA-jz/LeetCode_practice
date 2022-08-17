-- cannot use full outer join in leetcode
-- SELECT employee_id
-- FROM
-- (SELECT *
-- FROM Employees a
-- FULL JOIN Salaries b
-- ON a.employee_id = b.employee_id) c
-- WHERE c.name IS NULL OR c.salary IS NULL
-- ORDER BY employee_id;

-- union & not in
SELECT employee_id FROM Employees WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION 
SELECT employee_id FROM Salaries WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY 1 ASC

-- full join by left join union right join -> faster
SELECT T.employee_id
FROM  
  (SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
   UNION 
   SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id))
AS T
WHERE T.salary IS NULL OR T.name IS NULL
ORDER BY employee_id;