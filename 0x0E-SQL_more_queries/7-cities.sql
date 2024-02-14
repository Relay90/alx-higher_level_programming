-- Script to create the database hbtn_0d_usa and the table cities
-- Create the database if it doesn't exist
-- Insert data into the cities table
-- Use the specified database
-- Create the table if it doesn't exist

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
