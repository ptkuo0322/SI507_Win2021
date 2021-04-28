import sqlite3
# connect to database
conn = sqlite3.connect("Test.db")
# The database will be saved in the location where your 'py' file is saved
c = conn.cursor()

# Create table - CLIENTS
c.execute('''CREATE TABLE CLIENTS
            ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [Country_ID] integer, [Date] date)''')

# Create table - COUNTRY
c.execute('''CREATE TABLE COUNTRY
            ([generated_id] INTEGER PRIMARY KEY,[Country_ID] integer, [Country_Name] text)''')

# Create table - DAILY_STATUS
c.execute('''CREATE TABLE DAILY_STATUS
            ([Client_Name] text, [Country_Name] text, [Date] date)''')


conn.commit()