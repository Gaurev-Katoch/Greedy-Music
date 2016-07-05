# Greedy-Music
Description:
A Web App to list, save, view and edit Tracks and Genres built using the Django Web Framework

Requirements:
Django Version - 1.9.4

Some Tips to the User:

1. Track or Genre names cannot be left blank. The app will not save a record with blank names.
2. Genres for Tracks are a many to many relation, hence you can only add genres that already exist to a track.
3. In case you want to add a genre that does not exist, add the genre through the add genre page then add it to a track.
4. Track names are not unique but genre names are.

Search bar instructions: 

1. You can search tracks by their Track Name, Artist or Genres.
2. You can search for multiple genres at once by entering the genre names separated by a comma ','.
