
-- this query will return the second highest salary from the employee table
select max(salary) as "SecondHighestSalary"
from employee 
where salary < (select max(salary) from employee)