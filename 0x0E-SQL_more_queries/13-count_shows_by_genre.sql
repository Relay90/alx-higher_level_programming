-- Script to list all genres and the number of shows linked to each in hbtn_0d_tvshows

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;

-- Use the specified database
USE hbtn_0d_tvshows;

-- Select the desired columns and aggregate the count of shows for each genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
