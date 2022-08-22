SELECT player_id, first_login
FROM
(SELECT player_id, event_date AS first_login
FROM Activity
GROUP BY player_id, event_date
ORDER BY event_date) a
GROUP BY player_id;

-- min
select player_id, min(event_date) as first_login
from activity 
group by player_id

-- rank + partition by
select player_id,event_date as first_login from (
select player_id, event_date,
rank() over(partition by player_id order by event_date) as rank_no
from Activity ) m
where rank_no = 1

-- dense_rank + partition by
-- doing inner calculations without calling outer functions
select 
player_id,
first_login
from (
    select 
    player_id, 
    event_date first_login,
    dense_rank() over(
        partition by player_id
        order by event_date
    ) poz
    from Activity
) src
where
poz = 1;

-- over + partition by
select distinct player_id, first_value(event_date) 
over(partition by player_id order by event_date) first_login 
from Activity;