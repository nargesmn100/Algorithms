# Write your MySQL query statement below
SELECT name, population, area FROM World # Note that the SELECT clause doesn't accept logical operators like AND directly, so we will use commas for multiple culumn selection
WHERE population >= 25000000 OR area >= 3000000

# Runtime: 418 ms, Beats 45.44%
