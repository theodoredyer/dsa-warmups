# Write your MySQL query statement below

select max(salary) AS SecondHighestSalary
from Employee
where salary not in (select max(salary) from Employee)