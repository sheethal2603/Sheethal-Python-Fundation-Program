from dao.ivirtual_art_gallery import IVirtualArtGallery
from util import get_connection
from entity import Artwork
from exception import ArtworkNotFoundException, UserNotFoundException  

class VirtualArtGalleryImpl(IVirtualArtGallery):
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def add_artwork(self, artwork):
        try:
            query = '''
            INSERT INTO Artwork (Title, Description, CreationDate, Medium, ImageURL, ArtistID)
            VALUES (%s, %s, %s, %s, %s, %s)
            '''
            values = (artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url, artwork.artist_id)
            self.cursor.execute(query, values)
            self.conn.commit()
            return True
        except Exception as e:
            print("Error adding artwork:", e)
            return False

    def update_artwork(self, artwork):
        try:
            check_query = "SELECT * FROM Artwork WHERE ArtworkID = %s"
            self.cursor.execute(check_query, (artwork.artwork_id,))
            result = self.cursor.fetchone()
            if result is None:
                raise ArtworkNotFoundException(f"Artwork with ID {artwork.artwork_id} not found.")
            update_query = '''
            UPDATE Artwork
            SET Title = %s,
                Description = %s,
                CreationDate = %s,
                Medium = %s,
                ImageURL = %s,
                ArtistID = %s
            WHERE ArtworkID = %s
            '''
            values = (
                artwork.title,
                artwork.description,
                artwork.creation_date,
                artwork.medium,
                artwork.image_url,
                artwork.artist_id,
                artwork.artwork_id
            )
            self.cursor.execute(update_query, values)
            self.conn.commit()
            return True
        except ArtworkNotFoundException as e:
            print(e)
            return False
        except Exception as e:
            print("Error updating artwork:", e)
            return False

    def remove_artwork(self, artwork_id):
        try:
            self.cursor.execute("SELECT * FROM Artwork WHERE ArtworkID = %s", (artwork_id,))
            result = self.cursor.fetchone()
            if result is None:
                raise ArtworkNotFoundException(f"Artwork with ID {artwork_id} not found.")
            self.cursor.execute("DELETE FROM Artwork WHERE ArtworkID = %s", (artwork_id,))
            self.conn.commit()
            return True
        except ArtworkNotFoundException as e:
            print(e)
            return False
        except Exception as e:
            print("Error while deleting artwork:", e)
            return False

    def get_artwork_by_id(self, artwork_id):
        try:
            query = "SELECT * FROM Artwork WHERE ArtworkID = %s"
            self.cursor.execute(query, (artwork_id,))
            row = self.cursor.fetchone()
            if row is None:
                raise ArtworkNotFoundException(f"Artwork with ID {artwork_id} not found.")
            artwork = Artwork(*row)
            return artwork
        except ArtworkNotFoundException as e:
            print(e)
            return None
        except Exception as e:
            print("Error retrieving artwork:", e)
            return None

    def search_artworks(self, keyword):
        try:
            query = """
                SELECT * FROM Artwork 
                WHERE Title LIKE %s OR Description LIKE %s
            """
            wildcard = f"%{keyword}%"
            self.cursor.execute(query, (wildcard, wildcard))
            rows = self.cursor.fetchall()
            return [Artwork(*row) for row in rows]
        except Exception as e:
            print("Error searching artworks:", e)
            return []

    def add_artwork_to_favorite(self, user_id, artwork_id):
        try:
            self.cursor.execute("SELECT * FROM User WHERE UserID = %s", (user_id,))
            if not self.cursor.fetchone():
                raise UserNotFoundException(f"User ID {user_id} not found.")  
            self.cursor.execute("SELECT * FROM Artwork WHERE ArtworkID = %s", (artwork_id,))
            if not self.cursor.fetchone():
                raise ArtworkNotFoundException(f"Artwork ID {artwork_id} not found.")

            query = "INSERT INTO User_Favorite_Artwork (UserID, ArtworkID) VALUES (%s, %s)"
            self.cursor.execute(query, (user_id, artwork_id))
            self.conn.commit()
            return True
        except UserNotFoundException as e:
            print(e)
            return False
        except ArtworkNotFoundException as e:
            print(e)
            return False
        except Exception as e:
            print("Error adding to favorites:", e)
            return False

    def remove_artwork_from_favorite(self, user_id, artwork_id):
        try:
            query_check = """
                SELECT * FROM User_Favorite_Artwork
                WHERE UserID = %s AND ArtworkID = %s
            """
            self.cursor.execute(query_check, (user_id, artwork_id))
            if not self.cursor.fetchone():
                print("This artwork is not in the user's favorites.")
                return False

            query_delete = """
                DELETE FROM User_Favorite_Artwork
                WHERE UserID = %s AND ArtworkID = %s
            """
            self.cursor.execute(query_delete, (user_id, artwork_id))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error removing from favorites:", e)
            return False

    def get_user_favorite_artworks(self, user_id):
        try:
            query = """
            SELECT a.ArtworkID, a.Title, a.Description, a.CreationDate, 
                   a.Medium, a.ImageURL, a.ArtistID
            FROM Artwork a
            JOIN User_Favorite_Artwork ufa ON a.ArtworkID = ufa.ArtworkID
            WHERE ufa.UserID = %s
            """
            self.cursor.execute(query, (user_id,))
            rows = self.cursor.fetchall()
            return [Artwork(*row) for row in rows]
        except Exception as e:
            print("Error fetching user favorite artworks:", e)
            return []

    def add_gallery(self, gallery):
        try:
            query = """
                INSERT INTO Gallery (Name, Description, Location, CuratorID, OpeningHours)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (
                gallery.name,
                gallery.description,
                gallery.location,
                gallery.curator_id,
                gallery.opening_hours
            ))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error adding gallery:", e)
            return False

    def update_gallery(self, gallery):
        try:
            query = """
                UPDATE Gallery
                SET Name = %s,
                    Description = %s,
                    Location = %s,
                    CuratorID = %s,
                    OpeningHours = %s
                WHERE GalleryID = %s
            """
            self.cursor.execute(query, (
                gallery.name,
                gallery.description,
                gallery.location,
                gallery.curator_id,
                gallery.opening_hours,
                gallery.gallery_id
            ))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error updating gallery:", e)
            return False

    def remove_gallery(self, gallery_id):
        try:
            query = "DELETE FROM Gallery WHERE GalleryID = %s"
            self.cursor.execute(query, (gallery_id,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print("Error removing gallery:", e)
            return False

    def search_galleries(self, keyword):
        try:
            cursor = self.conn.cursor()
            query = """
                SELECT * FROM Gallery 
                WHERE Name LIKE %s OR Description LIKE %s OR Location LIKE %s
            """
            keyword_pattern = f"%{keyword}%"
            cursor.execute(query, (keyword_pattern, keyword_pattern, keyword_pattern))
            rows = cursor.fetchall()
            from entity.gallery import Gallery
            return [Gallery(*row) for row in rows]
        except Exception as e:
            print("Error in search_galleries:", e)
            return []
