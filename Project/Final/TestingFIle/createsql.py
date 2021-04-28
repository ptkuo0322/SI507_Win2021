import sqlite3
# connect to database
conn = sqlite3.connect("practice.db")
conn.execute("PRAGMA foreign_keys = ON")

conn.commit()
# The database will be saved in the location where your 'py' file is saved
c = conn.cursor()

# Create table - YELP
c.execute('''CREATE TABLE if NOT EXISTS FOOD_RESULT ( [GeneralId] INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, [RestaurantName] text, 
            [PhoneNumber] text, [ReviewCount] REAL, [Rating] REAL, [Address] text, 
            [Longitude] text, [Latitude] text, [UrlLink] text, [Id] INTEGER )''')
            

conn.commit()
