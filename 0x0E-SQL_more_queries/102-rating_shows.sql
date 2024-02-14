-- Script to list all shows from hbtn_0d_tvshows_rate by their rating

-- Use the specified database
USE hbtn_0d_tvshows_rate;

-- Select the desired columns and perform aggregation to calculate the rating sum
SELECT tv_shows.title, SUM(tv_ratings.rating) AS rating_sum
FROM tv_shows
LEFT JOIN tv_ratings ON tv_shows.id = tv_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
