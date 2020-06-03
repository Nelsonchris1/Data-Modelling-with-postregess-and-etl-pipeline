# Drop Tables

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS table users"
song_table_drop = "DROP TABLE IF EXISTS table songs"
artist_table_drop = "DROP TABLE IF EXISTS table artists"
time_table_drop = "DROP TABLE IF EXISTS table time"


# Create Tables

songplay_table_create = "CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY, start_time timestamp NOT NULL, user_id text NOT NULL, level text, song_id text, artist_id text , session_id int , location text, user_agent text)"

user_table_create = "CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY, first_name text NOT NULL, last_name text NOT NULL,  gender text NOT NULL, level text NOT NULL)"

song_table_create = "CREATE TABLE IF NOT EXISTS songs (song_id text PRIMARY KEY, title text, artist_id text NOT NULL, year int, duration float)"

artist_table_create = "CREATE TABLE IF NOT EXISTS artists (artist_id text PRIMARY KEY, name text, location text, lattitude text, longitude text)"

time_table_create = "CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY, hour int, day int, week int, month int, year int, weekday text)"

# Insert Records

songplay_table_insert = "INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (songplay_id) DO NOTHING"

user_table_insert = "INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level"

song_table_insert = "INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) "

artist_table_insert = "INSERT INTO artists (artist_id, name, location, lattitude, longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING"

time_table_insert = "INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING"


# FIND SONGS
# Here we create a query that returns an artist name and the particular song
song_select = "SELECT songs.song_id, artists.artist_id FROM songs JOIN artists ON songs.artist_id = artists.artist_id WHERE songs.title = %s AND artists.name=%s AND songs.duration=%s"



# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]