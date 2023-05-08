import sqlite3

# Connect to the chinook.db database
conn = sqlite3.connect('chinook.db')

# Retrieve data for all tracks in the Classical playlist (PlaylistId = 12)
cursor = conn.execute('''SELECT t.Name, t.Composer, t.UnitPrice
                         FROM tracks t
                         INNER JOIN playlist_track pt ON t.TrackId = pt.TrackId
                         INNER JOIN playlists p ON pt.PlaylistId = p.PlaylistId
                         WHERE p.PlaylistId = 12''')

# Print the data for each track in the Classical playlist
for row in cursor:
    print("Title: " + row[0])
    print("Composer Name: " + str(row[1]))
    print("Unit Price: $" + str(row[2]))
    print("")

# Close the database connection
conn.close()
