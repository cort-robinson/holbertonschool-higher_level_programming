-- Uses the hbtn_0d_tvshows database to lists all genres not related to Dexter
SELECT g.name
FROM tv_genres AS g
WHERE g.name NOT IN (
        SELECT g.name
        FROM tv_genres AS g
            JOIN tv_show_genres AS sg ON g.id = sg.genre_id
            JOIN tv_shows AS s ON sg.show_id = s.id
        WHERE s.title = "Dexter"
    )
ORDER BY g.name;
