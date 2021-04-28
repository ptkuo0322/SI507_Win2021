# these are the module for use
import requests
import json
import pandas as pd
import csv 
import sqlite3
from pandas import DataFrame
import webbrowser
import time
from googleapiclient.discovery import build
import secrets


def load_cache():
    ''' To read the dictionary from the cache file if it exists, if not, create
    an empty dictionary

    Parameters
    ----------
    None

    Returns
    -------
    dict
        information store in the cache, which is a dictionary
    '''
    try:
        cache_file = open('RestaruantOrFood.json', 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache


# This section is for API keys (need to be in secret code)
YELP_API_KEY = secrets.YELP_API_KEY

# This section for Yelp query
YELP_BASEURL = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % YELP_API_KEY}

# Define my parameters of the search

# BUSINESS SEARCH PARAMETERS - EXAMPLE

query_name = input("please input the food/restaurant")
query_name = query_name.lower().strip(" ")
time.sleep(1)
query_location = input("please input the location")
query_location = query_location.lower().strip(" ")
query_string = query_name + query_location
time.sleep(1)
PARAMETERS = {'term': query_name,'radius': 10000,'location': query_location}

# Request to the Yelp API
response = requests.get(url = YELP_BASEURL,params = PARAMETERS,headers = HEADERS)
business_data = response.json()


# create json file for cache and furture use [need to add with cache]

if len(query_name) == 0:
    #filenameJ = "Restaurant.json"
    filenameC = "Restaurant.csv"
elif len(query_name) != 0:
    #filenameJ = "Food.json"
    filenameC = "Food.csv"

outer_list = []
for idx in range(len(business_data["businesses"])):
    for ele in business_data["businesses"][idx]:
        inner_list = []
        inner_list.append(idx)   
        inner_list.append(business_data["businesses"][idx]["name"])
        inner_list.append(business_data["businesses"][idx]["display_phone"])    
        inner_list.append(business_data["businesses"][idx]["review_count"])
        inner_list.append(business_data["businesses"][idx]["rating"])
        inner_list.append(business_data["businesses"][idx]["location"]['display_address'])
        inner_list.append(business_data["businesses"][idx]["coordinates"]['longitude'])
        inner_list.append(business_data["businesses"][idx]["coordinates"]['latitude'])
        inner_list.append(business_data["businesses"][idx]["url"])
        inner_list.append(business_data["businesses"][idx]["id"])
    outer_list.append(inner_list)



cache_dicte = load_cache()
if query_string not in cache_dicte.keys():
    print("fetching data from API")
    cache_dict[query_string] = outer_list
else:
    print("readling from cache ")
    cache_dict = cache_dict

# create json file for cache and furture use [need to add with cache]
with open('RestaruantOrFood.json', 'w') as outfile:
    json.dump(cache_dict, outfile)

with open(filenameC, 'w') as outfile:
    json.dump(business_data, outfile)
