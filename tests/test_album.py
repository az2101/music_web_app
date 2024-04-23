
from lib.album import *
"""
Albums constructs with an id, title, release_year and artist_id
"""

def test_album_constructs_with_fields():
    album = Album(1, 'Test Title', 1995, 1)
    assert album.id == 1
    assert album.title == 'Test Title'
    assert album.year == 1995
    assert album.artist_id == 1

"""
We can format albums into a string
"""

def test_album_formats_to_string():
    album = Album(1, 'Test Title', 1995, 1)
    assert str(album) == "Album(1, Test Title, 1995, 1)"


"""
We can compare two identical albums
and have them be equal
"""

def test_albums_are_equal():
    album1 = Album(1, 'Test Title', 1995, 1)
    album2 = Album(1, 'Test Title', 1995, 1)
    assert album1 == album2
    