-- Script to create the database hbtn_0d_usa and the table states

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the specified database
USE hbtn_0d_usa;

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Insert data into the states table
INSERT INTO states (name) VALUES
    ('California'),
    ('Arizona'),
    ('Nevada'),
    ('Illinois'),
    ('New York'),
    ('Louisiana')
    ON DUPLICATE KEY UPDATE id = id + 1;
