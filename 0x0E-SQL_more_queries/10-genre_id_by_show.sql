-- Script to list shows with at least one linked genre in hbtn_0d_tvshows

-- Use the specified database
USE hbtn_0d_tvshows;

-- Select the desired columns and join the necessary tables
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
