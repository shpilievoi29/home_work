films=# select film.name_film, film.genre , year, duration, country, editor, actor from film left join editor on (film.name_film =editor.name_film) left join actor on (film.name_film = actor.film);
     name_film      |   genre    | year | duration |    country    |        editor        |        actor
--------------------+------------+------+----------+---------------+----------------------+----------------------
 Brilliant hand     | comedy     | 1968 |      100 | USSR          | Gayday               | Nataly Varley
 Brilliant hand     | comedy     | 1968 |      100 | USSR          | Gayday               | Alexander Demyanenko
 Brilliant hand     | comedy     | 1968 |      100 | USSR          | Gayday               | Eugeniy Morgunov
 Brilliant hand     | comedy     | 1968 |      100 | USSR          | Gayday               | Georgy Vitsyn
 Brilliant hand     | comedy     | 1968 |      100 | USSR          | Gayday               | Yuriy Nikulin
 Snatch             | criminal   | 2000 |      102 | Great Britain | Ritchie              | Benicio del Toro
 Snatch             | criminal   | 2000 |      102 | Great Britain | Ritchie              | Jason Statham
 Snatch             | criminal   | 2000 |      102 | Great Britain | Ritchie              | Brad Pitt
 Apocalypse Now     | drama      | 1979 |      202 | USA           | Francis Ford Coppola | Dennis Hopper
 Apocalypse Now     | drama      | 1979 |      202 | USA           | Francis Ford Coppola | Larry Fishburne
 Apocalypse Now     | drama      | 1979 |      202 | USA           | Francis Ford Coppola | Martin Sheen
 Apocalypse Now     | drama      | 1979 |      202 | USA           | Francis Ford Coppola | Marlon Brando
 The Revenant       | adventures | 2015 |      156 | USA           |                      | Domhnall Gleeson
 The Revenant       | adventures | 2015 |      156 | USA           |                      | Tom Hardy
 The Revenant       | adventures | 2015 |      156 | USA           |                      | Leonardo DiCaprio
 Titanic            | drama      | 1997 |      195 | USA           |                      | Kathy Bates
 Titanic            | drama      | 1997 |      195 | USA           |                      | Billy Zane
 Titanic            | drama      | 1997 |      195 | USA           |                      | Kate Winslet
 Titanic            | drama      | 1997 |      195 | USA           |                      | Leonardo DiCaprio
 Back to the Future | fantasy    | 1985 |      116 | USA           |  Robert Lee Zemeckis | Christopher Lloyd
 Back to the Future | fantasy    | 1985 |      116 | USA           |  Robert Lee Zemeckis | Bob Gale
 Back to the Future | fantasy    | 1985 |      116 | USA           |  Robert Lee Zemeckis | Michael J. Fox
 Treasure Island    | adventures | 1988 |      107 | USSR          | David Cherkassky     | Valery Chegliaev
 Treasure Island    | adventures | 1988 |      107 | USSR          | David Cherkassky     | Victor Andriyenko
(24 rows)
ilms=# select  name_film, editor, actor from editor left join actor on(actor.film = name_film);
     name_film      |        editor        |        actor
--------------------+----------------------+----------------------
 Brilliant hand     | Gayday               | Nataly Varley
 Brilliant hand     | Gayday               | Alexander Demyanenko
 Brilliant hand     | Gayday               | Eugeniy Morgunov
 Brilliant hand     | Gayday               | Georgy Vitsyn
 Brilliant hand     | Gayday               | Yuriy Nikulin
 Snatch             | Ritchie              | Benicio del Toro
 Snatch             | Ritchie              | Jason Statham
 Snatch             | Ritchie              | Brad Pitt
 Apocalypse Now     | Francis Ford Coppola | Dennis Hopper
 Apocalypse Now     | Francis Ford Coppola | Larry Fishburne
 Apocalypse Now     | Francis Ford Coppola | Martin Sheen
 Apocalypse Now     | Francis Ford Coppola | Marlon Brando
 Gonzalez           | The Revenant         |
 Cameron            | Titanic              |
 Back to the Future |  Robert Lee Zemeckis | Christopher Lloyd
 Back to the Future |  Robert Lee Zemeckis | Bob Gale
 Back to the Future |  Robert Lee Zemeckis | Michael J. Fox
 Treasure Island    | David Cherkassky     | Valery Chegliaev
 Treasure Island    | David Cherkassky     | Victor Andriyenko
(19 rows)
films=# select film.name_film, film.genre , year, duration, country, editor from film inner join editor on (film.name_film =editor.name_film);
     name_film      |   genre    | year | duration |    country    |        editor
--------------------+------------+------+----------+---------------+----------------------
 Brilliant hand     | comedy     | 1968 |      100 | USSR          | Gayday
 Snatch             | criminal   | 2000 |      102 | Great Britain | Ritchie
 Apocalypse Now     | drama      | 1979 |      202 | USA           | Francis Ford Coppola
 Back to the Future | fantasy    | 1985 |      116 | USA           |  Robert Lee Zemeckis
 Treasure Island    | adventures | 1988 |      107 | USSR          | David Cherkassky

(5 rows)
films=# select film.name_film, film.genre , year, duration, country, editor from film left join editor on (film.name_film =editor.name_film);
     name_film      |   genre    | year | duration |    country    |        editor
--------------------+------------+------+----------+---------------+----------------------
 Brilliant hand     | comedy     | 1968 |      100 | USSR          | Gayday
 Snatch             | criminal   | 2000 |      102 | Great Britain | Ritchie
 Apocalypse Now     | drama      | 1979 |      202 | USA           | Francis Ford Coppola
 The Revenant       | adventures | 2015 |      156 | USA           |
 Titanic            | drama      | 1997 |      195 | USA           |
 Back to the Future | fantasy    | 1985 |      116 | USA           |  Robert Lee Zemeckis
 Treasure Island    | adventures | 1988 |      107 | USSR          | David Cherkassky
(7 rows)