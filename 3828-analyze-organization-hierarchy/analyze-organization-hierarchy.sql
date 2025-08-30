# Write your MySQL query statement below

WITH RECURSIVE
-- 1) Levels from the root (CEO(s))
lvl AS (
  SELECT employee_id, 1 AS level
  FROM Employees
  WHERE manager_id IS NULL
  UNION ALL
  SELECT e.employee_id, l.level + 1
  FROM Employees e
  JOIN lvl l ON e.manager_id = l.employee_id
),

-- 2) Full transitive closure (ancestor -> descendant), incl. self
paths AS (
  SELECT employee_id AS ancestor_id, employee_id AS descendant_id
  FROM Employees
  UNION ALL
  SELECT p.ancestor_id, e.employee_id
  FROM paths p
  JOIN Employees e ON e.manager_id = p.descendant_id
),

-- 3) Aggregate subtree metrics for each ancestor (manager)
agg AS (
  SELECT 
    p.ancestor_id AS employee_id,
    COUNT(*) - 1 AS team_size,        -- exclude self
    SUM(e.salary)   AS budget          -- includes self
  FROM paths p
  JOIN Employees e ON e.employee_id = p.descendant_id
  GROUP BY p.ancestor_id
)

SELECT 
  e.employee_id,
  e.employee_name,
  l.level,
  a.team_size,
  a.budget
FROM Employees e
JOIN lvl  l ON l.employee_id = e.employee_id
JOIN agg  a ON a.employee_id = e.employee_id
ORDER BY l.level ASC, a.budget DESC, e.employee_name ASC;


