import sqlite3
# connect to database
conn = sqlite3.connect("YelpSearch.db")
conn.execute("PRAGMA foreign_keys = ON")

conn.commit()
# The database will be saved in the location where your 'py' file is saved
c = conn.cursor()

# Create table - YELP
c.execute('''CREATE TABLE if NOT EXISTS FOOD_RESULT ([RestaurantName] text, 
            [PhoneNumber] text, [ReviewCount] REAL, [Rating] REAL, [Price] text, [Address] text, 
            [Longitude] text, [Latitude] text, [UrlLink] text, [State] text,[RefId] text PRIMARY KEY )''')
            
c.execute('''CREATE TABLE if NOT EXISTS RESTAURANT_RESULT ([RestaurantName] text, 
            [PhoneNumber] text, [ReviewCount] REAL, [Rating] REAL, [Price] text, [Address] text, 
            [Longitude] text, [Latitude] text, [UrlLink] text, [State] text, [RefId] text PRIMARY KEY )''')
            

conn.commit()
