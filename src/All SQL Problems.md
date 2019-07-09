### 177. Nth Highest Salary.sql
```
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      # remeber here, the limit N-1 and offset 1
      select Distinct Salary  from employee order BY Salary DESC  limit M,1
  );
END
```
### 182. Duplicate Emails
```
select Email from Person group by Email having count(*)>1; 
```
### 183. Customers Who Never Order
```
//Write your MySQL query statement below
select  Customers.name as Customers from Customers
 where Customers.Id not in ( select distinct CustomerId from Orders);
 ```
