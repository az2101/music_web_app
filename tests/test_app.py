# Tests for your routes go here

"""
When I POST/albums  to albums
It is added to the list in GET/albums
"""
def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/music_library_web_app.sql")
    post_response = web_client.post('/albums', data={'title': 'Voyage', 'year': '2022', 'artist_id': '2'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == 'Album(1, Doolittle, 1989, 1), Album(2, Surfer Rosa, 1988, 1), Album(3, Waterloo, 1974, 2), Album(4, Super Trouper, 1980, 2), Album(5, Bossanova, 1990, 1), Album(6, Lover, 2019, 3), Album(7, Folklore, 2020, 3), Album(8, I Put a Spell on You, 1965, 4), Album(9, Baltimore, 1978, 4), Album(10, Here Comes the Sun, 1971, 4), Album(11, Fodder on My Wings, 1982, 4), Album(12, Ring Ring, 1973, 2), Album(13, Voyage, 2022, 2)'

"""
When I POST/artists to artists
It is added to the list in GET/artists
"""

def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/music_library_web_app.sql")
    post_response = web_client.post('/artists', data={'name': 'Wild nothing', 'genre': 'Indie'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == 'Artist(1, Pixies, Rock), Artist(2, ABBA, Pop), Artist(3, Taylor Swift, Pop), Artist(4, Nina Simone, Jazz), Artist(5, Wild nothing, Indie)'
