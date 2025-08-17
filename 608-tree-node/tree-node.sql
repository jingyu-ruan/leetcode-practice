SELECT t.id,
CASE
  WHEN t.p_id IS NULL THEN 'Root'         -- 没有父节点
  WHEN COUNT(c.id) > 0 THEN 'Inner'       -- 有子节点
  ELSE 'Leaf'                             -- 没有子节点
END AS type
FROM Tree t
LEFT JOIN Tree c ON c.p_id = t.id   -- 把每个节点和它的“孩子”连起来
GROUP BY t.id, t.p_id;
