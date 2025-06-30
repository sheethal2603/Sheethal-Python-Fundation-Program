VIRTUAL ART GALLERY - BACKEND SYSTEM

In today's digital-first world, virtual platforms have become essential — even for art. This project is a backend system for Virtual Art Gallery where artists can showcase their works and users can explore and save their favorite pieces. It captures essential business logic like artwork lifecycle management, user preferences, and database operations. This system is built in Python with MySQL integration, emphasizing clean architecture, exception handling, and unit testing.

• Business Logic :

In the modern world, art is no longer limited to physical galleries. With the rise of digital platforms, virtual art spaces have become a powerful way to make artwork accessible to a global audience. 

1. Artists can contribute their creations to the gallery.
2. Users can browse the artwork collection and save pieces to their personal favorites.
3. Administrators can manage artworks — adding new pieces, editing existing ones, or removing outdated entries.
4. The system also supports advanced search features, allowing users to quickly discover art based on titles or descriptions.

• Features :

The Virtual Art Gallery system supports the following core features
-> Add Artwork : 
Insert new artwork into the gallery with full details like title, description, medium, and artist.
-> Update Artwork :
Modify existing artwork records to keep information accurate and up to date.
-> Remove Artwork : 
Delete artwork entries that are no longer needed or relevant.
-> View Artwork by ID :
Retrieve complete details of a specific artwork using its unique ID.
-> Search Artworks :
Search artworks by title or description using keyword-based filtering.
-> Add to Favorites :
Allow users to mark specific artworks as favorites for quick access.
-> Remove from Favorites :
Let users remove artworks from their favorites list.
-> View Favorite Artworks :
Display all artworks marked as favorite by a particular user.

These features simulate real-world gallery operations and are backed by a MySQL database using Python, object-oriented design, and clean exception handling.

• Technologies Used :

-> Python 3
-> MySQL Database
-> MySQL Connector (mysql-connector-python)
-> Object-Oriented Programming (OOPS)
-> SQL Queries
-> Exception Handling
-> unittest for Unit Testing
-> Git & GitHub (for version control)

• Database Schema :

1. Artwork
Stores individual artworks uploaded to the virtual gallery.
Contains attributes like title, description, medium, creation date, image reference, and a foreign key linking to the artist who created it.

2. Artist
Represents artists who have contributed to the gallery.
Holds biographical and contact information.

3. User
Represents platform users who explore the gallery and can save favorite artworks.
Includes basic user information and authentication details.

4. Gallery
Represents virtual gallery rooms or collections where artworks are exhibited.
Each gallery is curated by an artist.

5. User_Favorite_Artwork (Junction Table)
Handles the many-to-many relationship between users and artworks.
Allows users to mark multiple artworks as favorites and vice versa.

6. Artwork_Gallery (Junction Table)

Maps artworks to the galleries they are displayed in.
Supports many-to-many relationships — one artwork can be featured in multiple galleries, and each gallery can contain many artworks.

• File Structure 

VirtualArtGallery
├── 📁 .venv/
├── 📁 dao/
│ ├── init.py
│ ├── ivirtual_art_gallery.py - Interface (ABC)
│ └── virtual_art_gallery_impl.py -  actual implementation, Perfect separation of interface and logic.

├── 📁 entity/
│ ├── init.py
│ ├── artist.py
│ ├── artwork.py
│ ├── gallery.py
│ └── user.py - Define classes/models that match the database tables.

├── 📁 exception/
│ ├── init.py
│ ├── artwork_not_found_exception.py
│ └── user_not_found_exception.py

├── 📁 main/
│ ├── init.py
│ ├── main_module.py -  Where app runs
│ └── test_db.py - DB connection test

├── 📁 resources/
│ └── db.properties -  Database connection settings

├── 📁 tests/
│ └── init.py
  └── test_virtual_art_gallery.py - This is where your unit tests would go

├── 📁 util
│ ├── init.py
│ ├── db_conn_util.py -  Handles connection logic
│ └── db_property_util.py - Reads db.properties

└── schema.sql - Stores SQL table creation scripts

• Future Scope

The Virtual Art Gallery can grow with many new features to improve user experience and support business goals:

1. Artist Sign-Up: Artists will be able to register and upload their own artworks directly to the platform.
2. Show Images: Instead of just showing image links, the system will display real pictures of the artwork.
3. Buy & Sell Art: Users could buy artworks through secure payments or even bid in online auctions.
4. Better Search Options: Add filters like artist name, medium, or date to help users find exactly what they want.
5. Online Exhibitions: Organize themed digital exhibitions, just like in real galleries.
6. Artwork Reviews: Let users rate and comment on artworks to share their opinions and feedback.
7. Admin Dashboard: A dashboard for admins to track user activity and see which artworks are most popular.
8. Mobile App: Create a mobile version of the platform so users can browse art on the go.
9. Multiple Languages: Add language options to support people from different regions.
10. User Roles: Add separate logins and permissions for admins, artists, and regular users to keep things secure.
