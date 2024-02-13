-- Import the table dump into the hbtn_0c_0 database
USE hbtn_0c_0;
SOURCE /path/to/your/table_dump.sql;

-- Display the top 3 cities' temperatures during July and August ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM temperature_data
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
