from abc import ABC, abstractmethod
from entity import Artwork

class IVirtualArtGallery(ABC):

    # Artwork Management
    @abstractmethod
    def add_artwork(self, artwork): pass

    @abstractmethod
    def update_artwork(self, artwork): pass

    @abstractmethod
    def remove_artwork(self, artwork_id): pass

    @abstractmethod
    def get_artwork_by_id(self, artwork_id): pass

    @abstractmethod
    def search_artworks(self, keyword): pass

    # User Favorites
    @abstractmethod
    def add_artwork_to_favorite(self, user_id, artwork_id): pass

    @abstractmethod
    def remove_artwork_from_favorite(self, user_id, artwork_id): pass

    @abstractmethod
    def get_user_favorite_artworks(self, user_id): pass
