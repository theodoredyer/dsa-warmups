# Write your MySQL query statement below
select Department.name as "Department", e.name as "Employee", e.Salary from
(select departmentId, name, salary, dense_rank() over(partition by departmentId order by salary desc) as r from Employee) e
join Department on e.departmentId = Department.id
where r <= 3