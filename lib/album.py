class Album():
    def __init__(self, id, title, year, artist_id):
        self.id = id
        self.title = title
        self.year = year
        self.artist_id = artist_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.year}, {self.artist_id})"
    
    