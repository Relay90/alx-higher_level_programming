-- Import the table dump into the hbtn_0c_0 database
USE hbtn_0c_0;
SOURCE /path/to/your/table_dump.sql;

-- Display the max temperature of each state ordered by state name
SELECT state, MAX(temperature) AS max_temp
FROM temperature_data
GROUP BY state
ORDER BY state;
