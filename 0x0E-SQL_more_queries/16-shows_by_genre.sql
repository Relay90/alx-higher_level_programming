-- lists all shows and linked genres from the database hbtn_0d_tvshows
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display:
-- tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre
-- The database name will be passed as an argument of the mysql command

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;

-- Use the specified database
USE hbtn_0d_tvshows;

-- Select the desired columns and perform LEFT JOINs
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
