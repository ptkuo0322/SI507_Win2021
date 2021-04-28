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


# This section is for API keys (need to be in secret code)
YELP_API_KEY = 'c2GgFaTUbluwOQFNZjLY35_G8KdzPdZfxi64b2Hwz7ADbQUsR_BDBL48WYm6QCLp9MkswmS79HAazAUOJzUKS7u6S6bAfQosjFpjNG58jHZkohXL1Mq8GmsorCtlYHYx'
MAP_API_KEY = "AIzaSyBaCdZ4_5GiifOCE4PXGhyno6AwpVsCE-U"
YOUTUBE_API_KEY = 'AIzaSyDi9NtuLf43xi37SiMjPF6BwCgQtHVrY3o'

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

#parse the query result for food (need to add cache code)
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
    outer_list.append(inner_list)

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

def load_cache1():
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


cach_dict = load_cache()

if query_string not in cach_dict.keys():
    print("fetching data from API")
    cach_dict[query_string] = outer_list
else:
    print("readling from cache ")
    cach_dict = cach_dict

# create json file for cache and furture use [need to add with cache]
with open('RestaruantOrFood.json', 'w') as outfile:
    json.dump(cach_dict, outfile)

# create csv file for SQL database and furture use [need to add with cache]
headers = ['name', 'display_phone', 'review_count', 'rating','address', 'longitude', 'latitude', ['url']]

with open('RestaruantOrFood.csv', 'w') as outfile:
    csvwriter = csv.writer(outfile)
    csvwriter.writerow(headers)
    csvwriter.writerows(outer_list)
    


# This section for generate SQL database and plug in the value
conn = sqlite3.connect("YELP.db")
c = conn.cursor()
    #Read the csv file, plug in the value
read_clients = pd.read_csv('/Users/pkuo/Desktop/SI507_finalProject/RestaruantOrFood.csv')
read_clients.to_sql('YELP_RESULT', conn, if_exists='append', index = False) # if_exist, it will replace the old value, if not exist, it will append





# This section for search the related videos on Youtube
    # Setting for youtube API
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
#print("aaaaa")
#print(cach_dict)
#print('BBBBBBB')
name_list = []
#print out the restaurant name for usr to choose
for idx, ele in enumerate(cach_dict[query_string]):
    name_list.append(ele[1])
    print(idx+1, ele[1])


#user choose the restaurant for the related video on YOutube
choose_restaurant = input("which restaurant do you want? Please enter the number")
time.sleep(1)

youtube_request = youtube.search().list(part='snippet',q=name_list[int(choose_restaurant)-1]) # maxResult= 0~ 50 default 5 maxResults="2"
youtube_response = youtube_request.execute()


#print(len(response))  

#print(youtube_response)

#with open('2.json', 'w') as outfile:
#    json.dump(youtube_response, outfile)  

# same name problem of restaurant need to be fixed

link = ""
link_list = []
for idx in range(len(youtube_response)-2):
    for ele in youtube_response['items'][idx]['snippet']['thumbnails']['default']['url']:
        link += ele
    link_list.append(link.split('/')[-2])

#print(link_list)

# new cache for Youtube link
cache_dict = {}
cache_dict[name_list[int(choose_restaurant)-1]] = link_list
with open('YouTube.json', 'w') as outfile:
    json.dump(cache_dict, outfile)


# open new windows for related videos in youtube
watchUrl = "https://www.youtube.com/watch?"
id = link_list
for ele in id:
    webbrowser.open_new("{}v={}".format(watchUrl,ele))



# This section for GOOGLE MAP -- show the relative location on a static map
GOOGLEMAP_BASE_URL = "https://maps.googleapis.com/maps/api/staticmap?"

# parameters
#CITY = query_location

loc_list=[]
for idx, ele in enumerate(cach_dict[query_string]):
    loc= ""
    loc = str(cach_dict[query_string][idx][7]) + "," + str(cach_dict[query_string][idx][6])
    loc_list.append(loc)
print(loc_list)

query_list = []

for idx, ele in enumerate(loc_list):
    astring = f'&markers=label:{idx+1}|{ele}'
    query_list.append(astring)
    
#print(query_list)

query_word = ""
for ele in query_list:
    query_word += ele

#print(query_word)

# updating the URL

URL = GOOGLEMAP_BASE_URL + "center=" + query_location + "&zoom=13" + "&size=2180x1080&key=" + MAP_API_KEY +"&maptype=roadmap" + query_word

result = requests.get(URL)
print(URL)


#with open('3.json', 'w') as outfile:
#    json.dump(URL, outfile)  
#webbrowser.open_new(URL)

# This section for GOOGLE MAP -- show direction page to the specific restaurant on google map

# This part is for Google Maps URLs 

usr_res = input("Would you like to use the GOOGLE MAP for Direction?, Yes or no")
usr_res = usr_res.lower().strip(" ")
if usr_res == "yes":
    for idx, ele in enumerate(cach_dict[query_string]):
    #name_list.append(ele[1])
        print(idx+1, ele[1])
elif usr_res == "no":
    print("Thank you, and google bye!")
    time.sleep(1)
    exit()
else:
    print("invalid input")  # need to fixed the loop here

time.sleep(1)
usr_res = input("Which you would you like to direct to? Enter the number! ")
loca = loc_list[int(usr_res)-1]

# base url
map_url = "https://www.google.com/maps/search/?api=1"

# get response

print(result)

result = map_url + "&query=" + loca
#print(r)
print(result)
with open('4.json', 'w') as outfile:
    json.dump(result, outfile)  
#webbrowser.open_new(result)
