class Artwork:
    def __init__(self, artwork_id=None, title="", description="", creation_date="", medium="", image_url="", artist_id=None):
        self.artwork_id = artwork_id
        self.title = title
        self.description = description
        self.creation_date = creation_date
        self.medium = medium
        self.image_url = image_url
        self.artist_id = artist_id

    def __str__(self):
        return f"Artwork({self.artwork_id}, {self.title}, {self.medium})"



