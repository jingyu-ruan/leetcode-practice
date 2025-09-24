# Write your MySQL query statement below
WITH open_close AS (
    SELECT *
    FROM app_events 
    WHERE event_type ='app_open' OR event_type ='app_close'
), open_close_2 AS (
    SELECT session_id, user_id, event_timestamp AS end_time, 
           LAG(event_timestamp, 1) OVER (PARTITION BY user_id ORDER BY event_timestamp) AS start_time
    FROM open_close

), duration AS (
    SELECT session_id, user_id, TIMESTAMPDIFF(MINUTE, STR_TO_DATE(start_time, '%Y-%m-%d %H:%i:%s'),  STR_TO_DATE(end_time, '%Y-%m-%d %H:%i:%s')) AS session_duration_minutes
    FROM open_close_2
), duration2 AS (
    SELECT session_id, user_id, session_duration_minutes
    FROM duration
    WHERE session_duration_minutes >30
), scroll AS (
    SELECT user_id, COUNT(*) AS scroll_count 
    FROM app_events 
    WHERE event_type ='scroll'
    GROUP BY user_id
    HAVING COUNT(*) >= 5
), click_scroll AS (
    SELECT user_id, 
           SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS click, 
           SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END) AS scroll
    FROM app_events 
    GROUP BY user_id 
), ratio AS (
    SELECT user_id
    FROM click_scroll
    WHERE click/scroll < 0.2
)


SELECT session_id, duration2.user_id, session_duration_minutes, scroll_count 
FROM duration2
JOIN scroll ON scroll.user_id = duration2.user_id 
JOIN click_scroll ON click_scroll.user_id = duration2.user_id 
JOIN ratio ON ratio.user_id = duration2.user_id 
WHERE duration2.user_id NOT IN (SELECT DISTINCT user_id FROM app_events WHERE event_type = 'purchase') 
ORDER BY scroll_count DESC, session_id 
;