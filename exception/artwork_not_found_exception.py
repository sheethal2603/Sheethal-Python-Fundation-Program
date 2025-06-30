class ArtworkNotFoundException(Exception):
    def __init__(self, message="Artwork not found in the database."):
        super().__init__(message)
