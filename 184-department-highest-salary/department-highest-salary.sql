# Write your MySQL query statement below
select d.name as Department, 
       e2.name as Employee, 
       e2.salary as Salary 
from(
    select e.*, 
    dense_rank() over(PARTITION by departmentid order by salary desc) as rk
    from employee e
) e2
left join department d
on e2.departmentid = d.id
where e2.rk = 1;
 