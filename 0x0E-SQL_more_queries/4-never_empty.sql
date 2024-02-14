-- Script to create the table id_not_null in the specified database
-- Create the table if it doesn't exist
-- Use the specified database
-- id_not_null description:
      -- id INT - default value 1
      -- name VARCHAR(256)

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
