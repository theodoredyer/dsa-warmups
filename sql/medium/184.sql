# Write your MySQL query statement below

select Department.name as Department, Employee.name as Employee, salary as Salary
from Employee join Department on Employee.departmentId = Department.id
where (departmentId, salary) in
(select departmentId, MAX(Salary) from Employee
group by departmentId)