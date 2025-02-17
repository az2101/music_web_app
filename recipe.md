
# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)


# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a music lover,
So I can organise my records,
I want to keep a list of albums' titles.

As a music lover,
So I can organise my records,
I want to keep a list of albums' release years.

As a music lover,
So I can organise my records,
I want to keep a list of artists' names.

As a music lover,
So I can organise my records,
I want to know each album's artist.
```

```
Nouns:

album, title, release year, artist, name
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| album                 | id, title, release year
| artist                | name

1. Name of the first table (always plural): `albums` 

    Column names: `title`, `release_year`

2. Name of the second table (always plural): `artists` 

    Column names: `name`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: albums
id: SERIAL
title: text
release_year: int

Table: artists
id: SERIAL
name: text
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
2. Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)

You'll then be able to say that:

1. **[A] has many [B]**
2. And on the other side, **[B] belongs to [A]**
3. In that case, the foreign key is in the table [B]

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one artist have many albums? YES
2. Can one album have many artists? NO

-> Therefore,
-> An artist HAS MANY albums
-> An album BELONGS TO an artist

-> Therefore, the foreign key is on the albums table.
```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).*

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
);

-- Then the table with the foreign key second.
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
-- The foreign key name is always {other_table_singular}_id
  artist_id int,
  constraint fk_artist foreign key(artist_id)
    references artists(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```


# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
POST /albums
title: string
release_year: number (str)
artist_id: number (str)
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
Scenario 1

POST /albums
title=Voyage
release_year=2022
artist_id=2
Expecte response (200 OK)
(No content)

GET /albums
Expected response (200 OK)
Album(1, "Doolittle", 1989, 1),
Album(2, "Surfer Rosa", 1988, 1),
Album(3, "Waterloo", 1974, 2),
Album(4, "Super Trouper", 1980, 2),
Album(5, "Bossanova", 1990, 1),
Album(6, "Lover", 2019, 3),
Album(7, "Folklore", 2020, 3),
Album(8, "I Put a Spell on You", 1965, 4),
Album(9, "Baltimore", 1978, 4),
Album(10, "Here Comes the Sun", 1971, 4),
Album(11, "Fodder on My Wings", 1982, 4),
Album(12, "Ring Ring", 1973, 2)
Album(13, "Voyager", 2022, 2)

Scenario 2

POST /albums
Expected repsponse (400 Bad Request)

'You need to submit a title, release_year, and artist_id'

GET/ albums
Expected response (200 OK)
Album(1, "Doolittle", 1989, 1),
Album(2, "Surfer Rosa", 1988, 1),
Album(3, "Waterloo", 1974, 2),
Album(4, "Super Trouper", 1980, 2),
Album(5, "Bossanova", 1990, 1),
Album(6, "Lover", 2019, 3),
Album(7, "Folklore", 2020, 3),
Album(8, "I Put a Spell on You", 1965, 4),
Album(9, "Baltimore", 1978, 4),
Album(10, "Here Comes the Sun", 1971, 4),
Album(11, "Fodder on My Wings", 1982, 4),
Album(12, "Ring Ring", 1973, 2)

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```

