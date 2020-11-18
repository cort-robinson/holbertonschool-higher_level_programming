-- Lists all genres from hbtn_0d_tvshows and displays number of shows linked to each
SELECT tv_genres.name AS genre,
    COUNT(*) AS number_of_shows
FROM tv_genres
    LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.genre_id IS NOT NULL
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC,
    tv_genres.id ASC;
