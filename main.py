import sqlalchemy


engine = sqlalchemy.create_engine('postgresql://laitkilla:MSUMCFZZ342511m@localhost:5432/homework5_1')
engine

connection = engine.connect()

ispoltineli_janr = connection.execute('''SELECT name_of_the_genre, COUNT(name_of_the_artist) FROM genres g left join artists_genre ag on g.id = ag.genres_id
left join artists a on ag.artists_id = a.id
group by g.id;''').fetchall()
print(ispoltineli_janr)

album_track = connection.execute('''select album_name, COUNT(track_name) from albums a left join tracks t on a.id = t.album_id
where year_of_release between 2019 and 2020
group by a.id;''').fetchall()
print(album_track)

avg_tracks = connection.execute('''select album_name, AVG(duration) from albums a left join tracks t on a.id = t.album_id
group by a.id
order by avg(duration);''').fetchall()
print(avg_tracks)

albums_2020 = connection.execute('''select name_of_the_artist from artists 
where name_of_the_artist not in 
(select name_of_the_artist from artists a left join artists_album aa on a.id = aa.artists_id
left join albums al on aa.album_id = al.id 
where year_of_release = 2020);''').fetchall()
print(albums_2020)

artists_collection = connection.execute('''select name_colletion from collection
where name_colletion in 
(select name_colletion from collection c left join track_collection tc on c.id = tc.collection_id
left join tracks t on tc.track_id = t.id
left join albums a on t.id = a.id
left join artists_album aa on a.id = aa.album_id
left join artists ar on aa.artists_id = ar.id
where name_of_the_artist ilike '%%Eminem%%');''').fetchall()
print(artists_collection)

artists_genre = connection.execute('''select album_name from albums a
left join artists_album aa on a.id = aa.album_id
left join artists ar on aa.artists_id = ar.id
left join artists_genre ag on ar.id = ag.artists_id
left join genres g on ag.genres_id = g.id
group by a.album_name
having count(name_of_the_genre) >1;''').fetchall()
print(artists_genre)

track_not_in = connection.execute('''select track_name from tracks
where track_name not in
(select track_name from tracks t join track_collection tc on t.id = tc.track_id);''').fetchall()
print(track_not_in)

short_tracks = connection.execute('''select name_of_the_artist, track_name, duration from tracks t
left join albums al on t.id = al.id
left join artists_album aa on al.id = aa.album_id
left join artists a on aa.artists_id = a.id
group by a.name_of_the_artist, t.track_name, t.duration
having duration = (select min(duration) from tracks);''').fetchall()
print(short_tracks)

albums_tracks = connection.execute('''select album_name from albums a
left join tracks t on a.id = t.album_id
where album_id in
(select album_id from tracks group by album_id having count(id) = (select count(id) from tracks 
group by album_id
order by count
limit 1));''').fetchall()
print(albums_tracks)