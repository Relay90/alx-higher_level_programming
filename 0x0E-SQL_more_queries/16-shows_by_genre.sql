-- Script to list all shows and linked genres in hbtn_0d_tvshows

-- Use the specified database
USE hbtn_0d_tvshows;

-- Select the desired columns and join the necessary tables
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
