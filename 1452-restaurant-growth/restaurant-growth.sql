# Write your MySQL query statement below

-- 1. 先把每天的消费额汇总成一行 (去掉 customer_id, name)
WITH daily AS (
  SELECT visited_on, SUM(amount) AS day_amt
  FROM Customer
  GROUP BY visited_on
),

win AS (
  SELECT
    visited_on,

    -- 2. SUM 的窗口语法改正确：ROWS 必须写在 OVER(...) 里面
    SUM(day_amt) OVER (
      ORDER BY visited_on
      ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS amt_7,

    -- 3. AVG 同理，在窗口里写 ROWS
    AVG(day_amt) OVER (
      ORDER BY visited_on
      ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS avg_7,

    -- 4. 增加一个 COUNT(*)，统计窗口内天数，用来判断是否满 7 天
    COUNT(*) OVER (
      ORDER BY visited_on
      ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS cnt_7
  FROM daily
)

SELECT
  visited_on,
  amt_7 AS amount,
  ROUND(avg_7, 2) AS average_amount
FROM win
-- 5. 只保留窗口天数 = 7 的行，避免前 6 天窗口不完整
WHERE cnt_7 = 7
ORDER BY visited_on;


