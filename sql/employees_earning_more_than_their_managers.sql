# Write your MySQL query statement below
# SELECT e.name as Employee from Employee e INNER JOIN
# (SELECT id, name, salary FROM Employee) as manager
# ON e.managerId = manager.id
# WHERE e.salary > manager.salary;

SELECT e2.name as Employee
FROM employee e1
INNER JOIN employee e2 ON e1.id = e2.managerID
WHERE
e1.salary < e2.salary