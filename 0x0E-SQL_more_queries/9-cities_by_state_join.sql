-- Script to list all cities with corresponding states in hbtn_0d_usa

-- Use the specified database
USE hbtn_0d_usa;

-- Select the desired columns and join the cities and states tables
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
