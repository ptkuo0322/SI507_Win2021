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
import os
import plotly.graph_objs as go
from plotly.subplots import make_subplots

## general setting 

# instruction 

instruction = '''This program provides two way of search:
---------------------------------------------------------------------------------
1. Instant search on Yelp for specific type of food or restaurant
2. Search the Restaurants existing in the database based on Reviews/Rating/Price
---------------------------------------------------------------------------------
note: option 1 is able to expand the database used in option2.
'''
instructionforone:'''
this option allows you to search the Food or restaruant On Yelp. 
You are required to enter the following information:
-------------------------------------------------------------------------------------------
    -- Food/Restaurant (optional)
    -- Location (required)
-------------------------------------------------------------------------------------------

    You would be able to see the following information:

-------------------------------------------------------------------------------------------
    -- The search results in text format
    -- The related videos about search results on YouTube
    -- The location information of the search results on static google map
    -- The direction to the search results on google map
-------------------------------------------------------------------------------------------

    Also, you can type "exit" to quit anytime
'''

instructionfortwo:'''
This option allows you to search and compare the restaruant in particular state of USA
You are required to enter the following information:
-------------------------------------------------------------------------------------------
    -- State in abbreivation. e.g. MI, TX, OH...
    -- Filtering condition
    -- number of search result you wish (The final results may be less than you expected)
    -- Order of the search result
-------------------------------------------------------------------------------------------

    You would be able to see the following information:

-------------------------------------------------------------------------------------------
    -- The search results in text format
    -- The search results in figure format(bar chart, radar chart)
-------------------------------------------------------------------------------------------
    Also, you can type "exit" to quit anytime
'''

# This section is for API keys (need to be in secret code)
YELP_API_KEY = secrets.YELP_API_KEY
YELP_BASEURL = 'https://api.yelp.com/v3/businesses/search'
YtWatchhUrl = "https://www.youtube.com/watch?"
map_url = "https://www.google.com/maps/search/?api=1"
YOUTUBE_API_KEY = secrets.YOUTUBE_API_KEY
MAP_API_KEY = secrets.MAP_API_KEY
HEADERS = {'Authorization': 'bearer %s' % YELP_API_KEY}
symbol_list = ['A','B','C','D','E','F','G','H','I','J','H']
query_list0 = []
query_list1 = []
query_list2 = []
query_list3 = []
query_list4 = []
name_list = []
final_list = []

instruction = '''This is a program that allows you to search the Food or restaruant On Yelp. You can enter the food/restaurant(optional)
    and the location(required) for search. You would be able to see the following information:
-------------------------------------------------------------------------------------------
    -- The search results in text format
    -- The search results in figure format
    -- The related videos about search results on YouTube
    -- The location information of the search results on static google map
    -- The direction to the search results on google map
-------------------------------------------------------------------------------------------
    Also, you can type "exit" to quit anytime
        '''

def read_loc_cache():
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
        cache_file = open('ResultofLocation.json', 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache  #return a dictionary

def write_to_Loc_cache(cache_dict):
    ''' output the data searched by location to json file
    
    Parameters
    ----------
    cache_dict
        the searched data stored in dictionary format

    Returns
    -------
    none
    '''
    with open("ResultofLocation.json", "w") as outputfile:
            json.dump(cache_dict, outputfile)

def write_to_Food_cache(cache_dict):
    ''' output the data searched by food or restaurant 
        along with location to json file
    
    Parameters
    ----------
    cache_dict
        the searched data stored in dictionary format

    Returns
    -------
    none
    '''
    with open("ResultofFOOD.json", "w") as outputfile:
            json.dump(cache_dict, outputfile)

    
def write_to_csv(result, filename):
    ''' output the search result with headers to csv file 
    
    Parameters
    ----------
    result
        the search result
    
    filename
        the csv file

    Returns
    -------
    none
    '''
    file_exists = os.path.isfile(filename)
    with open(filename, 'a+', newline='') as outfile:
        headers = ['id','RestaurantName', 'PhoneNumber', 'ReviewCount', 'Rating', 'Price', 'Address', 'Longitude', 'Latitude', 'UrlLink', 'State', 'RefId']
        file_is_empty = os.stat(filename).st_size == 0
        writer = csv.writer(outfile)
        if file_is_empty:
            writer.writerow(headers)
        writer.writerows(result)    


def read_rest_cache():
    ''' read the dictionary from the cache file if it exists, 
        if not, create an empty dictionary
    
    Parameters
    ----------
    None

    Returns
    -------
    dictonary 
        the data in dictionary format that read from json file
    ''' 
    try:
        cache_file = open('ResultofFOOD.json', 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache 

def read_loc_cache():
    ''' read the dictionary from the cache file if it exists, 
        if not, create an empty dictionary
    
    Parameters
    ----------
    None

    Returns
    -------
    dictonary 
        the data in dictionary format that read from json file
    '''
    try:
        cache_file = open('ResultofLocation.json', 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache 

def search_yelp(query_name, query_location):
    ''' search the food/restaurant information on Yelp
    
    Parameters
    ----------
    query_name
        either restaurant name or food name 
    
    query_location
        the places such as cities, countries or so

    Returns
    -------
    outer_list 
        a list with specific information about the search results
    '''
    PARAMETERS = {'term': query_name,'radius': 10000,'location': query_location, 'limit': 50}
    response = requests.get(url = YELP_BASEURL,params = PARAMETERS,headers = HEADERS)
    res_data = response.json()
    with open('see.json','w') as obj:
            json.dump(res_data, obj)
    outer_list = []
    if 'error' in res_data.keys():
        print("invalid input cause error! please restart the program again")
        exit()
    for idx in range(len(res_data["businesses"])):
        for ele in res_data["businesses"][idx]:
            inner_list = []
            inner_list.append(idx)   
            inner_list.append(res_data["businesses"][idx]["name"])
            inner_list.append(res_data["businesses"][idx]["display_phone"])    
            inner_list.append(res_data["businesses"][idx]["review_count"])
            inner_list.append(res_data["businesses"][idx]["rating"])
            if 'price' in res_data["businesses"][idx].keys():
                if res_data['businesses'][idx]['price'] == '$':
                    inner_list.append("1")
                elif res_data['businesses'][idx]['price'] == '$$':
                    inner_list.append("2")
                elif res_data['businesses'][idx]['price'] == '$$$':
                    inner_list.append("3")
                elif res_data['businesses'][idx]['price'] == '$$$$':
                    inner_list.append("4")
                elif res_data['businesses'][idx]['price'] == '$$$$$':
                    inner_list.append("5")
            else:
                inner_list.append("0")
            
            inner_list.append(res_data["businesses"][idx]["location"]['display_address'])
            inner_list.append(res_data["businesses"][idx]["coordinates"]['longitude'])
            inner_list.append(res_data["businesses"][idx]["coordinates"]['latitude'])
            inner_list.append(res_data["businesses"][idx]["url"])
            inner_list.append(res_data["businesses"][idx]["location"]["state"])
            inner_list.append(res_data["businesses"][idx]["id"])
        outer_list.append(inner_list)
        with open('see3.json','w') as obj:
            json.dump(outer_list, obj)
    return outer_list


def update_database(query_name):
    ''' update the data stored in SQL database
    
    Parameters
    ----------
    query_name
        either restaurant name or food name 

    Returns
    -------
    none 
        
    '''
    conn = sqlite3.connect("practice1.db")
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    if len(query_name) == 0:
        read_clients = pd.read_csv('/Users/pkuo/Desktop/SI507_finalProject/FInalcode/FinalProject/loc.csv')
        read_clients.to_sql('RESTAURANT_RESULT', conn, if_exists='replace', index = False) # if_exist, it will replace the old value, if not exist, it will append
    elif len(query_name) != 0:
        read_clients = pd.read_csv('/Users/pkuo/Desktop/SI507_finalProject/FInalcode/FinalProject/food.csv')
        read_clients.to_sql('FOOD_RESULT', conn, if_exists='replace', index = False) # if_exist, it will replace the old value, if not exist, it will append


def path_decision(query_name, query_location):
    ''' update the cache and csv files based on the query information
    
    Parameters
    ----------
    query_name
        either restaurant name or food name 

    query_location
        the places such as cities, countries or so

    Returns
    -------
    cache_dict
        the dictionary with search results 
    '''
    if len(query_name) == 0:
        query_string = query_name + query_location
        search_result = search_yelp(query_name, query_location)
        cache_dict = read_loc_cache()
        if query_string not in cache_dict.keys():
            print("fetching data from API")
            cache_dict[query_string] = search_result
            #print(cache_dict[query_string])
            #print(cache_dict)
            write_to_Loc_cache(cache_dict)
            ## write to csv
            filenameC = "loc.csv"
            write_to_csv(search_result,filenameC)
        else:
            print("readling from cache ")
            #print(cache_dict[query_string])
    else:
        search_result = search_yelp(query_name, query_location)
        cache_dict = read_rest_cache()
        if query_string not in cache_dict.keys():
            print("fetching data from API")
            cache_dict[query_string] = search_result
            #print(cache_dict[query_string])
            #print(cache_dict)
            write_to_Food_cache(cache_dict)
            ## write to csv
            filenameC = "food.csv"
            write_to_csv(search_result,filenameC)
        else:
            print("readling from cache ")
            #print(cache_dict[query_string])
    update_database(query_name)
    
    return cache_dict


### for youtube case

def yt_search(query_name, query_location, query_string):
    ''' search the related videos on Youtube and display on the browsers
    
    Parameters
    ----------
    query_name
        the food/restaurant  information
    
    query_location
        the  location information

    query_string
        the food/restaurant and location information

    Returns
    -------
    None
    '''
    link = ""
    link_list = []
    result =  path_decision(query_name, query_location)
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    name_list = []
    #print out the restaurant name for usr to choose
    print("---------------------------------------------------")
    print("The search results are the following ")
    for idx, ele in enumerate(result[query_string]):
        name_list.append(ele[1])
        print(idx+1, ele[1])
    print("---------------------------------------------------")
    while True:
        choose_restaurant = input("which restaurant do you want or skip this step ? Please enter the number or type in 'skip' ")
        if choose_restaurant.strip(' ').lower() == 'skip':
            break
        elif choose_restaurant.strip(' ').lower().isnumeric() and 0 <= int(choose_restaurant.strip(' ').lower()) <= len(result[query_string]):
            youtube_request = youtube.search().list(part='snippet',q=name_list[int(choose_restaurant)-1]) # maxResult= 0~ 50 default 5 maxResults="2"
            youtube_response = youtube_request.execute()
            for idx in range(len(youtube_response)-2):
                for ele in youtube_response['items'][idx]['snippet']['thumbnails']['default']['url']:
                    link += ele
                link_list.append(link.split('/')[-2])
            open_youtube(link_list)
            break
        else:
            print("Invalid Input. Please try again")
            


def open_youtube(link_list):
    ''' ask the user whether to open the videos on YouTube
    
    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    
    while True:
        ans = input("would you like to open the relative videos on the YouTube? Yes or No ? ")
        if ans.strip(" ").lower() == "yes":
            for ele in link_list:
                webbrowser.open_new("{}v={}".format(YtWatchhUrl,ele))
            break
        elif ans.strip(" ").lower() == "no":
            print("OK! Thank you, let's go to next step!!")
            break
        else:
            print("invalid input! Plsase try again")


# This section for GOOGLE MAP -- show the relative location on a static map
GOOGLEMAP_BASE_URL = "https://maps.googleapis.com/maps/api/staticmap?"

# parameters
#CITY = query_location

def open_static_map(urlLink):
    ''' ask the user whether to show the search results on static google map
    
    Parameters
    ----------
    urlLink
        the url that links to google map

    Returns
    -------
    None
    '''
    
    while True:
        ans = input("would you like to know the relative location on the Map? Yes or No or skip ? ")
        if ans.strip(" ").lower() == "yes":
            webbrowser.open_new(urlLink)
            break
        elif ans.strip(" ").lower() == "no":
            print("OK! Thank you, let's go to next step!!")
            break
        elif ans.strip(" ").lower() == "skip":
            print(("OK! Thank you, let's skip this step and go to next step!!"))
            break
        else:
            print("invalid input! Plsase try again")

            
def count_query_list(loc_list):
    ''' construct the information in specific format for static google API
    
    Parameters
    ----------
    loc_list
        the list that contains all the location information of the search results

    Returns
    -------
    final_list
        the list contains the query information for static map API
    '''

    for idx, ele in enumerate(loc_list):
        if 40 <= len(loc_list):
            if idx in range(0,10):
                astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
                query_list0.append(astring)
            if idx in range(10,20):
                print(idx)
                astring = f"&markers=label:{symbol_list[(idx%10)]}|{ele}"
                query_list1.append(astring)
            if idx in range(20,30):
                astring = f"&markers=label:{symbol_list[(idx%10)]}|{ele}"
                query_list2.append(astring)
            if idx in range(30,40):
                astring = f"&markers=label:{symbol_list[(idx%10)]}|{ele}"
                query_list3.append(astring)
            if idx in range(40,51):
                astring = f"&markers=label:{symbol_list[(idx%10)]}|{ele}"
                query_list4.append(astring)
        elif 30 <= len(loc_list) < 40:
            if idx in range(0,10):
                astring = f"&markers=label:{symbol_list[(idx%10)]}|{ele}"
                query_list0.append(astring)
            if idx in range(10,20):
                astring = f"&markers=label:{symbol_list[(idx%10)]}|{ele}"
                query_list1.append(astring)
            if idx in range(20,30):
                astring = f"&markers=label:{symbol_list[(idx%10)]}|{ele}"
                query_list2.append(astring)
            if idx in range(30,40):
                astring = f"&markers=label:{symbol_list[(idx%10)]}|{ele}"
                query_list3.append(astring)
        elif 20 <= len(loc_list) < 30:
            if idx in range(0,10):
                astring = f"&markers=label:{symbol_list[(idx%10)]}|{ele}"
                query_list0.append(astring)
            if idx in range(10,20):
                astring = f"&markers=label:{symbol_list[(idx%10)]}|{ele}"
                query_list1.append(astring)
            if idx in range(20,30):
                astring = f"&markers=label:{symbol_list[(idx%10)]}|{ele}"
                query_list2.append(astring)
        elif 10 <= len(loc_list) < 20:
            if idx in range(0,10):
                astring = f"&markers=label:{symbol_list[(idx%10)]}|{ele}"
                query_list0.append(astring)
            if idx in range(10,20):
                astring = f"&markers=label:{symbol_list[(idx%10)]}|{ele}"
                query_list1.append(astring)
        elif 0 <= len(loc_list) < 10:
            astring = f"&markers=label:{symbol_list[(idx%10)]}|{ele}"
            query_list0.append(astring)  

    if len(loc_list) < 10:
        final_list.append(query_list0)
    elif 10 <=len(loc_list) < 20:
        final_list.append(query_list0)
        final_list.append(query_list1)
    elif 20 <=len(loc_list) < 30:
        final_list.append(query_list0)
        final_list.append(query_list1)
        final_list.append(query_list2)
    elif 30 <=len(loc_list) < 40:
        final_list.append(query_list0)
        final_list.append(query_list1)
        final_list.append(query_list2)
        final_list.append(query_list3)
    elif 40 <=len(loc_list):
        final_list.append(query_list0)
        final_list.append(query_list1)
        final_list.append(query_list2)
        final_list.append(query_list3)
        final_list.append(query_list4)
    return final_list

def show_related_loc(query_name, query_location,query_string):
    ''' display the searched restaurants/foods with relative location 
        in both command line prompt and figure format
    
    Parameters
    ----------
    query_name
        either restaurant name or food name 

    query_location
        the places such as cities, countries or so
    
    query_string
        the food/restaurant and location information

    Returns
    -------
    loc_list
        the list contains the location information about the searched results
    '''

    result =  path_decision(query_name, query_location)
    loc_list=[]
    name_list = []
    query_word = ""
    for idx, ele in enumerate(result[query_string]):
        loc= ""
        loc = str(result[query_string][idx][8]) + "," + str(result[query_string][idx][7])
        loc_list.append(loc)
        name_list.append(result[query_string][idx][1])
    result_list = count_query_list(loc_list)
    for idx1, listele in enumerate(result_list):
        print("---------------------------------------------------")
        for idx, ele in enumerate (listele):
            query_word += ele
            if idx % 10 == 0:
                print(f'This is shown in {idx1+1} page')
            print(symbol_list[idx], name_list[idx+(idx1*10)]) 
        print("---------------------------------------------------")
        URL = GOOGLEMAP_BASE_URL + "center=" + query_location + "&zoom=13" + "&size=1344x768&scale=2&key=" + MAP_API_KEY +"&maptype=roadmap" + query_word
        #print(URL)
        open_static_map(URL)
        URL = ""
        query_word = ""
    return loc_list


def go_direction(query_name, query_location, query_string):
    ''' display the direction of the searched result on google map
    
    Parameters
    ----------
    query_name
        either restaurant name or food name 

    query_location
        the places such as cities, countries or so
    
    query_string
        the string constructed by query_name and query_location

    Returns
    -------
    none

    '''
    option_list = ['yes', 'no']
    dict_result = path_decision(query_name, query_location)
    #print(dict_result)
    while True:
        usr_res = input("Would you like to direction to the location ? Yes or no?")
        if usr_res.strip(" ").lower() in option_list:
            if usr_res.strip(" ").lower() == 'yes':
                for idx, ele in enumerate(dict_result[query_string]):
                    print(idx+1, ele[1])
                usr_res1 = input("Which you would you like to direct to? Enter the number! ")
                loc = dict_result[query_string][int(usr_res1)-1][7]
                lat = dict_result[query_string][int(usr_res1)-1][6]
                coord = str(loc) + "," + str(lat)
                print(coord)
                result = map_url + "&query=" + coord
                webbrowser.open_new(result)
                break
            elif usr_res.strip(" ").lower() == 'no':
                print("skip this step!")
                break
        else:
            print("invalid input")

def draw_barplot(alist):
    ''' draw the bar plot
    
    Parameters
    ----------
    alist
        the list contains the information for bar plots

    Returns
    -------
    none
    '''
    usr_input = input("which one do you want to comapre, Average rating = 1, Review_account =0")
    xval = []
    yval1 = []
    yval2 = []
    yval3 = []
    fig = make_subplots(rows=2, cols=3, subplot_titles=("Rate", "Review_count ", "price_range"))
#layout = {'range' :[0:5]}
    for ele in alist:
        xval.append(ele[0])
        yval1.append(ele[2])
        yval2.append(ele[3])
        yval3.append(ele[4])
    fig.add_trace(go.Bar(x=xval, y=yval1), row=1 , col=1)
    fig.add_trace(go.Bar(x=xval, y=yval2), row=1 , col=2)
    fig.add_trace(go.Bar(x=xval, y=yval3), row=1 , col=3)
    fig.update_yaxes(range=[0, 5], row=1, col=3)
    fig.update_layout(showlegend=False)
    fig.show()


def scale_convert(alist):
    ''' convert the data scale
    
    Parameters
    ----------
    alist
        the list contains the data for conversion
        
    Returns
    -------
    final_result
        the search results
    '''
    for ele in alist:
        print(ele[4])
        if ele[3] >= 2000:
            ele[3] = 5
        elif 2000 > ele[3] >= 1800:
            ele[3] = 4.75
        elif 1800 > ele[3] >= 1600:
            ele[3] = 4.5
        elif 1600 > ele[3] >= 1400:
            ele[3] = 4.25
        elif 1400 > ele[3] >= 1200:
            ele[3] = 4.0
        elif 1200 > ele[3] >= 1000:
            ele[3] = 3.75
        elif 1000 > ele[3] >= 800:
            ele[3] = 3.5
        elif 800 > ele[3] >= 600:
            ele[3] = 3.25
        elif 600 > ele[3] >= 400:
            ele[3] = 3.0
        elif 400 > ele[3] >= 200:
            ele[3] = 2.75
        elif 200 > ele[3] >= 100:
            ele[3] = 2.5    
        elif 100 > ele[3] >= 50:
            ele[3] = 2.0  
        elif 50 > ele[3] >= 0:
            ele[3] = 1.0
    return alist


def draw_radarplot(alist):
    ''' draw the radar plot
    
    Parameters
    ----------
    alist
        the list contains the information for radar plots
        
    Returns
    -------
    none
    '''
    converted_list = scale_convert(alist)
    cate = ["AverageRating", "Review", "Price"]
    fig = go.Figure()
    for i in range(len(converted_list)):
        fig.add_trace(go.Scatterpolar(r=[alist[i][2], alist[i][3], alist[i][4]],theta=cate, fill='toself',name=alist[i][0]))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True,range=[0, 5])),showlegend=True)

    fig.show()

def search_condition():
    ''' construct the query information for SQL database
    
    Parameters
    ----------
    None
        
    Returns
    -------
    query_list
        the query list for SQL database
    '''

    instruction = '''What kind of filtering condition would you like?
    1. filtered by Rating first and ordered by ReviewCount.
    2. filtered by Rating first and ordered by Price.
    3. filtered by ReviewCount first and ordered by Rating.
    4. filtered by ReviewCount first and ordered by Price.
    5. filtered by Price first and ordered by Rating.
    6. filtered by Price first and ordered by ReviewCount.
    '''
    option_list = ['1','2','3','4','5','6']
    rating_list = ["0", '0.5','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0']
    price_list = ["0", '1','2','3','4','5']
    while True:
        print(instruction)
        usr_input = input("what's your choice? from 1 to 6 ")
        if usr_input in option_list:
            if usr_input == "1":
                query_list = ["R.Rating", "R.ReviewCount"]
                print("Rating range:", rating_list)
                usr_input2 =input("Enter the number, please! ")
                if usr_input2 in rating_list:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")
            elif usr_input == "2":
                query_list = ["R.Rating", "R.Price"]
                print("Rating range:", rating_list)
                usr_input2 =input("Enter the number, please! ")
                if usr_input2 in rating_list:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")
            elif usr_input == "3":
                query_list = ["R.ReviewCount", "R.Rating"]
                print("ReviewCount range: at least 1")
                usr_input2 =input("Enter the number, please! ")
                if bool(int(usr_input2))==True and int(usr_input2) > 0:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")

            elif usr_input == "4":
                query_list = ["R.ReviewCount", "R.Price"]
                print("ReviewCount range: at least 1")
                usr_input2 =input("Enter the number, please! ")
                if bool(int(usr_input2))==True and int(usr_input2) > 0:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")

            elif usr_input == "5":
                query_list = ["R.Price", "R.Rating"]
                print("Price range:", price_list)
                usr_input2 =input("Enter the number, please! ")
                if usr_input2 in price_list:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")
            elif usr_input == "6":
                query_list = ["R.Price", "R.ReviewCount"]
                print("Price range:", price_list)
                usr_input2 =input("Enter the number, please! ")
                if usr_input2 in price_list:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")
        else:
            print("invalid input!, please try again!")
    return query_list

def search_order():
    ''' construct the query information for SQL database
    
    Parameters
    ----------
    None
        
    Returns
    -------
    query_word
        the query word for SQL database
    '''

    instruction = '''which order would you like?
    1, in ascending order.
    2, in descending order.
    '''
    option_list = ['1','2']
    print(instruction)
    while True:
        usr_input = input("what's your choice? from 1 to 2 ")
        if usr_input in option_list:
            if usr_input == "1":
                query_word = "ASC"
                break
            elif usr_input == "2":
                query_word = "DESC"
                break
        else:
            print("invalid input!, please try again!")
    return query_word

def search_number():
    ''' construct the query information for SQL database
    
    Parameters
    ----------
    None
        
    Returns
    -------
    query_word
        the query word for SQL database
    '''
    instruction = '''How many data do you want to search to compare?
    ranging for 1 to 20
    Note: The results might be less than you sepcify owing to your requirement!
    '''
    print(instruction)
    option_list  = ["1",'2','3','4','5','6','7','8','9','10','11',"12",'13','14','15','16','17','18','19',
    '20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39',
    '40','41','42','43','44','45','46','47','48','49','50']
    while True:
        usr_input = input("what's your choice? from 1 to 30 ")
        if usr_input in option_list:       
            query_word = usr_input
            break
        else:
            print("invalid input!, please try again!")
    return query_word


def search_state():
    ''' construct the query information for SQL database
    
    Parameters
    ----------
    None
        
    Returns
    -------
    query_word
        the query word for SQL database
    '''
    state_list = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY'
    'LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK',
    'OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

    while True:
        print(instruction)
        usr_input = input("Which state do you want to search? Please enter the abbreivation of the state! ex., MI, OH ")
        if usr_input.strip(' ').upper() in state_list:
            query_word = usr_input.strip(' ').upper()
            break
        else:
            print("invalid input!, please try again!")
    return query_word

def sql_query_for_specific_rest():
    ''' construct the ultimate query information for specific restaurant to search in SQL database
    
    Parameters
    ----------
    None
        
    Returns
    -------
    query_term
        the ultimate query word for SQL database
    '''
    nameofrest = input("Please enter name of the restaurant! ")
    query_term = f"SELECT F.RestaurantName, F.PhoneNumber, F.Rating, F.ReviewCount, F.Price FROM FOOD_RESULT AS F JOIN RESTAURANT_RESULT AS R  ON F.RefId = R.RefId WHERE R.RestaurantName='{nameofrest}'"
    return query_term

def sql_query_for_historical_data():
    ''' construct the ultimate query information for SQL database
    
    Parameters
    ----------
    None
        
    Returns
    -------
    query_term
        the ultimate query word for SQL database
    '''
    query_string1 = '''SELECT F.RestaurantName, F.PhoneNumber, F.Rating, F.ReviewCount, F.Price FROM FOOD_RESULT 
    AS F JOIN RESTAURANT_RESULT AS R  ON F.RefId = R.RefId 
    '''
    init_list = search_condition()
    a_word = search_state()
    b_word = search_order()
    c_word = search_number()
    init_list.append(b_word) 
    init_list.append(c_word) 
    init_list.append(a_word) 
    query_string2 = f'WHERE State={init_list[-1]} AND {init_list[0]} > {init_list[2]} ORDER BY {init_list[1]} {init_list[3]} LIMIT {init_list[4]}'
    query_term = query_string1 + query_string2
    return query_term

def array_output(alist):
    ''' display the SQL data in specific format(2D-array)
    
    Parameters
    ----------
    alist
        the list contains SQL data
        
    Returns
    -------
    None
    '''
    outer_row = []
    print('{:<16}{:<16}{:<16}{:<16}{:<16}'.format("RestaurantName","PhoneNumber", "Rating", 'TotalReview', "PriceRange"))
    print('--------------------------------------------------------------------------')
    for row in alist:
        trimmed_row=[]
        for i in range(len(row)):
            if type(row[i]) == str and len(row[i]) > 15:
                trimmed_row.append('{:.<14}..'.format(row[i][0:14]))
            else:
                trimmed_row.append(row[i])
        outer_row.append(trimmed_row)
    for ele in outer_row:
        print('{:<16}{:<16}{:<16}{:<16}{:<16}'.format(ele[0],ele[1],ele[2],ele[3],ele[4]))

def turn_to_list(alist):
    ''' convert the data into list
    
    Parameters
    ----------
    alist
        the original information
        
    Returns
    -------
    outer_list
        the converted data in list format
    '''
    outer_list = []
    for idx in range(len(alist)):
        inner_list = []
        for ele in alist[idx]:
            inner_list.append(ele)
        outer_list.append(inner_list)
    return outer_list

def sql_execute(query_term):
    ''' search the SQL database
    
    Parameters
    ----------
    query_term
        the query string for SQL database
        
    Returns
    -------
    final_result
        the search results
    '''
    final_list = []
    conn = sqlite3.connect('practice1.db')
    cur = conn.cursor()
    result = cur.execute(query_term).fetchall()
    for ele in result:
        if ele not in final_list:
            final_list.append(ele)
        else:
            final_list = final_list
    final_result = turn_to_list(final_list)
    return final_result



def interactive_prompt():
    ''' the active interface between user and the program
    Parameters
    ----------
    none 
    Returns
    -------
    none
    '''
    print(instruction)
    while True: 
        decision = input("what kind of search do you want? Search on Yelp = 1, Search on database = 2, or exit ")
        if decision == "1":
            print(instructionforone)
            time.sleep(1)

            query_name = input("please input the food/restaurant")
            query_name = query_name.lower().strip(" ")
            query_location = input("please input the location")
            query_location = query_location.lower().strip(" ")
            if query_name == 'exit' or query_location == 'exit':
                print("Goodbye! Thank you!")
                exit()
            else:
                query_string = query_name + query_location
                result = path_decision(query_name, query_location)
                array_output(result)
                time.sleep(0.5)
                yt_search(query_name, query_location, query_string)
                time.sleep(0.5)
                show_related_loc(query_name,query_location,query_string)
                time.sleep(0.5)
                go_direction(query_name, query_location,query_string)
                time.sleep(0.5)

        elif decision =='2':
            print(instructionfortwo)
            time.sleep(1)

            query_word = sql_query_for_historical_data()
            sql_result = sql_execute(query_word)
            array_output(result)
            time.sleep(0.5)
            draw_barplot(result)
            time.sleep(0.5)
            draw_radarplot(result)
            time.sleep(0.5)

        elif decision =='exit':
            print("Thank you! Hope you find your desire restaruant! Goodbye!")
            exit()
        else:
            print("Invalid Input! Please try again")
            time.sleep(0.5)
        

if __name__== "__main__":
    interactive_prompt()