SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date > '2019-06-27' AND activity_date <= '2019-07-27'
AND activity_type IS NOT NULL
GROUP BY activity_date;

-- use datediff
SELECT
     activity_date as day,
    COUNT(DISTINCT user_id) as active_users
    
FROM Activity
where 
    datediff('2019-07-27', activity_date) < 30
        and
    activity_date <= '2019-07-27'
GROUP BY activity_date

-- use HAVING
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
GROUP BY activity_date
HAVING COUNT(DISTINCT user_id)>0 AND activity_date <= '2019-07-27' AND activity_date > subdate('2019-07-27', 30)