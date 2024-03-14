-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- he tv_shows table contains only one record where title = Dexter (but the id can be different)


SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
