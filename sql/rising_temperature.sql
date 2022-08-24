-- official
SELECT
    weather.id AS 'Id'
FROM
    weather
        JOIN
    weather w ON DATEDIFF(weather.recordDate, w.recordDate) = 1
        AND weather.Temperature > w.Temperature

-- to_days
SELECT wt1.Id 
FROM Weather wt1, Weather wt2
WHERE wt1.Temperature > wt2.Temperature
AND TO_DAYS(wt1.recordDate)-TO_DAYS(wt2.recordDATE)=1;

-- prev + interval
select cur.Id
from Weather cur
join Weather prev
on prev.recordDate + interval 1 day = cur.recordDate
where cur.Temperature > prev.Temperature

-- inner join
SELECT t1.Id
FROM Weather t1
INNER JOIN Weather t2
ON TO_DAYS(t1.recordDate) = TO_DAYS(t2.recordDate) + 1
WHERE t1.Temperature > t2.Temperature