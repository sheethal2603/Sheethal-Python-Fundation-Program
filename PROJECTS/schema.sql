CREATE DATABASE virtual_art_gallery;
USE virtual_art_gallery;
CREATE TABLE Artwork (
    ArtworkID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Description TEXT,
    CreationDate DATE,
    Medium VARCHAR(100),
    ImageURL VARCHAR(255),
    ArtistID INT
);

INSERT INTO Artwork (Title, Description, CreationDate, Medium, ImageURL, ArtistID)
VALUES
('Mona Lisa', 'A portrait by Leonardo da Vinci.', '1503-06-01', 'Oil on wood', 'monalisa.jpg', 1),
('Starry Night', 'A swirling night sky by Van Gogh.', '1889-06-18', 'Oil on canvas', 'starrynight.jpg', 2),
('The Two Fridas', 'A double self-portrait by Frida Kahlo.', '1939-01-01', 'Oil on canvas', 'twofridas.jpg', 3);

SELECT * from artwork;

CREATE TABLE User (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(100) NOT NULL UNIQUE,
    Password VARCHAR(100) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    DateOfBirth DATE,
    ProfilePicture VARCHAR(255)
);

INSERT INTO User (Username, Password, Email, FirstName, LastName, DateOfBirth, ProfilePicture)
VALUES
('joseph_manik', '123', 'jj@example.com', 'Joseph', 'Manik', '1990-05-12', 'john.jpg'),
('emma.art', 'emma321', 'emma@gmail.com', 'Emma', 'Watson', '1992-10-05', 'emma.jpg'),
('aman_malik99', 'iloveart', 'art@example.com', 'Aman', 'Malik', '1988-12-20', 'aman.jpg');

SELECT * from User;

CREATE TABLE Artist (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Biography TEXT,
    BirthDate DATE,
    Nationality VARCHAR(100),
    Website VARCHAR(255),
    ContactInfo VARCHAR(255)
);
INSERT INTO Artist (Name, Biography, BirthDate, Nationality, Website) VALUES
('Leonardo da Vinci',
'Leonardo da Vinci was a polymath of the Italian Renaissance known for iconic works like the Mona Lisa and The Last Supper.',
'1452-04-15',
'Italian',
'https://en.wikipedia.org/wiki/Leonardo_da_Vinci'),

('Frida Kahlo',
'Frida Kahlo was a Mexican painter known for her deeply personal and symbolic self-portraits.',
'1907-07-06',
'Mexican',
'https://en.wikipedia.org/wiki/Frida_Kahlo'),

('Vincent van Gogh',
'Vincent van Gogh was a Dutch post-impressionist painter known for Starry Night and his expressive use of color and brushwork.',
'1853-03-30',
'Dutch',
'https://en.wikipedia.org/wiki/Vincent_van_Gogh');

SELECT * from Artist;

CREATE TABLE Gallery (
    GalleryID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    Location VARCHAR(255),
    CuratorID INT,
    OpeningHours VARCHAR(100),
    FOREIGN KEY (CuratorID) REFERENCES Artist(ArtistID)
);

INSERT INTO Gallery (Name, Description, Location, CuratorID, OpeningHours)
VALUES
('Renaissance Wonders', 'Gallery showcasing Renaissance era art.', 'Florence, Italy', 1, '9:00 AM - 5:00 PM'),
('Post-Impressionism Vault', 'Gallery of late 19th century art.', 'Amsterdam, Netherlands', 2, '10:00 AM - 6:00 PM'),
('Mexican Magic Realism', 'Gallery for modern Latin American art.', 'Mexico City, Mexico', 3, '11:00 AM - 7:00 PM');

SELECT * from Gallery;

CREATE TABLE User_Favorite_Artwork (
    UserID INT,
    ArtworkID INT,
    PRIMARY KEY (UserID, ArtworkID),
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID)
);

INSERT INTO User_Favorite_Artwork (UserID, ArtworkID)
VALUES
(7, 4),  -- Joseph Manik loves Mona Lisa
(8, 5),  -- Emma loves Starry Night
(9, 6),  -- Aman Malik loves The Two Fridas
(8, 6);  -- Emma also loves The Two Fridas

SELECT * from User_Favorite_Artwork;

CREATE TABLE Artwork_Gallery (
    ArtworkID INT,
    GalleryID INT,
    PRIMARY KEY (ArtworkID, GalleryID),
    FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID),
    FOREIGN KEY (GalleryID) REFERENCES Gallery(GalleryID)
);

INSERT INTO Artwork_Gallery (ArtworkID, GalleryID)
VALUES
(4, 1),  -- Mona Lisa → Renaissance Wonders
(5, 2),  -- Starry Night → Post-Impressionism Vault
(6, 3);  -- The Two Fridas → Mexican Magic Realism

SELECT * from Artwork_Gallery;


