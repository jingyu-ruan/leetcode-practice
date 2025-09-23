-- Find Stores with Inventory Imbalance
WITH store_sizes AS (
    SELECT
        store_id,
        COUNT(DISTINCT product_name) AS distinct_products
    FROM inventory
    GROUP BY store_id
),
max_one AS (
    SELECT
        store_id,
        product_name AS most_exp_product,
        quantity     AS max_qty,
        ROW_NUMBER() OVER (
            PARTITION BY store_id
            ORDER BY price DESC, product_name ASC
        ) AS rn
    FROM inventory
),
min_one AS (
    SELECT
        store_id,
        product_name AS cheapest_product,
        quantity     AS min_qty,
        ROW_NUMBER() OVER (
            PARTITION BY store_id
            ORDER BY price ASC, product_name ASC
        ) AS rn
    FROM inventory
),
picked AS (
    SELECT
        mx.store_id,
        mx.most_exp_product,
        mx.max_qty,
        mn.cheapest_product,
        mn.min_qty
    FROM max_one mx
    JOIN min_one mn
      ON mx.store_id = mn.store_id
    WHERE mx.rn = 1
      AND mn.rn = 1
),
imbalanced AS (
    SELECT
        p.store_id,
        p.most_exp_product,
        p.cheapest_product,
        -- 题目要求四舍五入到 2 位
        ROUND(p.min_qty / p.max_qty, 2) AS imbalance_ratio
    FROM picked p
    -- 只保留失衡店（最贵数量 < 最便宜数量）
    WHERE p.max_qty < p.min_qty
)
SELECT
    s.store_id,
    s.store_name,
    s.location,
    i.most_exp_product,
    i.cheapest_product,
    i.imbalance_ratio
FROM imbalanced i
JOIN store_sizes sz
  ON i.store_id = sz.store_id
JOIN stores s
  ON s.store_id = i.store_id
-- 至少 3 种不同产品
WHERE sz.distinct_products >= 3
ORDER BY i.imbalance_ratio DESC, s.store_name ASC;
