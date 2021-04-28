import sqlite3
# connect to database
conn = sqlite3.connect("YELP.db")
# The database will be saved in the location where your 'py' file is saved
c = conn.cursor()

# Create table - YELP
c.execute('''CREATE TABLE YELP_RESULT ([generated_id] INTEGER PRIMARY KEY, [RestaurantName] text, 
            "PhoneNumber" text, "ReviewCount" REAL, "Rating" REAL, "Longitude" text, "Latitude", text, "UrlLink" text)''')

conn.commit()