SELECT day, emp_id, SUM(total_out_time-total_in_time) AS total_time
FROM
(SELECT event_day AS day, emp_id, SUM(in_time) AS total_in_time, SUM(out_time) AS total_out_time
FROM Employees
GROUP BY event_day, emp_id) a
GROUP BY day, emp_id;

SELECT 
    event_day AS day, 
    emp_id, 
    SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY 1, 2

-- separate sum then subtract
select
    event_day as day, emp_id
    , sum(out_time) - sum(in_time) as total_time
from 
    Employees
group by 
    event_day, emp_id