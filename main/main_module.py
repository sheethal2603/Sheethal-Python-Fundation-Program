import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

from dao.virtual_art_gallery_impl import VirtualArtGalleryImpl
from entity import Artwork
from exception.artwork_not_found_exception import ArtworkNotFoundException
from exception.user_not_found_exception import UserNotFoundException


def main():
    service = VirtualArtGalleryImpl()

    while True:
        print("\n Virtual Art Gallery Menu ")
        print("1. Add Artwork")
        print("2. Update Artwork")
        print("3. Remove Artwork")
        print("4. Get Artwork by ID")
        print("5. Search Artworks by Keyword")
        print("6. Add Artwork to Favorites")
        print("7. Remove Artwork from Favorites")
        print("8. View Favorite Artworks")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            desc = input("Enter description: ")
            date = input("Enter creation date (YYYY-MM-DD): ")
            medium = input("Enter medium: ")
            image_url = input("Enter image URL: ")
            artist_id = input("Enter artist ID: ")

            artwork = Artwork(
                artwork_id=None,  
                title=title,
                description=desc,
                creation_date=date,
                medium=medium,
                image_url=image_url,
                artist_id=int(artist_id)
            )

            result = service.add_artwork(artwork)
            if result:
                print(" Artwork added successfully!")
            else:
                print(" Failed to add artwork.")

        elif choice == "2":
            try:
                art_id = int(input("Enter Artwork ID to update: "))
                title = input("Enter new title: ")
                desc = input("Enter new description: ")
                date = input("Enter new creation date (YYYY-MM-DD): ")
                medium = input("Enter new medium: ")
                image_url = input("Enter new image URL: ")
                artist_id = int(input("Enter new artist ID: "))

                updated_art = Artwork(
                    artwork_id=art_id,
                    title=title,
                    description=desc,
                    creation_date=date,
                    medium=medium,
                    image_url=image_url,
                    artist_id=artist_id
                )

                result = service.update_artwork(updated_art)
                if result:
                    print(" Artwork updated successfully!")
                else:
                    print(" Failed to update artwork.")
            except Exception as e:
                print(" Error updating artwork:", e)

        elif choice == '3':
            try:
                artwork_id = int(input("Enter the Artwork ID to remove: "))
                success = service.remove_artwork(artwork_id)

                if success:
                    print(" Artwork removed successfully.")
                else:
                    print(" Failed to remove artwork.")
            except Exception as e:
                print(" Error:", e)

        elif choice == '4':
            try:
                artwork_id = int(input("Enter Artwork ID: "))
                artwork = service.get_artwork_by_id(artwork_id)
                if artwork:
                    print("\n Artwork Details:")
                    print(f"ID: {artwork.artwork_id}")
                    print(f"Title: {artwork.title}")
                    print(f"Description: {artwork.description}")
                    print(f"Created On: {artwork.creation_date}")
                    print(f"Medium: {artwork.medium}")
                    print(f"Image URL: {artwork.image_url}")
                    print(f"Artist ID: {artwork.artist_id}")
                else:
                    print(" Artwork not found.")
            except Exception as e:
                print(" Error:", e)

        elif choice == '5':
            try:
                keyword = input("Enter keyword to search: ")
                results = service.search_artworks(keyword)

                if results and len(results) > 0:
                    print(f"\n Found {len(results)} artwork(s):")
                    for art in results:
                        print("\n Artwork Details:")
                        print(f"ID: {art.artwork_id}")
                        print(f"Title: {art.title}")
                        print(f"Description: {art.description}")
                        print(f"Created On: {art.creation_date}")
                        print(f"Medium: {art.medium}")
                        print(f"Image: {art.image_url}")
                        print(f"Artist ID: {art.artist_id}")
                else:
                    print(" No artworks found for that keyword.")

            except Exception as e:
                print("Error:", e)

        elif choice == '6':
            try:
                user_id = int(input("Enter your User ID: "))
                artwork_id = int(input("Enter the Artwork ID to favorite: "))
                success = service.add_artwork_to_favorite(user_id, artwork_id)
                if success:
                    print("Artwork added to favorites!")
                else:
                    print(" Failed to add to favorites.")
            except Exception as e:
                print(" Error:", e)

        elif choice == '7':
            try:
                user_id = int(input("Enter your User ID: "))
                artwork_id = int(input("Enter Artwork ID to remove from favorites: "))
                success = service.remove_artwork_from_favorite(user_id, artwork_id)
                if success:
                    print(" Artwork removed from favorites.")
                else:
                    print(" Could not remove the artwork from favorites.")
            except Exception as e:
                print(" Error:", e)

        
        elif choice == '8':
            try:
                user_id = int(input("Enter your User ID: "))
                favorites = service.get_user_favorite_artworks(user_id)
                if favorites:
                    print(f"\n Favorite Artworks for User {user_id}:")
                    for art in favorites:
                        print(f"\n ID: {art.artwork_id}")
                        print(f"Title: {art.title}")
                        print(f"Description: {art.description}")
                        print(f"Created On: {art.creation_date}")
                        print(f"Medium: {art.medium}")
                        print(f"Image URL: {art.image_url}")
                        print(f"Artist ID: {art.artist_id}")
                else:
                    print(" No favorites found for this user.")
            except Exception as e:
                print(" Error:", e)


        elif choice == "9":
            print(" Goodbye")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()







