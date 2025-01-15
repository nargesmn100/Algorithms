# Write your MySQL query statement below
SELECT name from Customer
WHERE referee_id != 2 or referee_id IS NULL; 
# Not referred by 2 (referred by a number other than 2) OR have a null referree.
# Note that we need to check for NULL values explicitly. 

# Runtime: 733 ms, Beats 42.39%
