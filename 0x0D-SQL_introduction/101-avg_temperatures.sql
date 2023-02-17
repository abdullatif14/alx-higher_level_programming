-- Average Temperature by City ordered by temperature

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP by CITY ORDER BY avg_temp DESC;
