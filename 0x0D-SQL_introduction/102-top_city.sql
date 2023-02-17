-- Import database 
-- display the top 3 of cities temperature

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP by CITY ORDER BY avg_temp DESC;
