-- Import the table dump into the hbtn_0c_0 database
USE hbtn_0c_0;
SOURCE /path/to/your/table_dump.sql;

-- Display the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM temperature_data
GROUP BY city
ORDER BY avg_temp DESC;
