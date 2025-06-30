import unittest
from datetime import datetime
from entity.artwork import Artwork
from entity.gallery import Gallery
from dao.virtual_art_gallery_impl import VirtualArtGalleryImpl

class TestVirtualArtGallery(unittest.TestCase):

    def setUp(self):
        self.gallery = VirtualArtGalleryImpl()

    #  1. ARTWORK MANAGEMENT 

    def test_add_artwork(self):
        art = Artwork(
            artwork_id=None,
            title="Test Art Upload",
            description="Uploaded for testing",
            creation_date=datetime(2022, 5, 10),
            medium="Oil on canvas",
            image_url="test_art.jpg",
            artist_id=1  
        )
        result = self.gallery.add_artwork(art)
        self.assertTrue(result)

    def test_update_artwork(self):
        art = Artwork(
            artwork_id=4, 
            title="Updated Art",
            description="Modified description",
            creation_date=datetime(2022, 1, 1),
            medium="Digital",
            image_url="updated.jpg",
            artist_id=1
        )
        result = self.gallery.update_artwork(art)
        self.assertTrue(result)

    def test_remove_artwork(self):
        # 
        temp_art = Artwork(
            artwork_id=None,
            title="Temp Art",
            description="To be deleted",
            creation_date=datetime(2023, 1, 1),
            medium="Sketch",
            image_url="temp.jpg",
            artist_id=1
        )
        self.gallery.add_artwork(temp_art)
        results = self.gallery.search_artworks("Temp Art")
        if results:
            last_id = results[-1].artwork_id
            result = self.gallery.remove_artwork(last_id)
            self.assertTrue(result)
        else:
            self.fail("Temp artwork not added.")

    def test_search_artworks(self):
        results = self.gallery.search_artworks("Mona")
        self.assertIsInstance(results, list)

    # 2. GALLERY MANAGEMENT

    def test_add_gallery(self):
        gal = Gallery(
            gallery_id=None,
            name="Unit Test Gallery",
            description="Gallery created for testing",
            location="Testville",
            curator_id=1,
            opening_hours="9:00 AM - 6:00 PM"
        )
        result = self.gallery.add_gallery(gal)
        self.assertTrue(result)

    def test_update_gallery(self):
        gal = Gallery(
            gallery_id=1, 
            name="Updated Gallery Name",
            description="Updated description",
            location="Updated Location",
            curator_id=1,
            opening_hours="10:00 AM - 7:00 PM"
        )
        result = self.gallery.update_gallery(gal)
        self.assertTrue(result)

    def test_remove_gallery(self):
        gal = Gallery(
            gallery_id=None,
            name="Temp Delete Gallery",
            description="Will be deleted",
            location="Temporary City",
            curator_id=1,
            opening_hours="8:00 AM - 4:00 PM"
        )
        self.gallery.add_gallery(gal)
        found = self.gallery.search_galleries("Temp Delete Gallery")
        if found:
            gallery_id = found[-1].gallery_id
            result = self.gallery.remove_gallery(gallery_id)
            self.assertTrue(result)
        else:
            self.fail("Temp gallery not added.")

    def test_search_galleries(self):
        results = self.gallery.search_galleries("Renaissance")
        self.assertIsInstance(results, list)


if __name__ == "__main__":
    unittest.main()
