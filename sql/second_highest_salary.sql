-- failed
SELECT IF(COUNT(a.salary)=2, a.salary, NULL) AS SecondHighestSalary
FROM
(SELECT salary
FROM Employee
ORDER BY salary DESC
LIMIT 2) a
ORDER BY salary ASC
LIMIT 1;

-- OFFSET
-- The OFFSET offset clause skips the offset rows before beginning to return the rows.
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;

-- IFNULL(expression, alt_value)
-- alt_value: The value to return if expression is NULL
-- faster
SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary

-- max
SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee)