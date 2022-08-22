SELECT player_id, first_login
FROM
(SELECT player_id, event_date AS first_login
FROM Activity
GROUP BY player_id, event_date
ORDER BY event_date) a
GROUP BY player_id;