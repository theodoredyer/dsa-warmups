# Write your MySQL query statement below
with cte as (
select customer_number, count(order_number) as ordnum
from Orders
group by customer_number
)
select customer_number
from cte 
order by ordnum desc
limit 1