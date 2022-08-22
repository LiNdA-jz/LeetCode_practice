SELECT day, emp_id, SUM(total_out_time-total_in_time) AS total_time
FROM
(SELECT event_day AS day, emp_id, SUM(in_time) AS total_in_time, SUM(out_time) AS total_out_time
FROM Employees
GROUP BY event_day, emp_id) a
GROUP BY day, emp_id;