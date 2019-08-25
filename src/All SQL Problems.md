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
### 178. Rank Scores
```
Select Score,
(SELECT count(DISTINCT score)+1 from Scores where Scores.score>s.score) Rank
From Scores s
ORDER BY score
DESC;
```
### 180. Consecutive Numbers
```
# Write your MySQL query statement below
SELECT DISTINCT L1.Num as ConsecutiveNums
FROM Logs L1 
Left JOIN Logs L2 On L1.Id=L2.Id-1
Left JOIN Logs L3 On L1.Id=L3.Id-2
WHERE L1.Num = L2.Num AND L1.Num = L3.Num ;
```

### 181. Employees Earning More Than Their Managers
```
SELECT e1.Name as Employee 
from Employee e1 
left join Employee e2 On e1.ManagerId=e2.Id
where e1.Salary>e2.Salary;
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
 
 ### 184. Department Highest Salary
 ```
SELECT D.name as Department, E.Name as Employee,Salary
FROM Employee E 
INNER JOIN Department D on E.DepartmentId=D.Id
WHERE (E.DepartmentID,Salary) in (Select DepartmentId, max(Salary) from Employee group by DepartmentId);
```
### 185. Department Top Three Salaries
```
SELECT D.Name Department,E.name Employee, E.Salary From Department D, Employee E
Where E.DepartmentId=D.Id
and (SELECT count(DISTINCT Salary) From Employee Where DepartmentId=D.id and SALARY>E.Salary)<3 ;
```
### 197. Rising Temperature
 ```
 Select W1.Id 
from Weather W1 
inner join Weather W2 ON TO_DAYS(W1.RecordDate)=TO_DAYS(W2.RecordDate)+1
where W1.Temperature>W2.Temperature;
```

### 595. Big Countries
```
# Write your MySQL query statement below
Select name,population, area from World where area>3000000 or population >25000000;
```
### 596. Classes More Than 5 Students
```
# Write your MySQL query statement below
SELECT class 
FROM courses 
Group By class
Having count(DISTINCT student)>=5;
```

### 601. Human Traffic of Stadium
```
SELECT distinct S1.*
from stadium S1,stadium S2,stadium S3 
Where ((s1.id+1=s2.id and s1.id+2=s3.id) 
or (s1.id-1=s2.id and s1.id+1=s3.id)
or (s1.id-2=s2.id and s1.id-1=s3.id))
and S1.People>=100 and S2.People >100 and s3.People>=100
order by s1.id;
```


### 620. Not Boring Movies
```
# Write your MySQL query statement below
Select id,movie,description,rating from cinema where id%2<>0 and description<> "boring" ORDER BY rating DESC;
```
