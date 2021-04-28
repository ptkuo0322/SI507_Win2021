import sqlite3
import pandas as pd
from pandas import DataFrame


# connect to database
conn = sqlite3.connect("TesTDB.db")
# The database will be saved in the location where your 'py' file is saved
c = conn.cursor()

#read csv file in pandas way, and  insert the values from the csv file into the table 'NAME'
read_clients = pd.read_csv('/Users/pkuo/Desktop/Testing_file/test5.csv')
read_clients.to_sql('CLIENTS', conn, if_exists='append', index = False)

# # Replace the values from the csv file into the table 'COUNTRY'
read_country = pd.read_csv('/Users/pkuo/Desktop/Testing_file/test6.csv')
read_country.to_sql('COUNTRY', conn, if_exists='replace', index = False)

#
c.execute('''
INSERT INTO DAILY_STATUS (Client_Name,Country_Name,Date) 
SELECT DISTINCT clt.Client_Name, ctr.Country_Name, clt.Date
FROM CLIENTS clt
LEFT JOIN COUNTRY ctr ON clt.Country_ID = ctr.Country_ID
          ''')

c.execute('''
SELECT DISTINCT *
FROM DAILY_STATUS
WHERE Date = (SELECT max(Date) FROM DAILY_STATUS)
          ''')

df = DataFrame(c.fetchall(), columns=['Client_Name','Country_Name','Date'])
print (df)

#print(c.fetchall())

# print in format

df = DataFrame(c.fetchall(), columns=['Client_Name','Country_Name','Date'])
print (df) # To display the results after an insert query, you'll need to add this type of syntax above: 'c.execute(''' SELECT * from latest table ''')

df.to_sql('DAILY_STATUS', conn, if_exists='append', index = False) # Insert the values from the INSERT QUERY into the table 'DAILY_STATUS'

# export_csv = df.to_csv (r'C:\Users\Ron\Desktop\Client\export_list.csv', index = None, header=True) # Uncomment this syntax if you wish to export the results to CSV. Make sure to adjust the path name
# Don't forget to add '.csv' at the end of the path (as well as r at the beg to address special characters)