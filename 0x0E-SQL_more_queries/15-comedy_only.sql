-- Lists all Comedy shows in the database hbtn_0d_tvshows
-- Displays the number of shows linked to each

-- Select the desired column and join the necessary tables
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;
