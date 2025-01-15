# Write your MySQL query statement below
SELECT DISTINCT author_id as id FROM Views # Distinct goes with select 
WHERE viewer_id = author_id
ORDER BY author_id ASC 

# Runtime: 403 ms, Beats 90.21%
