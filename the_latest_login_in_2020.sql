SELECT user_id, MAX(time_stamp) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp) = '2020'
GROUP BY user_id;

-- like
select user_id, max(time_stamp) 'last_stamp'
from logins
where time_stamp like '2020%'
group by user_id ;