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
