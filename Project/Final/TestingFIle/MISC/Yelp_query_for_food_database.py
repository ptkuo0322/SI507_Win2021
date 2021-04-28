
# Import the modules
import requests
import json
import pandas as pd
import csv 
import sqlite3
import time
from pandas import DataFrame
from googleapiclient.discovery import build


# Define my API Key, My Endpoint, and My Header
API_KEY = 'c2GgFaTUbluwOQFNZjLY35_G8KdzPdZfxi64b2Hwz7ADbQUsR_BDBL48WYm6QCLp9MkswmS79HAazAUOJzUKS7u6S6bAfQosjFpjNG58jHZkohXL1Mq8GmsorCtlYHYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# Define my parameters of the search
# BUSINESS SEARCH PARAMETERS - EXAMPLE

query_string1 = input("please input the food/restaurant")

query_string2 = input("please input the location")

PARAMETERS = {'term': query_string1,
            'radius': 10000,
            'location': query_string2}

# Request to the Yelp API
response = requests.get(url = ENDPOINT,
                        params = PARAMETERS,
                        headers = HEADERS)


# Conver the JSON String
business_data = response.json()

#parse the query result for food

# create list ele inside a list for csv
blist = []
for idx in range(len(business_data["businesses"])):
    for ele in business_data["businesses"][idx]:
        alist = []
        alist.append(idx)   
        alist.append(business_data["businesses"][idx]["name"])        
        alist.append(business_data["businesses"][idx]["review_count"])
        alist.append(business_data["businesses"][idx]["rating"])
        alist.append(business_data["businesses"][idx]["coordinates"]['longitude'])
        alist.append(business_data["businesses"][idx]["coordinates"]['latitude'])
        alist.append(business_data["businesses"][idx]["location"]['display_address'])
        alist.append(business_data["businesses"][idx]["display_phone"])
        alist.append(business_data["businesses"][idx]["url"])
    blist.append(alist)

#print(blist[1])
#print(blist[2])


# add header to csv file and write to files
headers = ['id','name', 'review_count', 'rating', 'longitude', 'latitude', 'address', 'display_phone', ['url']]

with open('test2221.csv', 'w') as outfile:
    csvwriter = csv.writer(outfile)
    csvwriter.writerow(headers)
    csvwriter.writerows(blist)

# create database for the csv 

conn = sqlite3.connect("yelpDB.db")
# The database will be saved in the location where your 'py' file is saved
c = conn.cursor()

# Create table - Food
#c.execute('''CREATE TABLE Food
#            ([generated_id] INTEGER PRIMARY KEY,[name] text, [url] text, [review_count] integer, [rating] integer, [longitude] integer, [latitude] integer, [address] text , [display_phone] text)''')

read_clients = pd.read_csv('/Users/pkuo/Desktop/SI507_finalProject/test.csv')
read_clients.to_sql('Food', conn, if_exists='replace', index = False)

conn.commit()
