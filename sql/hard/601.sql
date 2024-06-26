# Write your MySQL query statement below
select distinct s1.*
from Stadium s1 join Stadium s2 join Stadium s3
on (s1.id=s2.id-1 and s1.id=s3.id-2) or
(s1.id=s2.id+1 and s1.id=s3.id-1) or
(s1.id=s2.id+1 and s1.id=s3.id+2)
where s1.people >= 100 and s2.people >= 100 and s3.people >= 100
order by visit_date asc