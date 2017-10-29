## 4. Querying a normalized database ##

import sqlite3
conn = sqlite3.connect("academy_awards.db")
cursor = conn.cursor()
query = "select ceremonies.year , nominations.movie from nominations inner join ceremonies on nominations.ceremony_id == ceremonies.id where nominee == \"Natalie Portman\""
cursor.execute(query)
portman_movies = cursor.fetchall()
print(portman_movies)


## 7. Join table ##

five_movies = conn.execute("select * from movies limit 5;").fetchall()
five_actors = conn.execute("select * from actors limit 5;").fetchall()
five_join_table = conn.execute("select * from movies_actors limit 5;").fetchall()

print(five_movies)
print(five_actors)
print(five_join_table)

## 9. Querying a many-to-many relation ##

query = '''select actors.actor , movies.movie from actors inner join movies_actors on movies_actors.actor_id == actors.id inner join movies on movies_actors.movie_id == movies.id where movies.movie == "The King's Speech"'''


kings_actors = conn.execute(query).fetchall()
print(kings_actors)

## 10. Practice: querying a many-to-many relation ##

q = '''
select movies.movie, actors.actor from movies
inner join movies_actors on movies.id == movies_actors.movie_id
inner join actors on actors.id == movies_actors.actor_id
where actors.actor == "Natalie Portman";
'''
portman_joins = conn.execute(q).fetchall()
print(portman_joins)