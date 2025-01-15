# Write your MySQL query statement below
SELECT e1.unique_id, e2.name
FROM EmployeeUNI e1 RIGHT JOIN Employees e2
ON e1.id = e2.id OR e1.id = NULL OR e2.id = NULL;

# Runtime: 1313 ms, Beats 67.60%